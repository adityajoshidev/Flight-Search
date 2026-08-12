import requests,os
from dotenv import load_dotenv
from datetime import date,timedelta
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,arrival_id):
        load_dotenv()
        flight_endpoint="https://app.100daysofpython.dev/v1/flights/search"
        self.arrival_id=arrival_id
        tomorrow=(date.today()+timedelta(days=1))
        flight_params={
            "engine":"google_flights",
            "api_key":os.getenv("FLIGHTS_API_KEY"),
            "departure_id":"LHR",
            "arrival_id":self.arrival_id,
            "outbound_date":tomorrow.strftime("%Y-%m-%d"),
            "return_date":(tomorrow+timedelta(days=180)).strftime("%Y-%m-%d"),
            "type":1,
        }
        r=requests.get(flight_endpoint,params=flight_params)
        r.raise_for_status()
        self.data=r.json()
