import requests
import json



Base_url = "https://api.freecurrencyapi.com/v1/latest"

Api_key = open("api.txt", "r").read()


def get_currency():
    
    url = f"{Base_url}?apikey={Api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        
        
        exchange_rates = data["data"]

        user_currency = input("What Currency you wanna see: ")
    
        print(f"{user_currency} to USD:", exchange_rates[f"{user_currency}"])

        for currency, rate in exchange_rates.items():
            
            print(f"{currency}: {rate}")
           
    
    else:
        print("Error 404!!")


get_currency()