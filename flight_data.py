class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,data):
        flight_data = data["best_flights"][0]
        self.flight_data = {
            "price": flight_data["price"],
            "departure_id": flight_data["flights"][0]["departure_airport"]["id"],
            "departure_date": flight_data["flights"][0]["departure_airport"]["time"].split(" ")[0],
            "arrival_id": flight_data["flights"][0]["arrival_airport"]["id"],
            "arrival_date": flight_data["flights"][0]["arrival_airport"]["time"].split(" ")[0],
            "stops":len(flight_data["flights"])
        }