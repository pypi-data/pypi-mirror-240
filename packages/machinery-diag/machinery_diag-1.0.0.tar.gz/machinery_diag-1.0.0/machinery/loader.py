import os
import re
from typing import List, Tuple

import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from loguru import logger


def load_data(metadata_df: DataFrame, data_type: str = 'laspi') -> Tuple[
    np.ndarray, np.ndarray]:
    """
    Load data from CSV files specified in the metadata DataFrame and return NumPy arrays.

    Args:
        metadata_df (DataFrame): The metadata DataFrame containing file paths and class information.
        max_rows (int, optional): Maximum number of rows to load per file.
        data_type (str): Type of data ('laspi', 'ampere', 'metalida_dour').

    Returns:
        Tuple[np.ndarray, np.ndarray]: A tuple containing data (X) as a NumPy array and labels (y) as a NumPy array.

    Raises:
        FileNotFoundError: If any of the CSV files specified in metadata_df do not exist.
        ValueError: If the number of columns in the loaded CSV files is inconsistent.
        Exception: If the file format is not accepted.

    """
    filepaths = metadata_df.Filepath.tolist()
    y = metadata_df['class'].to_numpy()
    map_num_cols = {
        "laspi": 7,
        "ampere": 11,
        "metalida_dour": 12
    }
    num_cols = map_num_cols[data_type]
    data = []

    # parameter used for data with different number of rows among files
    min_rows = float('inf')

    for filepath in filepaths:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        try:
            if str(filepath).endswith(".csv"):
                df = pd.read_csv(filepath, encoding='utf-8')
                if df.values.shape[1] != num_cols:
                    raise ValueError(
                        f"Inconsistent number of columns in file {filepath}. Expected: {num_cols}, Actual: {df.shape[1]}")

                # Update min_rows based on the minimum number of rows in the current file
                min_rows = min(min_rows, df.values.shape[0])

                data.append(df.values[:min_rows])
            else:
                raise Exception("File format not accepted. Use CSV format.")
        except Exception as e:
            raise Exception(f"Error while loading CSV file: {filepath}, with error: {e}")
    data = [arr[:min_rows] for arr in data]
    data = np.stack(data, axis=0)
    return data, y


class MachineryDataLoader:
    def __init__(self, config: dict):
        """
        Initialize the MachineryDataLoader.

        Args:
            config (dict): Configuration dictionary containing parameters.

        """
        self.data_dir = config['data_dir']
        if config['data_type'] not in ['ampere', 'laspi', 'metalica_dour']:
            raise Exception("Invalid data type. It should be one of: ampere, laspi, metalica_dour")
        self.data_type = config['data_type']
        self.file_extension = ".csv"
        self.metadata_cols = ["Case", "Speed_Frequency", "Load_Percent", "Speed", "Filepath"]

        self.group_by_cols = config['group_by_cols']
        self.test_size = config['test_size']
        self.random_state = config.get('random_state', 42)
        self.max_rows = config.get('max_rows', None)

        self.metadata_df = None
        self.train_df = None
        self.test_df = None
        self.class_mapping = None
        self.data = None
        self.target = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def load_metadata(self) -> DataFrame:
        """
        Generate metadata from the directory structure.

        Returns:
            DataFrame: A Pandas DataFrame containing metadata columns.

        """
        metadata: List[List] = []
        for case_name in os.listdir(self.data_dir):
            case_dir = os.path.join(self.data_dir, case_name)
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
                        if filename.endswith(self.file_extension):
                            file_path = os.path.join(subcase_dir, filename)
                            metadata.append([case_name, speed_frequency, load_percent, speed, file_path])
                        else:
                            logger.warning(
                                f"The file {filename} is excluded. It is not in the required format {self.file_extension}")
                else:
                    logger.warning(
                        f"Folder {subcase_name} does not match the format: Xhz_Y%_Zrpm where X, Y, Z are integer values")

        self.metadata_df = pd.DataFrame(metadata, columns=self.metadata_cols)
        factorized, unique_values = pd.factorize(self.metadata_df['Case'])
        self.class_mapping = dict(zip(np.unique(factorized), unique_values))
        self.metadata_df['class'] = factorized
        self.metadata_df.reset_index(drop=True)
        return self.metadata_df

    def split_metadata(self) -> Tuple[DataFrame, DataFrame]:
        """
        Split metadata DataFrame into training and testing sets.

        Returns:
            Tuple[DataFrame, DataFrame]: A tuple containing the training and testing DataFrames.

        """
        if self.metadata_df is None:
            self.metadata_df = self.load_metadata()

        try:
            if self.group_by_cols in ["", '', None, 'none', 'None']:
                groups = self.metadata_df.groupby(['Case'])
            else:
                groups = self.metadata_df.groupby(['Case', self.group_by_cols])
        except Exception:
            raise Exception(f"Column(s) {self.group_by_cols} is/are not valid")

        train_dfs = []
        test_dfs = []

        for group_name, group_data in groups:
            train_data, test_data = train_test_split(group_data, test_size=self.test_size,
                                                     random_state=self.random_state)
            train_dfs.append(train_data)
            test_dfs.append(test_data)

        self.train_df = pd.concat(train_dfs, ignore_index=True)
        self.test_df = pd.concat(test_dfs, ignore_index=True)

        return self.train_df, self.test_df

    def load_global_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Load global data.

        Returns:
            Tuple[np.ndarray, np.ndarray]: A tuple containing the data (X) and labels (y).

        """
        if self.metadata_df is None:
            self.metadata_df = self.load_metadata()

        if self.data_type in ['laspi', 'ampere']:
            self.data, self.target = load_data(self.metadata_df, self.data_type)

        if self.data_type == 'metalica_dour':
            print('Loading metalica dour...')
        return self.data, self.target

    def load_split_data(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Load split data.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: A tuple containing training data (X_train),
            testing data (X_test), training labels (y_train), and testing labels
        """
        if self.metadata_df is None:
            self.metadata_df = self.load_metadata()

        if self.train_df is None or self.test_df is None:
            _, _ = self.split_metadata()

        if self.data_type in ['laspi', 'ampere']:

            X_train, y_train = load_data(self.train_df, self.data_type)
            X_test, y_test = load_data(self.test_df, self.data_type)

            # Find the minimum number of rows between X_train and X_test
            min_rows = min(X_train.shape[1], X_test.shape[1])

            # Update X_train and X_test based on the minimum number of rows
            self.X_train, self.y_train = X_train[:, :min_rows, :], y_train
            self.X_test, self.y_test = X_test[:, :min_rows, :], y_test

        return self.X_train, self.X_test, self.y_train, self.y_test
