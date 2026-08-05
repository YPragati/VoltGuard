import sys
import os
import json

from datetime import datetime


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtCore import Qt, QTimer




# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from physics.physics import process_command

def load_parser_data():

    with open("parser/output.json", "r") as file:
        data = json.load(file)

    registers = data["register_values"]

    return {
        "rpm": registers[0] * 100,
        "pressure": registers[1],
        "flow_rate": 500
    }



from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
    QProgressBar,
    QTextEdit,
    QGroupBox


)

from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("VoltGuard Dashboard")

window.resize(1100,700)

window.setStyleSheet("""
QWidget{
    background:#0F172A;
    color:white;
    font-family:Segoe UI;
    font-size:12pt;
}

QGroupBox{
    border:2px solid #38BDF8;
    border-radius:20px;
    margin-top:20px;
    padding:20px;
    font-weight:bold;
    status_box.setFixedHeight(100)
    sensor_box.setFixedHeight(260)
    health_box.setFixedHeight(90)
    alarm_box.setFixedHeight(90)
    log_box.setFixedHeight(180)
}

QGroupBox:title{
     subcontrol-origin: margin;
    left:15px;
    top:-2px;
    padding:0 8px;
    color:#FACC15;
    font-size:14px;
}

QLineEdit{
    background:white;
    color:black;
    border-radius:6px;
    padding:8px;
}

QPushButton{
    background:#2563EB;
    color:white;
    border-radius:8px;
    padding:10px;
    font-weight:bold;
}

QPushButton:hover{
    background:#1D4ED8;
}

QTextEdit{
    background:#1E293B;
    color:#22C55E;
}

QProgressBar{
    text-align:center;
    color:white;
    font-weight:bold;
}
""")
main_layout = QVBoxLayout()

title = QLabel("⚡ VoltGuard Industrial Monitoring System")
title.setAlignment(Qt.AlignCenter)
demo_label = QLabel("🔄 DEMO MODE - Automatic Sensor Simulation")
demo_label.setAlignment(Qt.AlignCenter)

demo_label.setStyleSheet("""
font-size:14px;
color:#FACC15;
font-weight:bold;
padding:5px;
""")

main_layout.addWidget(demo_label)

title.setStyleSheet("""
font-size:28px;
font-weight:bold;
color:#38BDF8;
padding:10px;
""")



clock = QLabel()
clock.setAlignment(Qt.AlignRight)
clock.setStyleSheet("""
font-size:14px;
color:#FACC15;
padding-right:10px;
""")

main_layout.addWidget(clock)

main_layout.addWidget(title)

# ============================
# System Overview
# ============================

overview_box = QGroupBox("📌 System Overview")

overview_layout = QVBoxLayout()

overview_text = QLabel(
    
    "Current motor status is continuously monitored using RPM, "
    "pressure, and flow rate sensors.\n""The system automatically "
    "detects SAFE, WARNING, and DANGER conditions."
)


overview_text.setWordWrap(True)

overview_text.setStyleSheet("""
font-size:15px;
color:#E2E8F0;
padding:10px;
font-weight:bold;
""")

overview_layout.addWidget(overview_text)

overview_box.setLayout(overview_layout)
overview_box.setMaximumHeight(150)

main_layout.addWidget(overview_box)




content_layout = QHBoxLayout()

left_layout = QVBoxLayout()
right_layout = QVBoxLayout()


content_layout.addLayout(left_layout,1)
content_layout.addLayout(right_layout,1)

main_layout.addLayout(content_layout)

status_box = QGroupBox("🚦 Machine Status")

status_layout = QVBoxLayout()

status_label = QLabel("⚪ READY")

status_label.setAlignment(Qt.AlignCenter)

status_label.setStyleSheet("""
font-size:28px;
padding:5px;
font-weight:bold;
""")

status_layout.addWidget(status_label)

status_box.setLayout(status_layout)
status_box.setMaximumHeight(120)



# ============================
# Sensor Values
# ============================

sensor_box = QGroupBox("📊 Sensor Values")

sensor_layout = QVBoxLayout()

sensor_layout.addWidget(QLabel("RPM"))

rpm_bar = QProgressBar()
rpm_bar.setMaximum(8000)
sensor_layout.addWidget(rpm_bar)

sensor_layout.addWidget(QLabel("Pressure"))

pressure_bar = QProgressBar()
pressure_bar.setMaximum(200)
sensor_layout.addWidget(pressure_bar)

sensor_layout.addWidget(QLabel("Flow Rate"))

flow_bar = QProgressBar()
flow_bar.setMaximum(1000)
sensor_layout.addWidget(flow_bar)

