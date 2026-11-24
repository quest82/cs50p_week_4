import sys
import requests
import json
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
    get_JSON()

def get_JSON():
    load_dotenv()
    API = os.getenv("CRYPTO_KEY")
    crypto = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + API)
    print(crypto.status_code, crypto.json())
    # print(json.dumps(crypto.json()))

main()