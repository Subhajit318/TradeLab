import yfinance as yf
import os

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

stocks = {
    "RELIANCE": "RELIANCE.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "INFY": "INFY.NS",
    "TCS": "TCS.NS",
    "ICICIBANK": "ICICIBANK.NS",
    "NIFTY50": "^NSEI"
}

for company, ticker in stocks.items():
    print(f"Downloading {company}...")

    data = yf.download(
        ticker,
        start="2021-01-01",
        end="2026-01-01",
        progress=False
    )

    data.to_csv(f"data/{company}.csv")

print("All files downloaded successfully!")