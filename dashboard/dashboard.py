import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("VoltGuard Dashboard")
window.resize(400, 300)

layout = QVBoxLayout()

# Title
title = QLabel("VoltGuard Dashboard")
layout.addWidget(title)

# Sensor Values
rpm_label = QLabel("RPM: 5000")
pressure_label = QLabel("Pressure: 80")
flow_label = QLabel("Flow Rate: 500")
status_label = QLabel("Status: SAFE")

layout.addWidget(rpm_label)
layout.addWidget(pressure_label)
layout.addWidget(flow_label)
layout.addWidget(status_label)

# Refresh Button
refresh_button = QPushButton("Refresh")


def refresh_data():
    rpm_label.setText("RPM: 6500")
    pressure_label.setText("Pressure: 95")
    flow_label.setText("Flow Rate: 600")
    status_label.setText("Status: DANGER")


refresh_button.clicked.connect(refresh_data)

layout.addWidget(refresh_button)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())


layout.addWidget(refresh_button)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())