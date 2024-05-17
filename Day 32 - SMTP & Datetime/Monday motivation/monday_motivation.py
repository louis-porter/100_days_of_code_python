import pandas as pd
import datetime as dt
import smtplib
import random

my_email = "louis.porter26@gmail.com"
password = "qnfb hbvr votm ewaq"

data = pd.read_csv(r"Day 32 - SMTP & Datetime\quotes.txt", sep="\t", header=None)
quotes = data[0].tolist()
random_quote = random.choice(quotes)

now = dt.datetime.now()
day_of_week = now.weekday()



if day_of_week == 0:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="louis.porter12@hotmail.co.uk", 
                      msg=f"Subject:Monday Motivation\n\n{random_quote}") 