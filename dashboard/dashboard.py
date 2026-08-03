import sys
import os

from datetime import datetime
from PyQt5.QtCore import Qt, QTimer




# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from physics.physics import process_command

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
}
""")
main_layout = QVBoxLayout()

title = QLabel("⚡ VoltGuard Industrial Monitoring System")
title.setAlignment(Qt.AlignCenter)

title.setStyleSheet("""
font-size:28px;
font-weight:bold;
color:#38BDF8;
padding:10px;
""")


logo = QLabel("🛡️ VOLTGUARD")
logo.setAlignment(Qt.AlignCenter)

logo.setStyleSheet("""
font-size:20px;
font-weight:bold;
color:#22C55E;
padding:5px;
""")

main_layout.addWidget(logo)

clock = QLabel()
clock.setAlignment(Qt.AlignRight)
clock.setStyleSheet("""
font-size:14px;
color:#FACC15;
padding-right:10px;
""")

main_layout.addWidget(clock)

main_layout.addWidget(title)

content_layout = QHBoxLayout()

left_layout = QVBoxLayout()
right_layout = QVBoxLayout()
# ============================
# Machine Parameters
# ============================

parameter_box = QGroupBox("⚙ Machine Parameters")

parameter_layout = QGridLayout()

parameter_layout.setVerticalSpacing(8)
parameter_layout.setHorizontalSpacing(12)
parameter_layout.setContentsMargins(15, 20, 15, 15)

rpm_input = QLineEdit()
rpm_input.setPlaceholderText("Enter RPM")

pressure_input = QLineEdit()
pressure_input.setPlaceholderText("Enter Pressure")

flow_input = QLineEdit()
flow_input.setPlaceholderText("Enter Flow Rate")

parameter_layout.addWidget(QLabel("RPM"),0,0)
parameter_layout.addWidget(rpm_input,0,1)

parameter_layout.addWidget(QLabel("Pressure"),1,0)
parameter_layout.addWidget(pressure_input,1,1)

parameter_layout.addWidget(QLabel("Flow Rate"),2,0)
parameter_layout.addWidget(flow_input,2,1)

parameter_box.setLayout(parameter_layout)

left_layout.addWidget(parameter_box)

button_layout = QHBoxLayout()

check_button = QPushButton("✔ Check Status")
reset_button = QPushButton("🔄 Reset")

button_layout.addWidget(check_button)
button_layout.addWidget(reset_button)

left_layout.addLayout(button_layout)

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

health_bar = QProgressBar()
health_bar.setMaximum(100)
health_bar.setValue(100)

health_layout.addWidget(health_bar)

health_box.setLayout(health_layout)
health_box.setMaximumHeight(120)
health_bar.setFixedHeight(35)

right_layout.addWidget(health_box,1)


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


def update_clock():
    clock.setText("🕒 " + datetime.now().strftime("%d %b %Y   %H:%M:%S"))

timer = QTimer()
timer.timeout.connect(update_clock)
timer.start(1000)

update_clock()


def refresh_data():
    try:

        command = {
            "rpm": int(rpm_input.text()),
            "pressure": int(pressure_input.text()),
            "flow_rate": int(flow_input.text())
        }

        status = process_command(command)

        # Update progress bars
        rpm_bar.setValue(command["rpm"])
        pressure_bar.setValue(command["pressure"])
        flow_bar.setValue(command["flow_rate"])

        # Update sensor values
        rpm_value.setText(f"RPM : {command['rpm']}")
        pressure_value.setText(f"Pressure : {command['pressure']}")
        flow_value.setText(f"Flow Rate : {command['flow_rate']}")

        # Update status, health and alarm
        if status == "SAFE":
            status_label.setText("🟢 SAFE")
            status_label.setStyleSheet("font-size:32px;font-weight:bold;color:#22C55E;")
            health_bar.setValue(100)

            alarm_label.setText("✅ No Active Alarm")
            alarm_label.setStyleSheet("color:#22C55E;font-size:18px;font-weight:bold;")

        elif status == "WARNING":
            status_label.setText("🟡 WARNING")
            status_label.setStyleSheet("font-size:32px;font-weight:bold;color:#FACC15;")
            health_bar.setValue(60)

            alarm_label.setText("⚠ Check Machine")
            alarm_label.setStyleSheet("color:#FACC15;font-size:18px;font-weight:bold;")

        else:
            status_label.setText("🔴 DANGER")
            status_label.setStyleSheet("font-size:32px;font-weight:bold;color:#EF4444;")
            health_bar.setValue(20)

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
    rpm_input.clear()
    pressure_input.clear()
    flow_input.clear()

    rpm_bar.setValue(0)
    pressure_bar.setValue(0)
    flow_bar.setValue(0)

    health_bar.setValue(100)

    status_label.setText("⚪ READY")
    status_label.setStyleSheet("font-size:32px;font-weight:bold;color:white;")

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

rpm_value = QLabel("RPM : 0")
pressure_value = QLabel("Pressure : 0")
flow_value = QLabel("Flow Rate : 0")

sensor_layout.addWidget(rpm_value)
sensor_layout.addWidget(pressure_value)
sensor_layout.addWidget(flow_value)




check_button.clicked.connect(refresh_data)
reset_button.clicked.connect(reset_data)

left_layout.addWidget(status_box)
left_layout.addWidget(alarm_box)

left_layout.addStretch()

footer = QLabel("Developed by Team VoltGuard | Industrial Safety Monitoring System")

footer.setAlignment(Qt.AlignCenter)

footer.setStyleSheet("""
font-size:12px;
color:gray;
padding:10px;
""")

main_layout.addWidget(footer)


















window.setLayout(main_layout)

window.show()

sys.exit(app.exec())