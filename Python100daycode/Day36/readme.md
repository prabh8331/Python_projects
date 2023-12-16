https://www.tradingview.com/symbols/NASDAQ-TSLA/

1. Stock Price: pull closing price compare the difference from the day before and pull difference and show the % change
2. pull news data
3. send msg/ mail -- 

<https://newsapi.org/>   #news api

the_api_key_for_newsapi

import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-12-10&'
       'sortBy=popularity&'
       'apiKey=the_api_key_for_newsapi')


"https://newsapi.org/v2/everything?q=Apple&from=2023-12-10&sortBy=popularity&apiKey=the_api_key_for_newsapi"

from yesterday sorted by popular
https://newsapi.org/v2/everything?q=apple&from=2023-12-15&to=2023-12-15&sortBy=popularity&apiKey=the_api_key_for_newsapi

last month, sorted by recent first
https://newsapi.org/v2/everything?q=tesla&from=2023-11-16&sortBy=publishedAt&apiKey=the_api_key_for_newsapi

top business headlines in the US right now
https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=the_api_key_for_newsapi


Top headlines from TechCrunch  right now
https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=the_api_key_for_newsapi

all artichles published by wall steet jornal in last 6 months sorted by recent
https://newsapi.org/v2/everything?domains=wsj.com&apiKey=the_api_key_for_newsapi

response = requests.get(url)


print response.json()



<https://www.alphavantage.co/>  #stock market api

https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=the_api_key_for_alphaavantage

https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=compact&apikey=the_api_key_for_alphaavantage




<https://www.twilio.com/en-us>  #sms api



setting up envrionmant variable in windows using powershell
```powershell
#get list of all environment variables 
Get-ChildItem Env:

# Set the environment variable
[Environment]::SetEnvironmentVariable("mypassappuser", "your_user_name", [EnvironmentVariableTarget]::User)

[Environment]::SetEnvironmentVariable("mypassappcode", "your_password", [EnvironmentVariableTarget]::User)

[Environment]::SetEnvironmentVariable("mypassappurl", "https://pass_app_api_end_point", [EnvironmentVariableTarget]::User)


# Display the environment variable to verify --- restart before 
$env:mypassappuser
$env:mypassappcode

[System.Environment]::GetEnvironmentVariable("mypassappuser", [System.EnvironmentVariableTarget]::User)

```