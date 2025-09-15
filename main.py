import yfinance as yf
import sys


tickerSymbol = sys.argv[1]
ticker = yf.Ticker(tickerSymbol)
lastClose = ticker.info['previousClose']
current = round(ticker.info['currentPrice'], 2)
marketState = ticker.info['marketState']
change = current - lastClose
percent = round((abs(change/lastClose) * 100), 2)


if marketState == "REGULAR":
    mark = "✓ "
else:
    mark = "✗ "

price = mark + tickerSymbol + ' $' + str(current)

if change < 0:
    sign = ' -'
    color = "#f44336"
elif change > 0:
    sign = ' +'
    color = "#4caf50"
else:
    print(price)
    sys.exit()

priceChange = sign + "$" + str(round(abs(change), 2))
percentChange = sign + str(percent) + "%"
output = price + f'<span color="{color}">{percentChange + priceChange}</span>'


print(output)
