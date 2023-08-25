
import pandas as pd
import numpy as np

def remove_missing_values(df, axis=0, threshold=None):
    """
    Remove rows or columns with missing values from a DataFrame.

    Parameters:
    - df (pd.DataFrame): Input dataframe.
    - axis (int): 0 for rows, 1 for columns.
    - threshold (int): Minimum number of non-NA values to keep.

    Returns:
    - pd.DataFrame: DataFrame with missing values removed.
    """
    return df.dropna(axis=axis, thresh=threshold)


def replace_missing_with_value(df, value=0):
    """
    Replace missing values in a DataFrame with a specified value.

    Parameters:
    - df (pd.DataFrame): Input dataframe.
    - value: Value to replace NaNs with.

    Returns:
    - pd.DataFrame: DataFrame with NaNs replaced.
    """
    return df.fillna(value)


def remove_outliers(df, column_name, threshold=1.5):
    """
    Remove outliers from a DataFrame using the IQR method.

    Parameters:
    - df (pd.DataFrame): Input dataframe.
    - column_name (str): Name of the column to check for outliers.
    - threshold (float): IQR multiplier to determine outliers.

    Returns:
    - pd.DataFrame: DataFrame with outliers removed.
    """
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1

    filter = (df[column_name] >= Q1 - threshold * IQR) & (df[column_name] <= Q3 + threshold * IQR)
    return df[filter]


def convert_column_to_categorical(df, column_name):
    """
    Convert a DataFrame column to a categorical type.

    Parameters:
    - df (pd.DataFrame): Input dataframe.
    - column_name (str): Name of the column to convert.

    Returns:
    - pd.DataFrame: DataFrame with the specified column converted.
    """
    df[column_name] = df[column_name].astype('category')
    return df
