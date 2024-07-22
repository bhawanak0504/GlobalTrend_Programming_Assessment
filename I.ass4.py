import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def clean_and_preprocess_data(df):
    """
    Clean and preprocess a given DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame to be cleaned and preprocessed.

    Returns:
    - pd.DataFrame: Preprocessed DataFrame with cleaned and normalized columns.
    """
    # Handling missing values
    df_cleaned = df.dropna()

    # Normalizing numerical columns (using StandardScaler)
    numerical_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df_cleaned[numerical_cols] = scaler.fit_transform(df_cleaned[numerical_cols])

    # Encoding categorical columns
    categorical_cols = df_cleaned.select_dtypes(include=['object']).columns
    encoder = LabelEncoder()
    for col in categorical_cols:
        df_cleaned[col] = encoder.fit_transform(df_cleaned[col])

    return df_cleaned

# Example DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': ['cat', 'dog', 'bird', 'cat'],
    'C': [0.1, 0.2, 0.3, None],
    'D': [100, 200, 300, 400]
}
df = pd.DataFrame(data)

# Clean and preprocess the DataFrame
preprocessed_df = clean_and_preprocess_data(df)
print(preprocessed_df)