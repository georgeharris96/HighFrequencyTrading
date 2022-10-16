import pandas as pd


def calculateTarget(df):
    """
    Calculates target variable from a pandas dataframe, does this in an inplace fashion.
    Dataframe MUST contain columns 'Open' and 'Close'.
    :param df:
    """
    df['target'] = (df['Open'] < df['Close']).astype(float).shift(-1)
    return df
