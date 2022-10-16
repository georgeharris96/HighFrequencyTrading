# Import required libraries
import yfinance as yf
from datetime import date

stocks = ('nvda', 'msft', 'ibm')

for stock in stocks:
    # Create ticker object
    ticker = yf.Ticker(stock)

    # Create dataframe with historical data
    historical_df = ticker.history(
        start='2000-01-01',
        end=date.today(),
        interval='1d'
    )

    # Save historical data as .csv
    historical_df.to_csv(f'{stock}_historical.csv')
