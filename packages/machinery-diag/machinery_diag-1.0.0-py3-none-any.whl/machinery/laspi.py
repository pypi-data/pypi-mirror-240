import numpy as np

import pandas as pd
from pandas import DataFrame
import os
import re
from sklearn.model_selection import train_test_split


def load_metadata_laspi(data_dir: str) -> DataFrame:
    """
    Generate metadata from the directory structure.

    Returns:
        DataFrame: A Pandas DataFrame containing metadata columns:
            "id", "Case", "Speed_Frequency", "Load_Percent", "Speed", and "Filepath".
    """
    metadata: list[list] = []
    for case_name in os.listdir(data_dir):
        case_dir = os.path.join(data_dir, case_name)
        if not os.path.isdir(case_dir):
            continue

        for subcase_name in os.listdir(case_dir):
            subcase_dir = os.path.join(case_dir, subcase_name)
            if not os.path.isdir(subcase_dir):
                continue

            match = re.match(r'(\d+)hz_(\d+)%_(\d+)rpm', subcase_name)
            if match:
                speed_frequency, load_percent, speed = map(int, match.groups())
                for filename in os.listdir(subcase_dir):
                    file_path = os.path.join(subcase_dir, filename)
                    metadata.append([case_name, speed_frequency, load_percent, speed, file_path])

    meta_df = pd.DataFrame(metadata,
                           columns=["Case", "Speed_Frequency", "Load_Percent", "Speed", "Filepath"])
    meta_df['class'] = pd.factorize(meta_df['Case'])[0]
    return meta_df.reset_index(drop=True)


def split_metadata(metadata_df: DataFrame, group_by_col='Load_Percent', test_size=0.25):
    # Assuming you already have a metadata DataFrame named metadata_df
    groups = metadata_df.groupby(['Case', group_by_col])

    train_dfs = []
    test_dfs = []

    for group_name, group_data in groups:
        # Split the group data into train and test
        train_data, test_data = train_test_split(group_data, test_size=test_size, random_state=42)

        train_dfs.append(train_data)
        test_dfs.append(test_data)

    # Concatenate the DataFrames for each group
    train_df = pd.concat(train_dfs, ignore_index=True)
    test_df = pd.concat(test_dfs, ignore_index=True)

    return train_df,  test_df


def load_data(metadata_df: DataFrame):
    filepaths = metadata_df.Filepath.tolist()
    y = metadata_df['class'].tolist()

    # Load data from CSV files and create a list of NumPy arrays
    data = []
    for filepath in filepaths:
        # Assuming that your CSV files have a common structure with headers
        try:
            df = pd.read_csv(filepath, encoding='utf-8')
            if df.values.shape[1] != 7:
                print(f"shape  not consistent,  shape is = {df.values.shape[1]} for: {filepath}")
            data.append(df.values)
        except Exception as e:
            raise Exception
    data = np.stack(data, axis=0)
    y = np.array(y)
    return data, y



