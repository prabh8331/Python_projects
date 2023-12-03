import requests
from datetime import datetime, timedelta

import pytz


##### API request to iss current location api

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(response)  # <Response [200]>  

#1XX: Hold Up
#2XX: Here you go
#3XX: Go Away
#4XX: You Screwed Up
#5XX: I Screwed Up

# print(response.status_code) 

#Error and Exception : if there is any issue in requet then follwoing 
response.raise_for_status()

data = response.json()

##Extract Iss positions
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

# iss_longitude = 70
# iss_latitude = 22

#My position
my_latitude = 18.5894739
my_longitude = 74.0105505


#Check if ISS position is within +5 or -5 degrees of my position to verify if ISS is present to my visible sky
def iss_in_sky():
    if (my_latitude+5 >= iss_latitude and my_latitude-5 <= iss_latitude) and (my_longitude+5 >= iss_longitude and my_longitude-5 <= iss_longitude):
        return True
    else:
        return False

def is_iss_overhead():
    if (my_latitude-5 <= iss_latitude <= my_latitude+5) and ( my_longitude-5 <= iss_longitude <= my_longitude+5):
        return True
    else:
        return False
##### API request to sunrise-sunset.org

parameters = {
    "lat" : my_latitude, 
    "lng" : my_longitude, 
    "formatted" : 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

#putting paramaters in URL   ?p1=val&p2=val
# response = requests.get(url="https://api.sunrise-sunset.org/json?lat=18.5894739&lng74.0105505&tzId=Asia/Kolkata", params=parameters)


response.raise_for_status()

data = response.json()

timezone_utc = pytz.timezone('UTC') 
timezone_ist = pytz.timezone('Asia/Kolkata')


sunset =  datetime.fromisoformat(data["results"]["sunset"]).replace(tzinfo=timezone_utc).astimezone(timezone_ist)
sunrise =  datetime.fromisoformat(data["results"]["sunrise"]).replace(tzinfo=timezone_utc).astimezone(timezone_ist) + timedelta(days=1)


time_now = datetime.now(timezone_ist)
# time_now = time_now.astimezone(timezone_ist)


def is_night():
    if time_now > sunset and time_now < sunrise:
        return True
    else:
        return False
    

import smtplib

my_email = "prabh8331@gmail.com"

try :
    with open("C:/Users/prabh/OneDrive/Desktop/google_app_pass.txt") as login:
        password=login.readlines()[1].strip()
except FileNotFoundError:
    with open("/home/coder/project/google_app_pass.txt") as login:
        password=login.readlines()[1].strip()

if is_iss_overhead() and is_night():

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        
        body="Hello Prabh, Look up in the sky ISS is passing through. Enjoy this Space event."
        
        connection.sendmail(from_addr=my_email, 
                        to_addrs="prabh8221@gmail.com", 
                        msg=f"Subject:International Space Station\n\n{body}")
    
    with open("Python100daycode/Day33/signal",mode="w") as file:
        file.write("day")

else:
    with open("Python100daycode/Day33/signal",mode="w") as file:
        file.write("minute")

