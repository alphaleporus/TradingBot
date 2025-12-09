import pandas as pd
import yfinance as yf
from backtesting import Backtest, Strategy
import ta  # Ensure you’ve run: pip install ta

class ScalpingStrategy(Strategy):
    def init(self):
        close = self.data.Close
        close_series = pd.Series(close, name="close")

        rsi_indicator = ta.momentum.RSIIndicator(close_series)
        bb_indicator = ta.volatility.BollingerBands(close_series)

        self.rsi = self.I(rsi_indicator.rsi)
        self.bb_high = self.I(bb_indicator.bollinger_hband)
        self.bb_low = self.I(bb_indicator.bollinger_lband)

    def next(self):
        price = self.data.Close[-1]

        # Buy condition
        if not self.position and self.rsi[-1] < 30 and price < self.bb_low[-1]:
            self.buy(size=1)  # fixed size order

        # Sell condition
        elif self.position and self.rsi[-1] > 70 and price > self.bb_high[-1]:
            self.sell(size=1)


# Load data
ticker = "^NSEBANK"  # NSE ticker; try "AAPL" for US
data = yf.download(ticker, start="2020-01-01", end="2024-12-31", interval="1d")

# Fix column index if necessary
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Keep only required columns
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.dropna(inplace=True)

# Run backtest
bt = Backtest(data, ScalpingStrategy, cash=50000, commission=0.001)
stats = bt.run()
print(stats)
bt.plot()
