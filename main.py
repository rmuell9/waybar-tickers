import yfinance as yf
import sys

tickerSymbol = sys.argv[1]
ticker = yf.Ticker(tickerSymbol)
lastClose = ticker.info['previousClose']
current = ticker.info['currentPrice']
change = current - lastClose

if change < 0:
    sign = '-'
else:
    sign = '+'


price = tickerSymbol + ' $' + str(current)
priceChange = f' {sign}$' + str(round(abs(change), 2))
output = price + priceChange

print(output)
