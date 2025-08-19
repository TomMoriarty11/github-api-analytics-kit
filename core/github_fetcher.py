import requests
import time

def fetch_data(url, headers=None, params=None, max_retries=3, delay=2):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403 and "rate limit" in response.text.lower():
            print("Rate limit hit. Retrying...")
            time.sleep(delay * (attempt + 1))
        else:
            response.raise_for_status()
    raise Exception("Failed to fetch data after retries.")
