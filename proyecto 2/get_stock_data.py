import requests as requests
 
API_KEY= "11DEP9BZAQ04JQ3F"

def get_stock_data(simbolo):
 url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol"
 
 response= requests.get(url)
 
 if response.status_code == 200:
     datos=response.json() 
     print(datos)
     
get_stock_data("5005")
