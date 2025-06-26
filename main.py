import yfinance as yf
from indicators import add_indicators
from anomaly_detector import detect_anomalies

# 📈 Download data
ticker = 'AAPL'
df = yf.download(ticker, start='2020-01-01', end='2024-12-31')

# 🧮 Calculate indicators
df = add_indicators(df)
df.dropna(inplace=True)

# 🔍 Detect anomalies
detect_anomalies(df)
