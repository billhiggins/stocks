import yfinance as yf
from datetime import datetime, timedelta
import sys

def fetch_last_five_days(ticker: str):
    """
    Fetch the last five trading days of daily price data for the given ticker
    and print the results to standard output.
    """

    end = datetime.today()
    # Fetch a slightly wider window to guarantee 5 trading days (weekends/holidays)
    start = end - timedelta(days=10)

    print(f"Fetching data for {ticker} from {start.date()} to {end.date()}...")

    try:
        data = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)
    except Exception as e:
        print("Error fetching data:", e)
        return

    if data.empty:
        print("No data returned.")
        return

    # Keep only the last 5 rows (trading days)
    last_five = data.tail(5)

    for date, row in last_five.iterrows():
        print("-----")
        print("Date:", date.date())
        print("Open:", float(row["Open"].iloc[0]))
        print("High:", float(row["High"].iloc[0]))
        print("Low:", float(row["Low"].iloc[0]))
        print("Close:", float(row["Close"].iloc[0]))
        print("Adj Close:", float(row["Adj Close"].iloc[0]))
        print("Volume:", int(row["Volume"].iloc[0]))

    print("-----")
    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: python fetch_daily_prices.py <TICKER>")
    ticker = sys.argv[1].upper()
    fetch_last_five_days(ticker)