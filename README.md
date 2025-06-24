# ☔️ Rain Alert Email Notifier

A Python script that fetches upcoming weather data using the OpenWeatherMap API and sends an email alert if rain is expected.

---

## 📄 Description

This lightweight Python utility helps you stay prepared for the weather. It pulls the next few hours of weather forecasts for a specified location and sends you a personalized email if there's a chance of rain.

---

## ⚙️ Features

* ✉️ Sends an email alert if rain is likely
* ☔️ Checks weather codes from the OpenWeatherMap 5-day/3-hour forecast
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
* [OpenWeatherMap API](https://openweathermap.org/forecast5)
* `requests`
* `smtplib`

---

![image](https://github.com/user-attachments/assets/e442d162-4683-414d-94ba-df00c81c5a58)

![image](https://github.com/user-attachments/assets/0327e8db-5696-41f3-9daa-5317468e9157)

