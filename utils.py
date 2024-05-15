import requests

def fetch_stock_data(symbols):
    stock_data = {}
    for symbol in symbols:
        # Make API call to Alpha Vantage
        response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&apikey=YOUR_API_KEY')
        data = response.json()
        # Extract latest price from response
        latest_data = data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]
        latest_price = latest_data['4. close']
        stock_data[symbol] = latest_price
    return stock_data
  
