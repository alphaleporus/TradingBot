# Trading Bot

A Python-based algorithmic trading bot for backtesting scalping strategies on Indian stock market data using technical indicators.

## Overview

This project implements automated trading strategies with backtesting capabilities. It uses RSI (Relative Strength Index) and Bollinger Bands indicators to identify entry and exit points for scalping trades.

## Features

- **Multiple Strategy Implementations**: Pre-configured strategies for different stocks and indices
- **Technical Indicators**: 
  - RSI (Relative Strength Index)
  - Bollinger Bands
  - EMA (Exponential Moving Average)
- **Backtesting**: Historical data backtesting using the `backtesting.py` library
- **Visualization**: Interactive HTML charts showing trade performance and equity curves
- **Indian Market Support**: Compatible with NSE (National Stock Exchange) tickers

## Project Structure

```
TradingBot/
├── banknifty_scalping.py      # Scalping strategy for Bank Nifty index
├── scalping_bot.py             # General scalping strategy for NSE stocks
├── ScalpingStrategy.html       # Backtest visualization output
├── EMACrossStrategy.html       # EMA crossover strategy results
└── README.md                   # This file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Required Packages

Install the required dependencies:

```bash
pip install pandas yfinance backtesting ta
```

## Usage

### Running a Backtest

Execute any of the strategy files to run a backtest:

```bash
python banknifty_scalping.py
```

or

```bash
python scalping_bot.py
```

### Strategy Configuration

The strategies can be customized by modifying parameters in the respective files:

- **Cash**: Initial capital for backtesting (default: ₹50,000 - ₹100,000)
- **Commission**: Trading commission percentage (default: 0.001 or 0.1%)
- **Date Range**: Historical data period for backtesting
- **Ticker**: Stock or index symbol (e.g., `^NSEBANK`, `TCS.NS`)

### Example: Bank Nifty Scalping

```python
ticker = "^NSEBANK"  # Bank Nifty index
data = yf.download(ticker, start="2020-01-01", end="2024-12-31", interval="1d")
bt = Backtest(data, ScalpingStrategy, cash=50000, commission=0.001)
stats = bt.run()
print(stats)
bt.plot()
```

## Strategy Details

### Scalping Strategy

**Entry Conditions:**
- RSI < 30 (oversold)
- Price below lower Bollinger Band

**Exit Conditions:**
- RSI > 70 (overbought)
- Price above upper Bollinger Band

This strategy aims to capitalize on mean reversion by buying oversold conditions and selling overbought conditions.

## Outputs

After running a backtest, you'll get:

1. **Console Output**: Statistical summary including:
   - Total return
   - Sharpe ratio
   - Maximum drawdown
   - Win rate
   - Number of trades

2. **HTML Visualization**: Interactive chart showing:
   - Price action
   - Indicator overlays
   - Trade entry/exit points
   - Equity curve

## Supported Tickers

### Indian Market (NSE)
- Bank Nifty: `^NSEBANK`
- Individual stocks: Add `.NS` suffix (e.g., `TCS.NS`, `RELIANCE.NS`)

### US Market
- Stocks: Use standard ticker symbols (e.g., `AAPL`, `MSFT`, `GOOGL`)

## Important Notes

⚠️ **Disclaimer**: This is for educational and backtesting purposes only. Past performance does not guarantee future results. Always conduct thorough research and risk management before live trading.

- **Market Hours**: Consider market timings when scheduling automated trading
- **Data Quality**: Historical data accuracy depends on Yahoo Finance data feed
- **Commission**: Adjust commission rates based on your broker's actual fees
- **Slippage**: Real trading may experience slippage not accounted for in backtests

## Customization

To create your own strategy:

1. Extend the `Strategy` class from `backtesting.py`
2. Implement the `init()` method to initialize indicators
3. Implement the `next()` method with your trading logic
4. Run backtest and analyze results

```python
class MyStrategy(Strategy):
    def init(self):
        # Initialize your indicators here
        pass
    
    def next(self):
        # Implement your trading logic here
        pass
```

## Performance Optimization

- Use appropriate data intervals (1m, 5m, 15m, 1h, 1d) based on strategy type
- Optimize indicator parameters using the built-in optimizer
- Consider transaction costs and slippage in realistic scenarios