sensor_box.setLayout(sensor_layout)

right_layout.addWidget(sensor_box,3)

# ============================
# Machine Health
# ============================

health_box = QGroupBox("❤️ Machine Health")

health_layout = QVBoxLayout()

health_layout.setAlignment(Qt.AlignCenter)

health_bar = QProgressBar()
health_bar.setTextVisible(True)
health_bar.setMaximum(100)
health_bar.setValue(100)
health_bar.setFormat("%p%")


health_bar.setFixedHeight(35)

health_bar.setStyleSheet("""
QProgressBar{
    border:2px solid #555;
    border-radius:5px;
    text-align:center;
    color:white;
    font-weight:bold;
}

QProgressBar::chunk{
    background:#22C55E;
}
""")

health_layout.addWidget(health_bar, alignment=Qt.AlignCenter)

health_box.setLayout(health_layout)
health_box.setFixedHeight(100)

right_layout.addWidget(health_box)



alarm_box = QGroupBox("🚨 Alarm Panel")

alarm_layout = QVBoxLayout()

alarm_label = QLabel("No Active Alarm")
alarm_label.setAlignment(Qt.AlignCenter)

alarm_label.setStyleSheet("""
font-size:16px;
font-weight:bold;
color:#22C55E;

""")

alarm_layout.addWidget(alarm_label)

alarm_box.setLayout(alarm_layout)
alarm_box.setMaximumHeight(120)




# ============================
# Event Log
# ============================

log_box = QGroupBox("📋 Event Log")

log_layout = QVBoxLayout()

log = QTextEdit()
log.setReadOnly(True)
log.setMinimumHeight(100)

log_layout.addWidget(log)

log_box.setLayout(log_layout)

right_layout.addWidget(log_box,2)

# ============================
# Live Sensor Graph
# ============================

graph_box = QGroupBox("📈 📈 Real-Time Sensor Graph")


graph_layout = QVBoxLayout()

figure = Figure(figsize=(8, 4), facecolor="#1E293B")

canvas = FigureCanvas(figure)

ax = figure.add_subplot(111)

# Dashboard styling
ax.set_facecolor("#0F172A")
ax.set_title("Live Sensor Trends", color="white", fontsize=14, fontweight="bold")
ax.set_xlabel("Time", color="white")
ax.set_ylabel("Value", color="white")

ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

ax.grid(True, linestyle="--", alpha=0.3)

# Store graph data
rpm_history = []
pressure_history = []
flow_history = []

# Demo Mode Sensor Values
demo_index = 0
graph_layout
demo_values = [
    {
        "rpm": 1000,
        "pressure": 50,
        "flow_rate": 500
    },
    {
        "rpm": 1000,
        "pressure": 10,
        "flow_rate": 500
    },
    {
        "rpm": 7000,
        "pressure": 80,
        "flow_rate": 500
    }
]

graph_layout.addWidget(canvas)

graph_box.setLayout(graph_layout)

left_layout.addWidget(graph_box)





def update_clock():
    clock.setText("🕒 " + datetime.now().strftime("%d %b %Y   %H:%M:%S"))

timer = QTimer()
timer.timeout.connect(update_clock)
timer.start(1000)





update_clock()


