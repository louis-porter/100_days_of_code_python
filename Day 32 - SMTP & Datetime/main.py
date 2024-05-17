import smtplib
import pandas as pd
import datetime as dt
import random

data = pd.read_csv(r"Day 32 - SMTP & Datetime\birthdays.csv")
birthdays = data.to_dict(orient="records")
birthdays_dict = {
     (birthdays[0]["month"], birthdays[0]["day"]): birthdays[0]
}


now = dt.datetime.now()
now_month = now.month
now_day = now.day

letters = [r"Day 32 - SMTP & Datetime\letter_templates\letter_1.txt",
            r"Day 32 - SMTP & Datetime\letter_templates\letter_2.txt", 
            r"Day 32 - SMTP & Datetime\letter_templates\letter_3.txt"]
random_letter = random.choice(letters)

if (now_month, now_day) in birthdays_dict:
    with open(random_letter) as f:
        lines = f.read().replace("[NAME]", birthdays_dict[(now_month, now_day)]["name"])
        
my_email = "louis.porter26@gmail.com"
password = "qnfb hbvr votm ewaq"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=f"{birthdays_dict[(now_month, now_day)]["email"]}", 
                        msg=f"Subject:Happy Birthday!\n\n{lines}")


