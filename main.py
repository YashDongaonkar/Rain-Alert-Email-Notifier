import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

API_KEY = os.getenv("API_KEY")
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# CITY SELECTION
# weather_params = {
#     "lat":input("Enter latitude of your location > "),
#     "lon":input("Enter longitude of your location > "),
#     "appid":API_KEY,
#     "units":"metric",
#     "cnt":5
# }

weather_params = {
    "lat":21.1458,
    "lon":79.0882,
    "appid":API_KEY,
    "units":"metric",
    "cnt":5
}

response = requests.get(API_ENDPOINT,params=weather_params)
response.raise_for_status()

weather_data = response.json()

city = weather_data["city"]["name"]

print(city)

for hour_data in weather_data["list"]:
    time = hour_data["dt_txt"]
    weather = hour_data["weather"][0]
    id = weather["id"] 
    main = weather["main"]
    desc = weather["description"]
    print(f"At {time},\nForecast:\n{main},{desc}") 

id_list = [item["weather"][0]["id"] for item in weather_data["list"]]

will_rain = False

for id in id_list:
    if id < 600:
        will_rain = True

def send_mail(subject, msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL,password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg = f"Subject:{subject}!\n\n{msg}"
        )
        print("Mail sent...")

if will_rain:
    send_mail(f"Rain Alert in {city}","Rain is expected today, don't forget your umbrella!")
else:
    send_mail(f"No Rain Today In {city}","No need of an umbrella today!")