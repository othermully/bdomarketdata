import requests
import datetime

def main():
    process_item()
    
def get_item():
    url = 'https://api.arsha.io/v2/na/GetMarketPriceInfo?id=10007&sid=0&lang=en'    
    response = requests.get(url=url)
    return response.json()

def process_item():
    data = get_item()
    data = data["history"]
    for timestamp, price in data.items():
        seconds = int(timestamp) / 1000
        dt = datetime.datetime.fromtimestamp(seconds)
        print(f"{dt.strftime('%Y-%m-%d')}, Price: {price}")

if __name__ == "__main__":
    main()
