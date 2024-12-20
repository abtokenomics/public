import pandas as pd



def merge_on_timestamp(dataframes):
    for df in dataframes:
        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')

    merged_dataset = dataframes[0]
    
    for df in dataframes[1:]:
        merged_dataset = pd.merge(merged_dataset, df, on='timestamp', how='outer')
        
    return merged_dataset



