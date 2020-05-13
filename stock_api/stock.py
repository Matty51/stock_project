import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = '9SWYFQZ5ERWH5OC7'

#Specify the stock tickers that will be included in our spreadsheet
tickers = [
            'MSFT',
            'AAPL',
            'AMZN',
            'GOOG',
            'FB',
            'BRK.B',
            'JNJ',
            'WMT',
            'V',
            'PG'
            ]

#Create an empty string called `ticker_string` that we'll add tickers and commas to
ticker_string = ''

#Loop through every element of `tickers` and add them and a comma to ticker_string
for ticker in tickers:
    ticker_string += ticker
    ticker_string += ','
    
#Drop the last comma from `ticker_string`
ticker_string = ticker_string[:-1]

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol=ticker_string, interval = '1min', outputsize = 'full')
print(data)

i = 1
while i==1:
    data, meta_data = ts.get_intraday(symbol=ticker_string, interval = '1min', outputsize = 'full')
    data.to_excel("stocks.xlsx")
    time.sleep(60)

close_data = data['4. close']
percentage_change = close_data.pct_change()

print(percentage_change)

last_change = percentage_change[-1]

if abs(last_change) > 0.0004:
    print(ticker + " Alert:" + last_change)

