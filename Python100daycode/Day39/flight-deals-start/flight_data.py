class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,data):
        self.local_departure = data["data"][0]["local_departure"]
        self.local_arrival = data["data"][0]["local_arrival"]
        self.price = data["data"][0]["price"]
        self.duration = data["data"][0]["duration"]

