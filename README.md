# Rain-alert
 This code uses the WeatherAPI to check if it will rain today in a specified location
Introduction

This Python code uses the WeatherAPI to check if it will rain today in a specified location (Accra - Ghana is used in this instance). If it will rain, the code sends a text message to the phone number specified in the to field using Twilio API.
Libraries

    requests - This library allows the code to send HTTP requests to the WeatherAPI to obtain weather data.
    twilio.rest.Client - This library allows the code to send text messages using the Twilio API.

Variables

    LAT - A float representing the latitude of the location for which the weather forecast is being checked.
    LON - A float representing the longitude of the location for which the weather forecast is being checked.
    WEATHER_ENDPOINT - A string representing the base URL of the WeatherAPI.
    WILL_IT_RAIN - An empty list that will store whether it will rain or not for the next 12 hours.
    account_sid - A string representing the account SID for the Twilio API.
    auth_token - A string representing the authentication token for the Twilio API.
    parameters - A dictionary containing the query parameters that will be sent to the WeatherAPI to obtain the weather forecast.

Code

    The code sends an HTTP GET request to the WeatherAPI endpoint using the requests library.
    The response from the endpoint is converted into a Python dictionary using the .json() method and stored in the weather_data variable.
    The first 12 hours of the weather forecast data are extracted from the weather_data variable and stored in the weather_slice variable.
    The code loops through the weather_slice variable and extracts the will_it_rain data for each hour. The extracted data is then added to the WILL_IT_RAIN list.
    The code checks if the value 1 exists in the WILL_IT_RAIN list.
    If 1 exists in the WILL_IT_RAIN list, the code uses the twilio library to send a text message to the phone number specified in the to field. The body field contains the message to be sent, while the from_ field represents the Twilio phone number sending the message.
    The status of the text message is printed to the console.