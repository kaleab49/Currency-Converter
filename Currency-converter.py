import requests
import json
import customtkinter as ctk

Base_url = "https://api.freecurrencyapi.com/v1/latest"

Api_key = open("apikey.txt", "r").read().strip()

def get_currency():
    url = f"{Base_url}?apikey={Api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        exchange_rates = data["data"]
        user_currency = currency_entry.get()
        
        if user_currency in exchange_rates:
            result_label.config(text=f"{user_currency} to USD: {exchange_rates[user_currency]}")
        else:
            result_label.config(text=f"Currency {user_currency} not found!")
    else:
        result_label.config(text="Error 404!!")

app = ctk.CTk()
app.title("Currency Converter")
app.geometry("400x300")

currency_label = ctk.CTkLabel(app, text="Enter Currency (e.g., EUR, GBP):")
currency_label.pack(pady=10)

currency_entry = ctk.CTkEntry(app, width=200)
currency_entry.pack(pady=10)

convert_button = ctk.CTkButton(app, text="Convert", command=get_currency)
convert_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=20)

app.mainloop()
