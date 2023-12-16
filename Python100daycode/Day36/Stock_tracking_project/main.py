import requests

from datetime import datetime, timedelta

import pytz

import os

user_name = os.environ.get("mypassappuser")
user_code = os.environ.get("mypassappcode")
timeout = 10
pass_app_url = os.environ.get("mypassappurl")
get_data_url = pass_app_url + "get_data"
response = requests.get(get_data_url, auth=(user_name, user_code), timeout=timeout)
pass_data = response.json()


STOCK = "tsla"

COMPANY_NAME = "Tesla Inc"

timezone_ist = pytz.timezone('Asia/Kolkata')

time_now = datetime.now(timezone_ist)
yesterday = str(time_now.date() + timedelta(days=-1))
day_before_ytd = str(time_now.date() + timedelta(days=-2))
day_back_3 = str(time_now.date() + timedelta(days=-3))

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=compact&apikey=yourapi

stock_url = "https://www.alphavantage.co/query"

stock_api=pass_data["prabh8331@gmail.com"]["alphavantage_api"]

paramaters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize" : "compact",
    "apikey": stock_api,
}

response = requests.get(url=stock_url,params=paramaters)

data = response.json()

yst_data = data["Time Series (Daily)"][yesterday]
db_yst_data = data["Time Series (Daily)"][day_before_ytd]

yst_close = float(yst_data["4. close"])
db_yst_close = float(db_yst_data["4. close"])

change = yst_close - db_yst_close
percentage_change = (change/db_yst_close)*100

print(yst_close)
print(db_yst_close)
print(change)
print(percentage_change)
percentage_change= -5

if percentage_change >= 5 or percentage_change <= -5:
    print("get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

news_url="https://newsapi.org/v2/everything"
news_api=pass_data["prabh8331@gmail.com"]["newsapi_api"]

paramaters = {
    "q" : "tesla",
    "from" : day_back_3,
    "to" : yesterday,
    "sortBy" : "popularity",
    "apiKey" : news_api
}

response = requests.get(url=news_url,params=paramaters)

response.raise_for_status()

data = response.json()


import smtplib
import html
from email.mime.text import MIMEText

my_email = "prabh8331@gmail.com"

with open("C:/Users/prabh/OneDrive/Desktop/google_app_pass.txt") as login:
    password=login.readlines()[1].strip()


if percentage_change>0:
    icon = "🔺😊"
else:
    icon = "🔻☹️"



# mail_body = f"""Subject:{STOCK}{icon}\n\nHeadline: {data["articles"][0]["title"]}\nBrief" {data["articles"][0]["description"]}"""
headline1 = html.unescape(data["articles"][0]["title"]).replace('\r', '').replace('\n', '')
brief1 = html.unescape(data["articles"][0]["description"]).replace('\r', '').replace('\n', '')
mail_body1="Headline: "+headline1+"\n"+"Brief: "+brief1

headline2 = html.unescape(data["articles"][1]["title"]).replace('\r', '').replace('\n', '')
brief2 = html.unescape(data["articles"][1]["description"]).replace('\r', '').replace('\n', '')
mail_body2="Headline: "+headline2+"\n"+"Brief: "+brief2

headline3 = html.unescape(data["articles"][2]["title"]).replace('\r', '').replace('\n', '')
brief3 = html.unescape(data["articles"][2]["description"]).replace('\r', '').replace('\n', '')
mail_body3 ="Headline: "+headline3+"\n"+"Brief: "+brief3

mail_body = mail_body1+"\n \n"+mail_body2+"\n \n"+mail_body3+"\n \n"

msg = MIMEText(mail_body, 'plain', 'utf-8')
msg['Subject'] = 'Tesla News Headlines'+icon
msg['From'] = my_email
msg['To'] = my_email

# mail_body = MIMEText(mail_body, 'plain', 'utf-8')

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    
    connection.starttls()
    
    connection.login(user=my_email, password=password)
    
    connection.sendmail(from_addr=my_email, 
                    to_addrs=[my_email,"prabh8221@gmail.com"], 
                    msg=msg.as_string()
                    )






#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


