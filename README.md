<div align="center">

# Waybar Stock Ticker Module

[python](http://python.org)
[yfinance](https://github.com/ranaroussi/yfinance)
[waybar](https://github.com/Alexays/Waybar)
</div>

`~/.config/waybar/config.json`
```json
    "custom/stocks": {
        "exec": "$HOME/.config/waybar/waybar-tickers/display.sh AAPL",
        "restart-interval": 10
    }
```
Example: putting module on left side of waybar, to the right of the workspaces
```json
    "modules-left": [
        "hyprland/workspaces",
        "custom/stocks"
    ],
```
