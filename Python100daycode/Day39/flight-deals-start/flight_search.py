import pass_app 
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.my_email = "prabh8331@gmail.com"
        
        self.tequila_flight_api=pass_app.PassApp().get_data(user=self.my_email,app="tequila_flight_api")
        
        self.location_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        
        self.headers = {
            "apikey" : self.tequila_flight_api
        }

    def get_IATA(self,city):
        """Gets the data"""
        
        parameters = {
            "term" : city
        }
        
        response = requests.get(self.location_endpoint, params=parameters, headers=self.headers, timeout=10)
        data = response.json()
        return data["locations"][0]["code"]


    def get_price(self, fly_from, fly_to):
        parameters = {
            "fly_from" : fly_from,
            "fly_to" : fly_to,
            "date_from" : "21/12/2023",
            "date_to" : "20/01/2024",
            "limit" : 2,
            "sort" : "price",
            "curr": "INR",
            "partner_market" : "in"
        }

        response = requests.get(self.search_endpoint, params=parameters, headers=self.headers, timeout=10)
        data = response.json()
        print(data["data"][0]["local_departure"])
        print(data["data"][0]["local_arrival"])
        print(data["data"][0]["price"])
        print(data["data"][0]["duration"])