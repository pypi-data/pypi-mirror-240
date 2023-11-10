import pandas as pd
from .preprocess import clean

# Read in meta data as a df
def create_metadata_df(metadata_path):
    meta_data = pd.read_csv(metadata_path)
    return meta_data

# Return specified df
def return_df(data_path, csv_name):
    df = pd.read_csv(data_path+csv_name)
    return df

# Create map of dfs for each school data (key: filename, value: df)
# Each school is matched with an index value (file_name_map) (key: filename, value: integer)
def create_master_df_list(metadata_path, data_path):
    file_name_map = {}
    dataframe_collection = {} 
    meta_data = create_metadata_df(metadata_path)
    files = meta_data.loc[:, 'Name_of_File']
    index = 0
    for file in files:
        file_name_map[file] = index
        df = pd.read_csv(data_path+file)
        df = clean(df=df, val=32767)
        dataframe_collection[file] = df
        index += 1
   
    return file_name_map, dataframe_collection