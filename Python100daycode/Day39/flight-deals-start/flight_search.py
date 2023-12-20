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
        """Gets the IATA code for provided city"""
        
        parameters = {
            "term" : city
        }
        
        response = requests.get(self.location_endpoint, params=parameters, headers=self.headers, timeout=10)
        data = response.json()
        if data["locations"][0]["code"] is None:
            return data["locations"][1]["code"]
        else:
            return data["locations"][0]["code"]


    def get_price(self, fly_from, fly_to, date_from, date_to):
        """Get price"""
        parameters = {
            "fly_from" : fly_from,
            "fly_to" : fly_to,
            "date_from" : date_from,
            "date_to" : date_to,
            "limit" : 2,
            "sort" : "price",
            "curr": "INR",
            "partner_market" : "in"
        }

        response = requests.get(self.search_endpoint, params=parameters, headers=self.headers, timeout=10)
        return response.json()
