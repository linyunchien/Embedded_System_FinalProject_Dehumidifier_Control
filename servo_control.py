import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QCheckBox
from PyQt5.QtCore import QTimer
import serial
import time

class ServoControlApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.arduino = serial.Serial('COM3', 9600, timeout=1)  # 確保連接至 Arduino 的 COM 埠
        self.auto_mode = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_humidity)
        self.timer.start(2000)  # 每2秒更新一次濕度
        self.already_pressed = False  # 紀錄是否已按壓

    def initUI(self):
        self.setWindowTitle("Servo Motor and Humidity Control")
        self.setGeometry(100, 100, 400, 300)

        self.humidity_label = QLabel("Current Humidity: --%", self)

        self.manual_button = QPushButton("Press Servo (Manual)", self)
        self.manual_button.clicked.connect(self.press_servo)

        self.auto_checkbox = QCheckBox("Automatic Dehumidifier Control", self)
        self.auto_checkbox.stateChanged.connect(self.toggle_auto_mode)

        layout = QVBoxLayout()
        layout.addWidget(self.humidity_label)
        layout.addWidget(self.manual_button)
        layout.addWidget(self.auto_checkbox)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def press_servo(self):
        if self.arduino.is_open:
            self.arduino.write(b'1')  # 傳送指令至 Arduino
            time.sleep(0.5)  # 等待 Arduino 完成按壓動作

    def toggle_auto_mode(self, state):
        self.auto_mode = state == 2  # 勾選時設為 True

    def update_humidity(self):
        if self.arduino.is_open:
            self.arduino.write(b'R')  # 向 Arduino 要求濕度數據
            time.sleep(0.1)
            if self.arduino.in_waiting > 0:
                humidity_data = self.arduino.readline().decode('utf-8').strip()
                try:
                    humidity = float(humidity_data)
                    self.humidity_label.setText(f"Current Humidity: {humidity}%")

                    if self.auto_mode and humidity > 60:  # 自動模式且濕度超過60%
                        if not self.already_pressed:
                            self.press_servo()
                            self.already_pressed = True  # 確保只按壓一次
                    elif humidity <= 60:
                        self.already_pressed = False  # 濕度低於門檻時重置狀態
                except ValueError:
                    pass

    def closeEvent(self, event):
        if self.arduino.is_open:
            self.arduino.close()  # 關閉序列埠
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServoControlApp()
    window.show()
    sys.exit(app.exec_())
