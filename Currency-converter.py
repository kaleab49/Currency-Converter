import requests
import json



Base_url = "https://api.freecurrencyapi.com/v1/latest"

Api_key = open("apikey.txt", "r").read().strip()


def get_currency():
    
    url = f"{Base_url}?apikey={Api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        
        
        exchange_rates = data["data"]

        user_currency = input("What Currency you wanna see: ")
    
        if user_currency in exchange_rates:
            print(f"{user_currency} to USD:", exchange_rates[user_currency])
        else:
            print(f"Currency {user_currency} not found!")

           
    
    else:
        print("Error 404!!")


get_currency()