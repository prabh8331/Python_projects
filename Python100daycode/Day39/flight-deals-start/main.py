import pass_app 
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests

passapp = pass_app.PassApp()

my_email = "prabh8331@gmail.com"

tequila_flight_api=passapp.get_data(user=my_email,app="tequila_flight_api")

location_endpoint = "https://api.tequila.kiwi.com/locations/query"

paramaters = {
    "term" : "Pune"
}

headers = {
    "apikey" : tequila_flight_api
}

response = requests.get(location_endpoint, params=paramaters, headers=headers, timeout=10)
data = response.json()
print(data["locations"][0]["code"])

paramaters = {
    "term" : "amritsar"
}
response = requests.get(location_endpoint, params=paramaters, headers=headers, timeout=10)
data = response.json()
print(data["locations"][0]["code"])

search_endpoint = "https://api.tequila.kiwi.com/v2/search"

paramaters = {
    "fly_from" : "ATQ",
    "fly_to" : "PNQ",
    "date_from" : "21/12/2023",
    "date_to" : "20/01/2024",
    "limit" : 2,
    "sort" : "price",
    "curr": "INR",
    "partner_market" : "in"
}

response = requests.get(search_endpoint, params=paramaters, headers=headers, timeout=10)
data = response.json()
print(data)