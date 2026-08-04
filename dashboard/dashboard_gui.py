"""
VoltGuard — Native Desktop Dashboard (Tkinter, real-time monitoring)
------------------------------------------------------------------------
Continuous live-monitoring dashboard. Instead of running a fixed batch
and showing results all at once, this simulates a real SCADA network
tap: packets arrive one at a time on a timer, get processed through
the full pipeline, and appear in the table live — like a real
intrusion-detection console would.

Run:
    python dashboard/dashboard_gui.py

Features:
  - "Start Monitoring" / "Stop Monitoring" toggle (instead of one-shot run)
  - Packets arrive continuously at an adjustable rate (packets/sec)
  - Pulsing "● LIVE" status indicator while monitoring is active
  - Each row is timestamped with real wall-clock time
  - Table auto-scrolls to the newest event, capped at MAX_ROWS so it
    doesn't grow forever during a long monitoring session
  - Live-updating counts (ALLOW / ALERT / BLOCK) and a rolling
    "commands/sec" throughput readout
  - Export snapshot of everything seen so far to JSON at any time
"""

import sys
import os
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from capture.capture import generate_packet
from parser.parser import parse_packet, PacketParseError
from physics.physics import process_command
from decision.decision import evaluate_command

MAX_ROWS = 300  # cap table size so a long-running session stays responsive


