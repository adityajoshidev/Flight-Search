#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData
data_manager=DataManager()
for places in data_manager.data["prices"]:
    print(f"Getting direct flights for {places["city"]}")
    flight_search=FlightSearch(places["iataCode"])
    message=1
    if len(flight_search.data["best_flights"])==0:
        if len(flight_search.data["other_flights"])==0:
            print(f"No direct flight to {places["city"]}. Looking for indirect flights...")
            flight_search=flight_search.search_stopover_flights()
            message=0
    flight_data=FlightData(flight_search.data)
    if flight_data.flight_data["price"]<places["lowestPrice"]:
        user_emails=[user["whatIsYourEmail?"] for user in data_manager.get_customer_emails()]
        notification_manager=NotificationManager(flight_data.flight_data,message)
        data_manager.update_price(places["id"],flight_data.flight_data["price"])
        print("Message sent successfully!")