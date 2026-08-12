from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
account_sid=os.getenv("TWILIO_SID")
auth_token=os.getenv("TWILIO_AUTH_TOKEN")
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,flight_data):
        '''Input a dictionary containing flight info'''
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=f"-Low price alert! Only £{flight_data["price"]} to fly from {flight_data["departure_id"]} to {flight_data["arrival_id"]}, on {flight_data["departure_date"]} until {flight_data["arrival_date"]}",
            from_=os.getenv("TWILIO_NUMBER"),
            to="+917617409508",
        )