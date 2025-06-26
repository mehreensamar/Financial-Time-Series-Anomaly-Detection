import pandas as pd

def add_indicators(df):
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['STD'] = df['Close'].rolling(window=20).std()
    df['Upper_BB'] = df['SMA_20'] + (2 * df['STD'])
    df['Lower_BB'] = df['SMA_20'] - (2 * df['STD'])

    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    return df
