import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)  # <Response [200]>  

#1XX: Hold Up
#2XX: Here you go
#3XX: Go Away
#4XX: You Screwed Up
#5XX: I Screwed Up

print(response.status_code) 

response.raise_for_status()

data = response.json()

print(data["iss_position"])