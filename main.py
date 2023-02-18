import requests
from twilio.rest import Client

LAT = 8.11728
LON = -5.60095
WEATHER_ENDPOINT = "http://api.weatherapi.com/v1/forecast.json"
WILL_IT_RAIN = []
account_sid = "AC32bfbbb6f5c1a52b3e4b2e422e6092a1"
auth_token = "a034f796bf57d81e218a02c2f3013d3a"
parameters = {"key": "7d86e1f3f28b4f98aa8141406231102", "q": {"Accra"}}

response = requests.get(WEATHER_ENDPOINT, params=parameters)

weather_data = response.json()
weather_slice = weather_data["forecast"]["forecastday"][0]["hour"][:12]

for i in range(0, 12):
    x = str(
        weather_slice[i]["will_it_rain"]
    )  # output will be 1 if it'll and 0 if it'll not
    WILL_IT_RAIN.extend(x)

# check if it'll rain
if "1" in WILL_IT_RAIN:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+17407167716",
        to="+233268125555",
    )
    print(message.status)
