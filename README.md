# ☔️ Rain Alert Email Notifier

A Python script that fetches upcoming weather data using the OpenWeatherMap API and sends an email alert if rain is expected.

---

## 📄 Description

This lightweight Python utility helps you stay prepared for the weather. It pulls 5 weather forecasts spaced over a few hours for a specified location and sends you a personalized email if there's a chance of rain.

---

## ⚙️ Features

* ✉️ Sends an email alert if rain is likely
* ☔️ Checks weather codes from the OpenWeatherMap API
* 📈 Provides a concise summary of forecast data in console
* 📊 Configurable for any city via latitude and longitude
* ⚒️ Supports both hardcoded and input-based configuration

---

## 💡 How It Works

* Retrieves hourly forecast data using the OpenWeatherMap API
* Scans weather condition codes to detect rain (<600)
* If rain is likely: sends an "umbrella needed" email
* If not: sends an "umbrella not needed" email

---

## 🛠️ Tech Stack

* Python 3.x
* OpenWeatherMap API
* `requests`
* `smtplib`

---
![image](https://github.com/user-attachments/assets/7407d8f9-d137-4b11-82b2-16b3eb03e7c5)

![image](https://github.com/user-attachments/assets/b5ab9e1e-aade-4f73-81bb-490669316609)

