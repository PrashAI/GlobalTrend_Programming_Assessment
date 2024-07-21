# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:14:46 2024

@author: prasa
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_dataframe(df):
    # Identify numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Define a pipeline for numerical features
    numerical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),  # Handle missing values by replacing with the mean
        ('scaler', StandardScaler())  # Normalize numerical columns
    ])

    # Define a pipeline for categorical features
    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Handle missing values by replacing with the most frequent value
        ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Encode categorical columns
    ])

    # Combine numerical and categorical pipelines into a single ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_pipeline, numerical_cols),
            ('cat', categorical_pipeline, categorical_cols)
        ]
    )

    # Apply the transformations to the DataFrame
    df_processed = preprocessor.fit_transform(df)

    # Convert the result back to a DataFrame with appropriate column names
    df_processed = pd.DataFrame(df_processed, columns=(
        preprocessor.named_transformers_['num']['scaler'].get_feature_names_out(numerical_cols).tolist() +
        preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols).tolist()
    ))

    return df_processed

# Example usage:
data = {
    'age': [25, 30, 35, 40, None],
    'salary': [50000, 60000, 70000, None, 90000],
    'city': ['New York', 'Los Angeles', 'New York', None, 'Chicago']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df_cleaned = preprocess_dataframe(df)
print("\nCleaned and Preprocessed DataFrame:")
print(df_cleaned)
