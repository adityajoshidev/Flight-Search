#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData
data_manager=DataManager()
for places in data_manager.data["prices"]:
    flight_search=FlightSearch(places["iataCode"])
    flight_data=FlightData(flight_search.data)
    if flight_data.flight_data["price"]<places["lowestPrice"]:
        notification_manager=NotificationManager(flight_data.flight_data)
        print("Message sent successfully!")