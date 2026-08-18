import requests,os
from dotenv import load_dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.sheety_headers={
            "Authorization":os.getenv("SHEETY_AUTHORIZATION_KEY")
        }
        self.sheety_endpoint="https://api.sheety.co/4e73b166c858db56bb9480a152563992/flightDeals/prices"
        r=requests.get(self.sheety_endpoint,headers=self.sheety_headers)
        r.raise_for_status()
        self.data=r.json()

    def update_price(self,object_id,new_price):
        update_endpoint=f"{self.sheety_endpoint}/{object_id}"
        update_params={
            "price":{
            "lowestPrice":new_price,
            }
        }
        r=requests.put(update_endpoint,json=update_params,headers=self.sheety_headers)
        r.raise_for_status()
    def get_customer_emails(self):
        users_endpoint="https://api.sheety.co/4e73b166c858db56bb9480a152563992/flightDeals/users"
        r=requests.get(users_endpoint,headers=self.sheety_headers)
        r.raise_for_status()
        return r.json()["users"]