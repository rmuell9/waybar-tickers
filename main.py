import yfinance as yf
import sys


tickerSymbol = sys.argv[1]
ticker = yf.Ticker(tickerSymbol)
lastClose = ticker.info['previousClose']
current = ticker.info['currentPrice']
change = current - lastClose

price = tickerSymbol + ' $' + str(current)

if change < 0:
    sign = '-'
elif change > 0:
    sign = '+'
else:
    print(price)

priceChange = f' {sign}$' + str(round(abs(change), 2))
output = price + priceChange

print(output)
