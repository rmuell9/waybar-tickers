<div align="center">

# Waybar Stock Ticker Module

[python](http://python.org)
[uv](https://github.com/astral-sh/uv)
[yfinance](https://github.com/ranaroussi/yfinance)
[waybar](https://github.com/Alexays/Waybar)
</div>

## Install
Make sure uv is installed for project management
```bash
cd ~/.config/waybar
git clone https://github.com/rmuell9/waybar-tickers
cd waybar-tickers
uv sync
```

## Config
`~/.config/waybar/config.jsonc`
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
Don't forget to integrate the module in `waybar/style.css`
## Extra
Adding Multiple Tickers - just make another one!
```json
    "modules-left": [
        "hyprland/workspaces",
        "custom/stocks",
        "custom/stocks-GOOG"
    ],

    "custom/stocks-GOOG": {
        "exec": "$HOME/.config/waybar/waybar-tickers/display.sh GOOG",
        "restart-interval": 10
    }
```

Extra Ideas - research shortcuts:
```json
    "custom/stocks-AAPL": {
        "exec": "$HOME/.config/waybar/waybar-tickers/display.sh AAPL",
        "restart-interval": 10,
        "on-click": "xdg-open https://finance.yahoo.com/",
        "on-click-right": "xdg-open https://www.sec.gov/search-filings",
        "tooltip-format": "AAPL 10-Q Dates: 10/31/24, 1/30/25, 5/1/25, 7/31/25"
    }
```
