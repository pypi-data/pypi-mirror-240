import datetime
import pandas as pd
import numpy as np
from dateutil import relativedelta
from scipy.stats import zscore

# Convert type of input to floating type
def format_to_float(val):
    return float(val)

# Convert type of input to string type
def format_to_string(val):
    return str(val)

# Add 'Month' column in df
def add_month(df):
    df['Month'] = df['TIMESTAMP'].dt.month
    return df

# Add 'Year' column in df
def add_year(df):
    df['Year'] = df['TIMESTAMP'].dt.year
    return df

# Convert 'TIMESTAMP' column to datetime object format
def timestamp_to_datetime(df):
    # Convert the column to datetime objects with the %Y, %m, %d %H:%M:%S format
    df['TIMESTAMP'] = df['TIMESTAMP'].apply(lambda x: datetime.datetime.strptime(x, '%b %d %Y-%H:%M:%S').strftime('%Y, %m, %d %H:%M:%S'))
    # Convert the formatted strings to datetime objects
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], format='%Y, %m, %d %H:%M:%S')

# Drop a row where every element is na
def drop_row_na(df):
    return df.dropna(axis='index', how='all', inplace=True)

# To drop the value 32767
def drop_val(df, val):
    df.replace(to_replace = val, value = np.nan, inplace=True)

# Drop all columns in df where every value is None
def drop_column_na(df):
    return df.dropna(axis='columns', how='all', inplace=True)

# Create timestamp type, replace invalid values (32767) with NaN, drop columns where every value is NaN, format all variable types to float
# For Sun Smart Schools, set val = 32767
def clean(df, val):
    timestamp_to_datetime(df)
    drop_val(df=df, val=val)
    drop_column_na(df=df)
    drop_row_na(df=df)

    for column in df:
        if column == 'TIMESTAMP':
            continue
        df[column] = df[column].map(format_to_float)
    return df

# Return start and end time in 'TIMESTAMP' column
def date_range(df):
    start = df.iloc[0]['TIMESTAMP']
    end = df.iloc[-1]['TIMESTAMP']
    return start, end

# Return the exact number of years, months, days, hours, and minutes between start and end timestamp data
def difference_in_range(start, end):
    difference = relativedelta.relativedelta(end, start)
    return difference

# Number of days between start and end timestamp data
def days_between_range(start, end):
    return ((end-start).days)

# Extract a subsection of df - used for displaying stats on specific range of data
def filter_df_time(df, start, end):
    pd.to_datetime(start, format='%Y-%m-%d %H:%M:%S')
    pd.to_datetime(end, format='%Y-%m-%d %H:%M:%S')
    mask = (df['TIMESTAMP'] >= pd.Timestamp(start)) & (df['TIMESTAMP'] <= pd.Timestamp(end))
    df_filter = df.loc[mask]
    return df_filter

# Return a portion of df with outliers
def return_outliers(df):
    df_outliers = df[(np.abs(zscore(df)) > 3).all(axis=1)]
    return df_outliers

# Remove outliers from user specifed columns
def remove_outliers(df, cols=[]):
    if cols == None:
        df = df[(np.abs(zscore(df)) <= 3).all(axis=1)]
    else: 
        for col in cols:
            if col in df.columns:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - 1.5*IQR
                upper = Q3 + 1.5*IQR
                
                upper_array = np.where(df[col]>=upper)[0]
                lower_array = np.where(df[col]<=lower)[0]
                df[col].drop(index=upper_array, inplace=True)
                df[col].drop(index=lower_array, inplace=True)
    return df