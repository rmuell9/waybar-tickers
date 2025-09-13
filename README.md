<div align="center">

# Waybar Stock Ticker Module

[python](http://python.org)
[yfinance](https://github.com/ranaroussi/yfinance)
[waybar](https://github.com/Alexays/Waybar)

`~/.config/waybar/config.json`
```vim
    "custom/stocks": {
        "exec": "$HOME/.config/waybar/waybar-tickers/display.sh AAPL",
        "restart-interval": 10
    }
```
