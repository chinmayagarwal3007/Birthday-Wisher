import smtplib
import datetime as dt

import pandas

testing = pandas.read_csv("birthdays.csv")
data = testing.to_dict(orient="records")

my_email = "email"
my_password = "password"

x = dt.datetime.now()

for i in range(len(data)):
    if(x.year == data[i]['year'] and x.month == data[i]['month'] and x.day == data[i]['day']):

        with smtplib.SMTP("smtp mail server") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data[i]['email'],
                msg = "Subject:Happy Birthday!!\n\nHappy Birthday to you."
            )