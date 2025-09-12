import yfinance as yf
import sys

tickerSymbol = sys.argv[1]
ticker = yf.Ticker(tickerSymbol)

formattedPrice = tickerSymbol + ' $' + str(ticker.info['currentPrice'])
print(formattedPrice)
