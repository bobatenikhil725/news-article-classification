import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_labels(df, column_name):
    """
    Label encode a specified column in a dataframe
    
    Args:
        df (pandas.DataFrame): Input dataframe
        column_name (str): Name of the column to encode
        
    Returns:
        pandas.DataFrame: DataFrame with encoded column
        LabelEncoder: The fitted label encoder for future use
    """
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} not found in dataframe")
        
    # Create a label encoder
    le = LabelEncoder()
    
    # Fit and transform the column
    df[f"{column_name}_encoded"] = le.fit_transform(df[column_name])
    
    return df, le

def decode_labels(encoded_values, label_encoder):
    """
    Decode previously encoded values back to original labels
    
    Args:
        encoded_values (array-like): The encoded values to decode
        label_encoder (LabelEncoder): The fitted LabelEncoder used for encoding
        
    Returns:
        array-like: Original labels
    """
    return label_encoder.inverse_transform(encoded_values)