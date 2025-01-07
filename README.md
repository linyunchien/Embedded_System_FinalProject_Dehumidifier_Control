# 伺服馬達與濕度控制系統

[English](README_EN.md) | [繁體中文](README.md)
## 概述

本專案結合 Arduino 和 PyQt5 應用程式，實現透過濕度感測器監測環境並控制伺服馬達操作除濕機。系統提供手動與自動模式切換。

## 功能

1. **手動伺服控制**：透過 GUI 按鈕觸發伺服馬達動作。
2. **自動除濕控制**：當濕度超過指定門檻值時，自動觸發伺服馬達操作。
3. **濕度監測**：在 GUI 中即時顯示當前環境濕度。

## 硬體需求

- Arduino 開發板（如 Uno）
- 伺服馬達
- DHT11 或 DHT22 濕度與溫度感測器
- 用於 Arduino 連接電腦的 USB 線
- 配有 Python 的電腦

## 軟體需求

1. **Python 套件**：

   - PyQt5
   - pyserial

   使用以下指令安裝：

   ```bash
   pip install PyQt5 pyserial
   ```

2. **Arduino 套件**：

   - Adafruit 提供的 DHT 感測器庫

   可在 Arduino IDE 的庫管理員中安裝。

## 設定步驟

### Arduino

1. 將伺服馬達的訊號腳接到 Arduino 的 9 號腳位。
2. 將 DHT 感測器的數據腳接到 Arduino 的 2 號腳位。
3. 將專案提供的 Arduino 程式碼上傳至 Arduino。

### Python 應用程式

1. 確保 Arduino 已連接至電腦，並記錄其 COM 埠（如 `COM3`）。
2. 更新 Python 程式碼中的 COM 埠設定，使其與 Arduino 相符。
3. 執行 Python 腳本：
   ```bash
   python servo_control.py
   ```

## 使用說明

1. **手動模式**：
   - 點擊 GUI 中的 "Press Servo (Manual)" 按鈕手動觸發伺服馬達動作。
2. **自動模式**：
   - 勾選 "Automatic Dehumidifier Control" 啟用自動模式。
   - 當濕度超過 60% 時，伺服馬達會自動觸發動作，並在濕度降低後重置狀態。
3. **濕度監測**：
   - GUI 中會即時顯示當前濕度。

## 問題排查

1. **濕度無法顯示**：

   - 確認 DHT 感測器接線無誤。
   - 確保 Arduino 正常運行，並且連接的 COM 埠正確。

2. **伺服馬達無反應**：

   - 檢查伺服馬達接線是否正確。
   - 確認 Arduino 程式中的伺服馬達腳位設定與硬體一致。

3. **接收到無效數據**：

   - 確保 Arduino 程式中使用的感測器類型（DHT11 或 DHT22）與硬體一致。
   - 檢查接線是否牢固。

## 自定義

- 可在 Arduino 程式碼中修改 `thresholdHumidity` 變數以改變濕度門檻值。
- 如需調整 GUI 布局或新增功能，可修改 Python 程式碼。

