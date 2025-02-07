import pandas as pd

def read_csv(file_path):
    """
    Reads a CSV file and returns the data as a pandas DataFrame.
    
    Parameters:
    - file_path (str): The path to the CSV file.
    
    Returns:
    - pd.DataFrame: The data from the CSV file.
    """
    return pd.read_csv(file_path)