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
        response = requests.get(url=self.sheety_url,headers=self.headers_sheety,timeout=self.timeout)
        return response.json()
    
    def put_data(self,id,city,iataCode):
        
        new_entry = {'id': id, 'city': city, 'iataCode': iataCode}
        data_post ={'price': new_entry}
        response = requests.put(url=self.sheety_url+f"/{id}", json=data_post, headers=self.headers_sheety,timeout=10)
    