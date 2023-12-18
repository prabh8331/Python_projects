import requests
import os

class PassApp:
    #PassApp api
    def __init__(self) -> None:
        self.user_name = os.environ.get("mypassappuser")
        self.user_code = os.environ.get("mypassappcode")
        self.timeout = 10
        self.pass_app_url = os.environ.get("mypassappurl")
        self.get_data_url = self.pass_app_url + "get_data"
        self.response = requests.get(self.get_data_url, auth=(self.user_name, self.user_code), timeout=self.timeout)
        self.pass_data = self.response.json()

    def get_data(self,user,app):
        """returns password"""
        return self.pass_data[user][app]
