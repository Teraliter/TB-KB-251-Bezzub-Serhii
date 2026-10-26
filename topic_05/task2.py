import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={}&json"
CURRENCIES = ["EUR", "USD", "PLN"]

def get_rate(code):
    response = requests.get(URL.format(code), timeout=10)
    response.raise_for_status()
    return response.json()[0]["rate"]

code = input("Enter currency (EUR, USD, PLN): ").strip().upper()

if code not in CURRENCIES:
    print("Unsupported currency")
else:
    try:
        amount = float(input("Enter amount: "))
        rate = get_rate(code)
        print(f"Rate: 1 {code} = {rate} UAH")
        print(f"{amount} {code} = {round(amount * rate, 2)} UAH")
    except ValueError:
        print("Invalid amount")
    except requests.RequestException:
        print("Failed to get exchange rate from NBU")
