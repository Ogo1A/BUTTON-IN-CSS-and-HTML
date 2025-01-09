import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_current_stock_data(ticker):
  """
  Fetches and displays current stock market data for a given ticker symbol.

  Args:
    ticker: The stock ticker symbol (e.g., "AAPL", "MSFT").
  """
  try:
    # Download the stock data
    stock_data = yf.download(ticker, period="1d") #Change period for more time span in data
    
    if stock_data.empty:
      print(f"No data found for ticker {ticker}")
      return

    # Display basic stock information
    print(f"Current Stock Data for {ticker}:")
    display(stock_data)

    # Plotting the adjusted closing price
    plt.figure(figsize=(10, 7))
    stock_data['Adj Close'].plot()
    plt.title(f"Adjusted Close Price of {ticker}", fontsize=16)
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.show()

  except Exception as e:
    print(f"An error occurred: {e}")

# Example usage
ticker_symbol = "AAPL"  # Replace with the desired ticker symbol
get_current_stock_data(ticker_symbol)
