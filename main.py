import requests
from twilio.rest import Client

LAT = 8.11728
LON = -5.60095
WEATHER_ENDPOINT = "http://api.weatherapi.com/v1/forecast.json"
WILL_IT_RAIN = []
account_sid = "your_sid_acount"
auth_token = "your-sid_auth_code"
parameters = {"key": "your_weather_api_key", "q": {"Accra"}}

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
        from_="contact_to_send_alert",
        to="contact_to_recieve_alert",
    )
    print(message.status)
