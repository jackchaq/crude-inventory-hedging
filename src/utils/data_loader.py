import yfinance as yf
import os


def fetch_yfinance_data(ticker: str, start: str, end: str, save_path: str):
    df = yf.download(ticker, start=start, end=end)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path)
    return df
