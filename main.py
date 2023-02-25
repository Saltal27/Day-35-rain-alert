import requests
import smtplib
import os

END_POINT = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = os.environ.get("API_KEY")
my_email = "pythontest32288@gmail.com"
my_password = os.environ.get("EMAIL_PASSWORD")

parameters ={
    "lat": 33.510414,
    "lon": 36.278336,
    "appid": api_key
}

response = requests.get(url=END_POINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data_list = weather_data["list"]

will_rain = False
for _ in weather_data_list[:4]:
    if [_][0]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="omarmobarak53@gmail.com",
            msg="Subject: Rain!\n\nIt's going to rain at some point in the next 12 hours, bring an umbrella"
        )
