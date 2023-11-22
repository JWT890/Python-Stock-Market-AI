import requests
import matplotlib.pyplot as plt

ALPHA_VANTAGE_API_KEY = '' # Get your own free API key from AlphaVantage

def get_stock_data(symbol):
    base_url = 'https://www.alphavantage.co/query'
    function = 'TIME_SERIES_DAILY'
    api_key = ALPHA_VANTAGE_API_KEY

    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'Time Series (Daily)' in data:
        return data['Time Series (Daily)']
    else:
        print(f"Error: {data['Error Message']}")
        return None
    
def visualize_stock_data(data):
    dates = list(data.keys())
    prices = [float(data[date]['4. close']) for date in dates]

    plt.figure(figsize=(14, 10))
    plt.plot(dates, prices, label='Closing Price', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Stock Price Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def main():
    company_symbol = input('Enter a company symbol: ')
    stock_data = get_stock_data(company_symbol)
    if stock_data:
        visualize_stock_data(stock_data)
    else:
        print('Failed to fetch stock data.')

if __name__ == '__main__':
    main()