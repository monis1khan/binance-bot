# Binance Futures Testnet Trading Bot (Python)

## Overview
This project is a Python-based CLI trading bot that places MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).
It demonstrates clean project structure, input validation, logging, and proper error handling.

## Features
- MARKET and LIMIT order placement
- BUY and SELL support
- Binance Futures Testnet (USDT-M)
- Command-line interface (CLI)
- Logging of API requests and responses
- Error handling and validation
- Automatic server time synchronization

## Project Structure
project/
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
│   └── trading.log
├── cli.py
├── README.md
└── requirements.txt

## Setup

1. Install dependencies:
python -m pip install -r requirements.txt

2. Create a `.env` file in the project root:
BINANCE_API_KEY=your_api_key  
BINANCE_API_SECRET=your_api_secret

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

Limit Order:
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.005 --price 20000

## Logs
All requests and responses are logged in:
logs/trading.log

## Notes
- Uses Binance Futures Testnet (no real money)
- Orders may remain NEW due to testnet liquidity
- Minimum notional value is 100 USDT

## Author
Python Developer Intern Assignment