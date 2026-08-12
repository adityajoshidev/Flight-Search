import requests
class DataManager():
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        sheety_headers={
            "Authorization": ""
        }
        self.sheety_endpoint="https://api.sheety.co/4e73b166c858db56bb9480a152563992/flightDeals/prices"
        r=requests.get(self.sheety_endpoint,headers=sheety_headers)
        r.raise_for_status()
        self.data=r.json()