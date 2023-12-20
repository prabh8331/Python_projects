#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search
import flight_data
import notification_manager
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pytz


timezone_ist = pytz.timezone('Asia/Kolkata')
time_now = datetime.now(timezone_ist) 

from_date = (time_now.date()+timedelta(days=1)).strftime("%d/%m/%Y")
to_date = (time_now.date()+relativedelta(months=4)).strftime("%d/%m/%Y")

excel_data = data_manager.DataManager().get_data()

city_all = []
IATA_all = []
local_departure = []
local_arrival = []
price = []
duration = []


user_city = "Pune"
user_IATA = "PNQ"


for city in excel_data["prices"]:
    current_city = city["city"]
    if current_city != user_city:
        city_all.append(current_city)
        if "iataCode" not in city :
            IATA = flight_search.FlightSearch().get_IATA(current_city)
            data_manager.DataManager().put_data(id=city["id"],city=city["city"],iataCode=IATA)
            IATA_all.append(IATA)
        else:
            IATA = city["iataCode"]
            IATA_all.append(city["iataCode"])
        
        data = flight_search.FlightSearch().get_price(fly_from=user_IATA, fly_to=IATA, date_from= from_date,date_to=to_date)

        local_departure.append(flight_data.FlightData(data).local_departure)
        local_arrival.append(flight_data.FlightData(data).local_arrival)
        price.append(flight_data.FlightData(data).price)
        duration.append(flight_data.FlightData(data).duration)

        
subject = "Cheapest Flight in Upcoming 4 Month, Enjoy!!"

to = ["prabh8221@gmail.com"]

mail_body = f"City from: {user_city} \nCity to:"

data = {
    'city': city_all,
    'local_departure' : local_departure,
    'local_arrival' : local_arrival,
    'price' : price,
    'duration' : duration
    }

print(data)

notification_manager.NotificationManager(subject=subject, mail_body=mail_body, data=data, to=to)
