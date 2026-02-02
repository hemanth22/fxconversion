import requests
import os
import redis


def fetch_and_transform_rates(api_key):
    # API Endpoint
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
    
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to connect. Status Code: {response.status_code}")
            return

        data = response.json()
        
        if data.get("result") == "success":
            base = data.get("base_code", "USD")
            rates = data.get("conversion_rates", {})
            
            print(f"{'Currency Pair'} | {'Bid'} | {'Ask'}")
            print("-" * 55)

            for target_currency, rate in rates.items():
                # Transform the format (e.g., USD + HKD = USDHKD)
                pair_name = f"{base}{target_currency}"
                
                # Logic: Bid is actual rate, Ask is rate + 0.90
                bid = rate
                ask = rate + 0.0010
                
                print(f"{pair_name} | {bid:.4f} | {ask:.4f}")

        if data.get("result") != "success":
            print("API Error:", data.get("error-type", "Unknown error occurred"))

    except Exception as e:
        print(f"An error occurred: {e}")

EX_API_KEY = os.environ.get('EX_API_KEY')

if __name__ == "__main__":
    fetch_and_transform_rates(EX_API_KEY)
