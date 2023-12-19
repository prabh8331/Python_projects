#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager

excel_data = data_manager.DataManager().get_data()

for city in excel_data["prices"]:
    print(city["city"])
