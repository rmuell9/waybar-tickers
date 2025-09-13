<div align="center">

# Waybar Stock Ticker Module

[python](http://python.org)
[uv](https://github.com/astral-sh/uv)
[yfinance](https://github.com/ranaroussi/yfinance)
[waybar](https://github.com/Alexays/Waybar)
</div>

## Install
```bash
cd ~/.config/waybar
git clone http://github.com/rmuell9/waybar-tickers
cd waybar-tickers
uv sync
```

## Config
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