class VoltGuardDashboard(tk.Tk):
    ACTION_COLORS = {
        "ALLOW": "#d4f7d4",
        "ALERT": "#fff3cd",
        "BLOCK": "#f8d7da",
    }

    def __init__(self):
        super().__init__()
        self.title("VoltGuard — Physics-Aware ICS/SCADA Dashboard (Live)")
        self.geometry("980x600")
        self.configure(bg="#1e1e2e")

        self.events = []
        self.counts = {"ALLOW": 0, "ALERT": 0, "BLOCK": 0}

        self.monitoring = False
        self._stop_event = threading.Event()
        self._monitor_thread = None
        self._blink_state = False

        # rolling throughput tracking
        self._recent_timestamps = []

        self._build_ui()
        self._blink_live_dot()

    # ---------------- UI ----------------
    def _build_ui(self):
        top = tk.Frame(self, bg="#1e1e2e", pady=10)
        top.pack(fill="x", padx=10)

        tk.Label(
            top, text="VoltGuard Dashboard", bg="#1e1e2e", fg="white",
            font=("Segoe UI", 16, "bold")
        ).pack(side="left")

        self.live_dot = tk.Label(
            top, text="● OFFLINE", bg="#1e1e2e", fg="#888888",
            font=("Segoe UI", 11, "bold")
        )
        self.live_dot.pack(side="left", padx=20)

        tk.Label(top, text="Rate (pkt/sec):", bg="#1e1e2e", fg="white").pack(side="left", padx=(20, 5))
        self.rate_var = tk.StringVar(value="2")
        tk.Entry(top, textvariable=self.rate_var, width=5).pack(side="left")

        self.start_btn = tk.Button(
            top, text="▶ Start Monitoring", command=self.toggle_monitoring,
            bg="#4caf50", fg="white", relief="flat", padx=12, pady=4
        )
        self.start_btn.pack(side="left", padx=15)

        tk.Button(
            top, text="⤓ Export Log", command=self.export_log,
            bg="#2196f3", fg="white", relief="flat", padx=10, pady=4
        ).pack(side="left")

        tk.Button(
            top, text="Clear", command=self.clear_table,
            bg="#607d8b", fg="white", relief="flat", padx=10, pady=4
        ).pack(side="left", padx=8)

        columns = ("time", "packet_id", "rpm", "pressure", "flow_rate", "verdict", "action")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=20)
        headings = {
            "time": "Time", "packet_id": "Packet ID", "rpm": "RPM", "pressure": "Pressure",
            "flow_rate": "Flow Rate", "verdict": "Verdict", "action": "Action",
        }
        widths = {"time": 90, "packet_id": 90}
        for col in columns:
            self.tree.heading(col, text=headings[col])
            self.tree.column(col, width=widths.get(col, 120), anchor="center")

        self.tree.tag_configure("ALLOW", background=self.ACTION_COLORS["ALLOW"])
        self.tree.tag_configure("ALERT", background=self.ACTION_COLORS["ALERT"])
        self.tree.tag_configure("BLOCK", background=self.ACTION_COLORS["BLOCK"])

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        bottom = tk.Frame(self, bg="#1e1e2e", pady=8)
        bottom.pack(fill="x", padx=10)

        self.summary_label = tk.Label(
            bottom, text="Total: 0   |   ALLOW: 0   ALERT: 0   BLOCK: 0   |   Throughput: 0.0/sec",
            bg="#1e1e2e", fg="white", font=("Segoe UI", 11)
        )
        self.summary_label.pack(side="left")

    def _blink_live_dot(self):
        """Pulse the LIVE indicator while monitoring is active."""
        if self.monitoring:
            self._blink_state = not self._blink_state
            color = "#4caf50" if self._blink_state else "#1e3a1e"
            self.live_dot.config(text="● LIVE", fg=color)
        else:
            self.live_dot.config(text="● OFFLINE", fg="#888888")
        self.after(500, self._blink_live_dot)

    # ---------------- Monitoring control ----------------
    def toggle_monitoring(self):
        if self.monitoring:
            self._stop_monitoring()
        else:
            self._start_monitoring()

    def _start_monitoring(self):
        try:
            rate = float(self.rate_var.get())
            if rate <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid rate", "Enter a positive number for packets/sec.")
            return

        self.monitoring = True
        self.start_btn.config(text="■ Stop Monitoring", bg="#e53935")
        self._stop_event.clear()
        self._monitor_thread = threading.Thread(
            target=self._monitor_loop, args=(rate,), daemon=True
        )
        self._monitor_thread.start()

    def _stop_monitoring(self):
        self.monitoring = False
        self._stop_event.set()
        self.start_btn.config(text="▶ Start Monitoring", bg="#4caf50")

    def _monitor_loop(self, rate):
        """Runs on a background thread: generates + processes one
        packet at a time at the requested rate, forever, until stopped."""
        interval = 1.0 / rate
        while not self._stop_event.is_set():
            raw_packet = generate_packet()
            try:
                command = parse_packet(raw_packet)
            except PacketParseError:
                result = {
                    "packet_id": raw_packet.get("packet_id"),
                    "command": raw_packet,
                    "verdict": "INVALID",
                    "action": "BLOCK",
                }
            else:
                result = evaluate_command(command, process_command)

            self.after(0, self._on_new_event, result)
            time.sleep(interval)

    # ---------------- Event handling ----------------
    def _on_new_event(self, result):
        now = datetime.now()
        result = {**result, "_ts": now.isoformat()}
        self.events.append(result)
        self.counts[result["action"]] += 1
        self._recent_timestamps.append(now)
        # keep only the last 5 seconds for a live throughput estimate
        cutoff = now.timestamp() - 5
        self._recent_timestamps = [t for t in self._recent_timestamps if t.timestamp() >= cutoff]

        self._add_row(result, now)
        self._trim_table()
        self._update_summary()

    def _add_row(self, result, now):
        cmd = result["command"]
        item = self.tree.insert(
            "", "end",
            values=(
                now.strftime("%H:%M:%S"),
                result["packet_id"],
                cmd.get("rpm", "-"),
                cmd.get("pressure", "-"),
                cmd.get("flow_rate", "-"),
                result["verdict"],
                result["action"],
            ),
            tags=(result["action"],),
        )
        self.tree.see(item)  # auto-scroll to newest

    def _trim_table(self):
        children = self.tree.get_children()
        if len(children) > MAX_ROWS:
            for item in children[: len(children) - MAX_ROWS]:
                self.tree.delete(item)

    def _update_summary(self):
        total = len(self.events)
        throughput = len(self._recent_timestamps) / 5.0
        self.summary_label.config(
            text=(
                f"Total: {total}   |   "
                f"ALLOW: {self.counts['ALLOW']}   "
                f"ALERT: {self.counts['ALERT']}   "
                f"BLOCK: {self.counts['BLOCK']}   |   "
                f"Throughput: {throughput:.1f}/sec"
            )
        )

    def clear_table(self):
        self.tree.delete(*self.tree.get_children())
        self.events = []
        self.counts = {"ALLOW": 0, "ALERT": 0, "BLOCK": 0}
        self._recent_timestamps = []
        self._update_summary()

    def export_log(self):
        if not self.events:
            messagebox.showinfo("Nothing to export", "No events captured yet.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")],
            initialfile="session_log.json",
        )
        if not path:
            return
        import json
        with open(path, "w") as f:
            json.dump(self.events, f, indent=2)
        messagebox.showinfo("Exported", f"Session log saved to:\n{path}")

    def on_close(self):
        self._stop_event.set()
        self.destroy()


if __name__ == "__main__":
    app = VoltGuardDashboard()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
