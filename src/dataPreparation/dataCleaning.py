# Import required libraries
import pandas as pd

def dataCleaning(df, temporal=False):
    df.drop(columns=['Dividends', 'Stock Splits'], inplace=True)

    df.drop_duplicates(inplace=True)

    if temporal:
        df.drop(columns=['Date'])

    pass
