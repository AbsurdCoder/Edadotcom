# auto_plotter.py

import pandas as pd
import matplotlib.pyplot as plt

def detect_numeric_columns(df):
    """Detect numeric columns in the dataframe."""
    return df.select_dtypes(include=['float64', 'int64']).columns

def detect_categorical_columns(df):
    """Detect categorical columns in the dataframe."""
    return df.select_dtypes(include=['object']).columns

def plot_scatter(df):
    """Automatically generate scatter plots for numeric columns."""
    numeric_cols = detect_numeric_columns(df)
    
    for i in range(len(numeric_cols)):
        for j in range(i+1, len(numeric_cols)):
            df.plot.scatter(x=numeric_cols[i], y=numeric_cols[j])
            plt.show()

def plot_box(df):
    """Automatically generate box plots for numeric vs categorical columns."""
    numeric_cols = detect_numeric_columns(df)
    categorical_cols = detect_categorical_columns(df)

    for num_col in numeric_cols:
        for cat_col in categorical_cols:
            df.boxplot(column=num_col, by=cat_col)
            plt.show()

def plot_bar(df):
    """Automatically generate bar plots for categorical columns."""
    categorical_cols = detect_categorical_columns(df)
    
    for cat_col in categorical_cols:
        df[cat_col].value_counts().plot.bar()
        plt.ylabel('Count')
        plt.title(f'Bar plot for {cat_col}')
        plt.show()

# The main function to call these plotting functions
def auto_plot(df):
    plot_scatter(df)
    plot_box(df)
    plot_bar(df)

