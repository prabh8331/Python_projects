import requests
import pass_app 

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        
        self.timeout=10
        self.my_email = "prabh8331@gmail.com"
        self.api_sheety = pass_app.PassApp().get_data(user=self.my_email,app="sheety_token")
        
        self.headers_sheety = {
        "Authorization": f"Bearer {self.api_sheety}"
        }
        
        self.sheety_url = "https://api.sheety.co/69ff39b78b52b370199fe9f25bb1ec09/flightDeals/prices"

    def get_data(self):
        # response = requests.get(url=self.sheety_url,headers=self.headers_sheety,timeout=self.timeout)
        data  = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, 
                            {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, 
                            {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, 
                            {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, 
                            {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, 
                            {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, 
                            {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, 
                            {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, 
                            {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
        return data
        # return response.json()
    