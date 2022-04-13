#import smtplib
#
#email = "kordixd1@gmail.com"
#password = "Kordusiak1234%"
#
#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()# make connection secure
#    connection.login(user=email, password=password)
#    connection.sendmail(from_addr=email,
#                        to_addrs="kordimalgorzata@gmail.com",
#                        msg="Subject:hello\n\nThis is a body of an email")
#import datetime as dt
#
#now = dt.datetime.now()
#year = now.year
#
#print(year)
#
#birth = dt.datetime(year=1999, month=5, day=4)
#print(birth)

import smtplib
import random
import datetime as dt

now = dt.datetime.now()
day = now.day
current = now.weekday()
print(current)




email = "gamil@gmail.com"
password = "password"

if day == 13:
    with open("quotes.txt") as f:
        a = f.readlines()
        quote = random.choice(a)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="lol.com",
                            msg=f"Subject:random_msg\n\n{quote}")