def refresh_data():
    try:

       
        global demo_index

        command = demo_values[demo_index]

        demo_index = (demo_index + 1) % len(demo_values)
        

        status = process_command(command)

        # Update progress bars
        rpm_bar.setValue(command["rpm"])
        pressure_bar.setValue(command["pressure"])
        flow_bar.setValue(command["flow_rate"])


        # Store latest values
        rpm_history.append(command["rpm"])
        pressure_history.append(command["pressure"])
        flow_history.append(command["flow_rate"])


        # Keep only last 10 readings
        rpm_history[:] = rpm_history[-10:]
        pressure_history[:] = pressure_history[-10:]
        flow_history[:] = flow_history[-10:]



  # Draw graph
       
        ax.clear()

        # Dark industrial theme
        ax.set_facecolor("#0F172A")

        # Plot sensor trends
        ax.plot(
            rpm_history,
            label="RPM",
            color="#3B82F6",
            linewidth=2.5,
            marker="o",
            markersize=4
        )

        ax.plot(
            pressure_history,
            label="Pressure",
            color="#F59E0B",
            linewidth=2.5,
            marker="s",
            markersize=4
        )

        ax.plot(
            flow_history,
            label="Flow Rate",
            color="#22C55E",
            linewidth=2.5,
            marker="^",
            markersize=4
        )

        # Title
        ax.set_title(
            "Live Sensor Trends",
            fontsize=14,
            fontweight="bold",
            color="white"
        )

        # Axis labels
        ax.set_xlabel("Readings", color="white")
        ax.set_ylabel("Sensor Values", color="white")

        # White axis text
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")

        # Light grid
        ax.grid(True, linestyle="--", alpha=0.3)

        # White border
        for spine in ax.spines.values():
            spine.set_color("white")

        # Legend
        legend = ax.legend(
            loc="upper left",
            facecolor="#1E293B",
            edgecolor="white"
        )

        for text in legend.get_texts():
            text.set_color("white")

        canvas.draw()




        

        # Update status, health and alarm
        if status == "SAFE":
            status_label.setText("🟢 SAFE")
            status_label.setStyleSheet("font-size:32px;font-weight:bold;color:#22C55E;")
            health_bar.setValue(100)
            health_bar.setFormat("Health: 100%")

            alarm_label.setText("✅ No Active Alarm")
            alarm_label.setStyleSheet("color:#22C55E;font-size:18px;font-weight:bold;")

        elif status == "WARNING":
            status_label.setText("🟡 WARNING")
            status_label.setStyleSheet("font-size:32px;font-weight:bold;color:#FACC15;")
            health_bar.setValue(60)
            health_bar.setFormat("Health: 60%")

            alarm_label.setText("⚠ Check Machine")
            alarm_label.setStyleSheet("color:#FACC15;font-size:18px;font-weight:bold;")

        else:
            status_label.setText("🔴 DANGER")
            status_label.setStyleSheet("font-size:32px;font-weight:bold;color:#EF4444;")
            health_bar.setValue(20)
            health_bar.setFormat("Health: 20%")

            alarm_label.setText("🚨 CRITICAL ALERT")
            alarm_label.setStyleSheet("color:#EF4444;font-size:18px;font-weight:bold;")

        # Event Log
        time = datetime.now().strftime("%H:%M:%S")

        if status == "SAFE":
            log.setTextColor(Qt.green)
            log.append(f"[{time}] 🟢 SAFE")

        elif status == "WARNING":
            log.setTextColor(Qt.yellow)
            log.append(f"[{time}] 🟡 WARNING")

        else:
            log.setTextColor(Qt.red)
            log.append(f"[{time}] 🔴 DANGER")

        log.setTextColor(Qt.white)
        log.append(f"RPM: {command['rpm']} | Pressure: {command['pressure']} | Flow: {command['flow_rate']}\n")
        
        
    except Exception as e:
        status_label.setText("❌ Invalid Input")
        log.setTextColor(Qt.red)
        log.append(f"❌ ERROR : {e}")


def reset_data():
    
   

    rpm_bar.setValue(0)
    pressure_bar.setValue(0)
    flow_bar.setValue(0)

    health_bar.setValue(0)

    status_label.setText("⚪ READY")
    status_label.setStyleSheet("font-size:32px;font-weight:bold;color:white;")
    alarm_label.setText("No Active Alarm")
    alarm_label.setStyleSheet("color:#22C55E;font-size:18px;font-weight:bold;")

    rpm_history.clear()
    pressure_history.clear()
    flow_history.clear()

    ax.clear()
    canvas.draw()


    
    log.clear()


#RPM

rpm_bar.setStyleSheet("""
QProgressBar{
    border:2px solid #555;
    border-radius:5px;
    text-align:center;
}
QProgressBar::chunk{
    background-color:#3B82F6;
}
""")


#Pressure

pressure_bar.setStyleSheet("""
QProgressBar{
    border:2px solid #555;
    border-radius:5px;
    text-align:center;
}
QProgressBar::chunk{
    background:#FACC15;
}
""")

#Flow Rate

flow_bar.setStyleSheet("""
QProgressBar{
    border:2px solid #555;
    border-radius:5px;
    text-align:center;
}
QProgressBar::chunk{
    background:#8B5CF6;
}
""")








left_layout.addWidget(status_box)
left_layout.addWidget(alarm_box)

left_layout.addStretch()

footer = QLabel("Developed by Team 03-VoltGuard | Industrial Safety Monitoring System")

footer.setAlignment(Qt.AlignCenter)

footer.setStyleSheet("""
font-size:12px;
color:gray;
padding:10px;
""")

main_layout.addWidget(footer)


















window.setLayout(main_layout)

sensor_timer = QTimer()
sensor_timer.timeout.connect(refresh_data)
sensor_timer.start(5000)


window.setLayout(main_layout)

window.show()

sys.exit(app.exec())

window.show()




sys.exit(app.exec())