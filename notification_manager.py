from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
account_sid=os.getenv("TWILIO_SID")
auth_token=os.getenv("TWILIO_AUTH_TOKEN")
MY_EMAIL=os.getenv("YAHOO_EMAIL")
MY_PASSWORD=os.getenv("YAHOO_PASSWORD")
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,flight_data,message):
        '''Input a dictionary containing flight info'''
        # client = Client(account_sid, auth_token)
        # client.messages.create(
        #     body=f"-Low price alert! Only £{flight_data["price"]} to fly from {flight_data["departure_id"]} to {flight_data["arrival_id"]}, on {flight_data["departure_date"]} until {flight_data["arrival_date"]}",
        #     from_=os.getenv("TWILIO_NUMBER"),
        #     to="+917617409508",
        # )
        if message==0:
            message=f"Low price alert! Only GBP {flight_data["price"]} to fly "\
                      f"from {flight_data["departure_id"]} to {flight_data["arrival_id"]}, "\
                      f"with {flight_data["stops"]} stop(s) "\
                      f"departing on {flight_data["departure_date"]} and returning on {flight_data["arrival_date"]}."
        else:
            message=f"-Low price alert! Only GBP{flight_data["price"]} to fly from {flight_data["departure_id"]} to {flight_data["arrival_id"]}, on {flight_data["departure_date"]} until {flight_data["arrival_date"]}"
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", port=465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"From:{MY_EMAIL}\n"
                                    f"To:{MY_EMAIL}\n"
                                    "Subject: Low Price Alert!!\n\n"
                                    f"{message}")