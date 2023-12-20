from datetime import datetime

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,data):
        self.local_departure = self.date_format(data["data"][0]["local_departure"])
        self.local_arrival = self.date_format(data["data"][0]["local_arrival"])
        self.price = data["data"][0]["price"]
        self.duration = self.seconds_to_hh_mm(data["data"][0]["duration"]["total"])

    def seconds_to_hh_mm(self, seconds):
        # Calculate hours and minutes
        hours, remainder = divmod(seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        # Format the result as "hh:mm"
        result = "{:02}:{:02}".format(int(hours), int(minutes))
        return result
    
    def date_format(self, date_string):
        date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
        formatted_date = date_object.strftime('%I:%M %p %d/%b/%y')
        return formatted_date