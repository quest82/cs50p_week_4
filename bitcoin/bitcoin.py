import sys
import requests
import os
from dotenv import load_dotenv

def main(): 
    try:
        amount = sys.argv[1]
        if not amount.isdigit():
            raise ValueError
    except IndexError:
        print("Missing command-line argument")
    except ValueError:
        print("Command-line argument is not a number")
    
    BITCOIN_DATA = get_JSON()
    

def get_JSON(): # Gets the data on bitcoin from CapCoin
    load_dotenv()
    API = os.getenv("CRYPTO_KEY")
    try:
        crypto = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + API, timeout=5)
        crypto.raise_for_status()
    except requests.RequestException as err:
        print(f"Error occured during connection: {err}")
    else:
        return crypto.json()

# def calc_bitcoin_price(dictionary):


main()