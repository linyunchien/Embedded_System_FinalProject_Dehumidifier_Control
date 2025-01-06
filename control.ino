#include <Servo.h>
#include <DHT.h>

#define DHTPIN 2 // DHT感測器的腳位
#define DHTTYPE DHT11 // 感測器型號

Servo myServo; // 宣告 Servo 馬達
DHT dht(DHTPIN, DHTTYPE);

int servoPin = 9; // Servo 連接至 Arduino 的腳位
int thresholdHumidity = 60; // 濕度門檻值

void setup() {
  Serial.begin(9600); // 初始化序列通訊
  myServo.attach(servoPin); // 設定 Servo 的腳位
  myServo.write(90); // 初始位置
  dht.begin(); // 啟動DHT感測器
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // 接收來自 PyQt 的指令

    if (command == '1') { // 按壓動作
      pressDehumidifier();
    } else if (command == 'R') { // 傳回濕度數據
      float humidity = dht.readHumidity();
      if (!isnan(humidity)) {
        Serial.println(humidity); // 傳回濕度至 PyQt
      } else {
        Serial.println("Error");
      }
    }
  }

  delay(100); // 簡單的執行間隔
}

void pressDehumidifier() {
  myServo.write(0); // 移動到按壓角度
  delay(500); // 保持按壓
  myServo.write(90); // 返回初始位置
}
