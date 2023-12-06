import os
import requests
from twilio.rest import Client

# account_sid = 'fjadsoifjasdfapofajoi23dsf'
# auth_token = 'gaopfrkgpdsfakg[adfg[sodfijgs]]'

### using enironment variables to access the tocken

account_sid= os.environ.get("twillio_account_sid")
auth_token = os.environ.get("twillio_auth_token")

client = Client(account_sid, auth_token)

# api_key = "afdigaiuhdfgaisdjfasdfnjasdhfash"
api_key = os.environ.get("OWM_api_key")

# Chalange--> 5 day weater forcast, they will give 3 Hour Intervals forcast and in total gives 8 forcast a day

my_latitude = 18.5894739
my_longitude = 74.0105505

paramaters = {
    "lat" : my_latitude,
    "lon" : my_longitude,
    "appid" : api_key,
    "cnt" : 8
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=paramaters)

response.raise_for_status()

# https://api.openweathermap.org/data/2.5/weather?q=pune,in&appid=cc95b453660165819ed332091d5cbcb2

data = response.json()

# len(data["list"])
# len(data["list"][0]["weather"])

forcast_weater_code  = []
will_rain = False

for i in range(0, len(data["list"])):
    for j in range(0, len(data["list"][i]["weather"])):
        # forcast_weater_code.append(data["list"][i]["weather"][j]["id"])
        if data["list"][i]["weather"][j]["id"] < 700:
            will_rain = True
            

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("bring umbrella")
    message = client.messages.create(
            from_='+18589432257',
            body='Hello, Bring umbrella, Its going to rain',
            to=os.environ.get("my_phone_no")
            )

print(message.sid)
print(message.status)
