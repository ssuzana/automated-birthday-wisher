import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = "smtppython1@gmail.com"
PASSWORD = "pyth0n2021"

now = dt.datetime.now()
today_month = now.month
today_day = now.day

data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")


def write_letter(birthday_person):
    letter_num = random.randint(1, 3)
    letter = open(f'letter_templates/letter_{letter_num}.txt', "r")
    new_letter = letter.read().replace('[NAME]', birthday_person)
    letter.close()
    return new_letter


def send_email(to_email, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject:Happy Birthday!!\n\n{message}")


for item in data_dict:
    if item['month'] == today_month and item['day'] == today_day:
        message = write_letter(item['name'])
        send_email(item['email'], message)
