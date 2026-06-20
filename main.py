import pandas as pd
import smtplib
from email.message import EmailMessage
import datetime as dt
from dotenv import load_dotenv
from os import getenv

load_dotenv("secrets.env")
#---------------Extracting month and day--------------#
now = dt.datetime.now()
month = now.month
day = now.day

#------------Setting up the birthday wish--------------#
birthdays = pd.read_csv("birthdays.csv")

gmail_email = getenv("GMAIL_EMAIL")
gmail_password = getenv("GMAIL_PASSWORD")
email_receiver = getenv("EMAIL_RECIEVER")

message = EmailMessage()
message['Subject'] = "Happy Birthday!"
message['From'] = gmail_email
message['To'] = email_receiver

with open("letter_1.txt", mode='r') as letter:
    name = str(birthdays.iat[0, 0])
    email_letter = letter.read().replace("[NAME]", name)
    message.set_content(email_letter)
    
#----Sending the birthday wish at the day of the bday---#  
num_month = birthdays[birthdays['name'] == 'John']['month'].values.item()
num_day = birthdays[birthdays['name'] == 'John']['day'].values.item()

# if month == num_month and day == num_day:
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(gmail_email, gmail_password)
        connection.send_message(message)
except Exception:
    print("Failed to send email.")
else:
    print("Email sent!")
# else:
#     print("It's not their birthday today :(")
