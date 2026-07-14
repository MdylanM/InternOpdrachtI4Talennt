import pandas as pd

def read_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: CSV data as a DataFrame.
    """

    return pd.read_csv(file_path)

data = read_csv('output.csv')

def filtering(data: pd.DataFrame, col: str, value: str) -> pd.DataFrame:
    """
    Filters out the rows with the mentioned value in the mentionened column.
    
    Args:
        data (pd.DataFrame): Dataframe that needs to be filtered.
        col (str): The name of the column where the filtering will take place. 
        value (str): Mentioned value you want to filter out. 
    
    Returns:
        Filtered out dataframe. 
    
    """
    return data[data[col] != value]

def diff_value(data: pd.DataFrame, col:str) -> pd.DataFrame:  
    """
    Calculates the differences between the last value and the current one.

    Args:
        data (DataFrame): From this dataframe the difference in values needs to be calculated.
        col (str): From this column  the difference in values needs to be calculated. 
    
    Returns:
        Dataframe with the differences in value.
    
    """

    data[col] = data.groupby("Kenteken")["KmStand"].diff()
    return data

dataset = filtering(data, 'Brandstof','wassen')
print(diff_kmstand(dataset, "verschil"))
