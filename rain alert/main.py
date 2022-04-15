import requests
from twilio.rest import Client

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = 'YOUR_OPEN_WEATHER_MAP_API_KEY'

account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

weather_params = {
    'lat': 6.524379,
    'lon': 3.379206,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="YOUR_TWILIO_NUMBER",
        to="YOU_VERIFIED_NUMBER"
    )
