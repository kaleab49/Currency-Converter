import requests
import math



Base_url = "https://api.freecurrencyapi.com/v1/latest"

Api_key = "fca_live_hxH8BgDmzqx85zo2y9iAo5aMkxdd7zUZjds5dmRU"


def get_currency():
    
    url = f"{Base_url}?apikey={Api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        print(data)
    
    else:
        print("Error 404!!")


get_currency()