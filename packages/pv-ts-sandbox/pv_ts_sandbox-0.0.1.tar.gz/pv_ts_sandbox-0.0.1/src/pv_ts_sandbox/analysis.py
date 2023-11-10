import pandas as pd
import numpy as np
from .preprocess import add_month, add_year
import calendar

# Count all missing data
def count_missing(df):
    return df.isna().sum().sum()

# Count missing data in each column
def count_missing_per_col(df):
    missing = {}
    for (colName, colData) in df.iteritems():
        if colName == "TIMESTAMP":
            continue
        missing[colName] = colData.isna().sum()
    return missing

# Count missing for specified column
def count_missing_for_col(df, col):
    if col in df.columns:
        return df[col].isna().sum()
    else:
        print("Invalid parameter input") 
        return

# Calculate mean of input variable 
def calculate_mean(df, col):
    if col in df.columns:
        mean_value = df[col].mean()
        return mean_value
    else:
        print("Invalid parameter input") 
        return

# Calculate median of input variable 
# Variable is an option of column headers
def calculate_median(df, col):
    if col in df.columns:
        median_value = df[col].median()
        return median_value
    else:
        print("Invalid parameter input")
        return

# Calculate range of input variable 
# Variable is an option of column headers
def calculate_range(df, col):
    if col in df.columns:
        min_val = min(df[col])
        max_val = max(df[col])
        return min_val,max_val
    else:
        print("Invalid parameter input")
        return

# Calculate mode of input variable 
# Variable is an option of column headers
def calculate_mode(df, col):
    if col in df.columns:
        mode = df[col].mode().iloc[0]
        return mode
    else:
        print("Invalid parameter input")
        return

# Variables [] are user selected column headers
def summarize_data(df,col):
    
    if col not in df.columns:
        print("Invalid parameter input")
        return

    mean_value = calculate_mean(df=df, col=col)
    median_value = calculate_median(df=df,col=col)
    min, max = calculate_range(df=df, col=col)
    range_value = max-min
    mode_val = calculate_mode(df=df, col=col)
    summary = {'Mean': mean_value, 'Median': median_value, 'Min': min , 'Max':  max, 'Range': range_value,  'Mode': mode_val}
    return summary

# Return df with hourly energy based on user input variable
def calculate_hourly_energy(df, col):
    if col in df.columns:
        newdf = df.copy()
        newdf.set_index('TIMESTAMP', inplace=True) 
        df_hourly_energy = newdf[col].resample('H').sum()
        return df_hourly_energy
    else:
        print("Invalid parameter input")
        return

# Return df with daily energy based on user input variable
def calculate_daily_energy(df, col):
    if col in df.columns:
        newdf = df.copy()
        newdf.set_index('TIMESTAMP', inplace=True) 
        df_daily_energy = newdf[col].resample('D').sum()
        return df_daily_energy
    else:
        print("Invalid parameter input")
        return

# Return df with monthly energy based on user input variable
def calculate_monthly_energy(df, col):
    if col in df.columns:     
        newdf = df.copy()
        newdf.set_index('TIMESTAMP', inplace=True) 
        df_monthly_energy = newdf[col].resample('M').sum()
        return df_monthly_energy
    else:
        print("Invalid parameter input")
        return

# Return df with annual energy based on user input variable
def calculate_annual_energy(df, col):  
    if col in df.columns:  
        newdf = df.copy()
        newdf.set_index('TIMESTAMP', inplace=True) 
        df_annual_energy = newdf[col].resample('Y').sum()
        return df_annual_energy
    else:
        print("Invalid parameter input")
        return

# Return df with three additional columns 'Power_1', 'Power_2', 'Power_3' representing power found from each of the 3 arrays
# Power = Current x Voltage
def calculate_power(meta_data, df, index):
    curr1= meta_data.loc[index, 'pv-array1-current-out'] 
    volt1 = meta_data.loc[index, 'pv-array1-voltage-out'] 
    df['Power_1'] = df[curr1] * df[volt1]

    curr2= meta_data.loc[index, 'pv-array2-current-out'] 
    volt2 = meta_data.loc[index, 'pv-array2-voltage-out'] 
    df['Power_2'] = df[curr2] * df[volt2]

    curr3= meta_data.loc[index, 'pv-array3-current-out'] 
    volt3 = meta_data.loc[index, 'pv-array3-voltage-out'] 
    df['Power_3'] = df[curr3] * df[volt3]

    return df

# Based on input year and month, calculates total sum of power for each of the 3 power arrays in DataFrame df.
def calculate_total_power_year_month(meta_data, df, index, year, month):
    if 'Year' not in df.columns:
         add_year(df)
    if 'Month' not in df.columns:
        add_month(df)

    if 'Power_1' not in df.columns or 'Power_2' not in df.columns or 'Power_3' not in df.columns:
        calculate_power(meta_data, df, index)
    
    df_power_year = df.loc[df['Year'] == year]
    df_power_year_month = df_power_year.loc[df['Month'] == month]

    sum_1 = df_power_year_month['Power_1'].sum()
    sum_2 = df_power_year_month['Power_2'].sum()
    sum_3 = df_power_year_month['Power_3'].sum()

    return  [sum_1, sum_2, sum_3]

# Based on the ‘Year’ column, returns all unique years in DataFrame df
def find_unique_years(df):
    if 'Year' not in df.columns:
         add_year(df)
    years = df.Year.unique()
    return years

# Create a new DataFrame df_power for total power for power array 1, power array 2, power array 3
# Rows = [0-11] representing months in a year
# Columns = [years] representing unique years present in DataFrame df
def create_year_month_power_df(meta_data, df, index):
    years = find_unique_years(df)
    power_map = {}

    for year in years:
        data = []
        for i in range (12):
            data.append(calculate_total_power_year_month(meta_data, df, index, year, i+1))
        power_map[year] = data
    
    df_power = pd.DataFrame.from_dict(power_map)
    return df_power

# Creates a new DataFrame of df_degradation with rows = [Power Array 1, Power Array 2, Power Array 3] and columns = [years [ months within years]]
# Comparing two years at a time, degradation is found by comparing the total power of all three arrays for each of the two years for the same month. 
# (Year2 - Year1) / Year1
def create_degradation_df(meta_data, df, index):
    df_power = create_year_month_power_df(meta_data, df, index)
    years = find_unique_years(df)
    degradation_map = {}

    for i in range(len(years)-1):
        year1 = years[i]
        year2 = years[i+1]

        for k in range (12):
            month = calendar.month_abbr[k+1]
            
            np_array_first = np.array(df_power.iloc[k, i])
            np_array_second = np.array(df_power.iloc[k, i+1])
            
            # Array of 0s for current year power [0 0 0]
            if not np.any(np_array_first):
                continue

            # Array of 0s for next year power [0 0 0]
            if not np.any(np_array_second):
                continue

            # Suppress divide by 0 warning
            # Not all arrays of power (Power_1, Power_2, Power_3) always have a value
            with np.errstate(divide='ignore'):
                degradation_list = np.divide((np_array_second - np_array_first), np_array_first)
                degradation_map[((year1, year2), month)] = degradation_list
   
    df_degradation = pd.DataFrame.from_dict(degradation_map)
    df_degradation.rename(index={0: 'Power Array 1', 1: 'Power Array 2', 2: 'Power Array 3'}, inplace=True)
    return df_degradation