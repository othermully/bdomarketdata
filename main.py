import requests
import datetime

def main():
    process_item_history()
    
def get_item_price_history():
    url = 'https://api.arsha.io/v2/na/GetMarketPriceInfo?id=10007&sid=0&lang=en'    
    response = requests.get(url=url)
    return response.json()

def get_item_market_trades():
    url = 'https://api.arsha.io/v2/na/GetWorldMarketSearchList?ids=10007&lang=en'
    response = requests.get(url=url)
    return response.json()

def process_item_history():
    data = get_item_price_history()
    data = data["history"]

    price_history_dict = {}
    price_history_list = []

    for timestamp, price in data.items():
        seconds = int(timestamp) / 1000
        dt = datetime.datetime.fromtimestamp(seconds)
        #print(f"{dt.strftime('%Y-%m-%d')}, Price: {price}")
        price_history_dict[dt.strftime('%Y-%m-%d')] = price

    for date, price in price_history_dict.items():
        price_history_list.append({date, price})

    return price_history_list

def process_item_trades():
    data = get_item_market_trades()
    total_trades = data["totalTrades"]
    return total_trades

if __name__ == "__main__":
    main()
