"""
Data Preprocessor for Credit Card Fraud Detection

This module provides a reusable DataPreprocessor class that encapsulates
the feature engineering and scaling pipeline used in the credit card
fraud detection model.

Key Features:
    - Scales 'Time' and 'Amount' features using separate StandardScaler
      instances to avoid data leakage between features.
    - Drops original 'Time' and 'Amount' columns after scaling.
    - Separates features (X) from target (y) for model training.
    - Applies SMOTE oversampling to handle class imbalance.

Usage:
    >>> from preprocessing import DataPreprocessor
    >>> preprocessor = DataPreprocessor()
    >>> X_train, X_test, y_train, y_test = preprocessor.fit_transform(df)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE


class DataPreprocessor:
    """Handles preprocessing steps for the credit card fraud detection pipeline.

    This class encapsulates feature scaling (for 'Time' and 'Amount'),
    train/test splitting, and SMOTE oversampling into a single reusable
    interface.

    Attributes:
        amount_scaler (StandardScaler): Scaler fitted on the 'Amount' feature.
        time_scaler (StandardScaler): Scaler fitted on the 'Time' feature.
        test_size (float): Fraction of data reserved for testing.
        random_state (int): Seed for reproducibility.
    """

    def __init__(self, test_size=0.2, random_state=42):
        """Initialize the DataPreprocessor.

        Args:
            test_size (float): Proportion of the dataset to include in the
                test split. Defaults to 0.2.
            random_state (int): Random seed for reproducibility across
                train/test split and SMOTE. Defaults to 42.
        """
        self.amount_scaler = StandardScaler()
        self.time_scaler = StandardScaler()
        self.test_size = test_size
        self.random_state = random_state

    def scale_features(self, df):
        """Scale 'Amount' and 'Time' features using separate StandardScalers.

        Uses separate scaler instances for each feature to avoid the bug where
        a single scaler's fit is overwritten by the second fit_transform call.

        Args:
            df (pd.DataFrame): Input DataFrame containing 'Amount', 'Time',
                and other feature columns.

        Returns:
            pd.DataFrame: A copy of the DataFrame with 'Amount' and 'Time'
                replaced by 'scaled_amount' and 'scaled_time'.

        Raises:
            KeyError: If 'Amount' or 'Time' columns are not found in df.
        """
        df = df.copy()
        df['scaled_amount'] = self.amount_scaler.fit_transform(
            df['Amount'].values.reshape(-1, 1)
        )
        df['scaled_time'] = self.time_scaler.fit_transform(
            df['Time'].values.reshape(-1, 1)
        )
        df = df.drop(['Time', 'Amount'], axis=1)
        return df

    def split_data(self, df):
        """Split DataFrame into train and test sets with stratification.

        Args:
            df (pd.DataFrame): Preprocessed DataFrame containing a 'Class'
                target column and feature columns.

        Returns:
            tuple: (X_train, X_test, y_train, y_test) — feature and target
                arrays for training and testing.
        """
        X = df.drop('Class', axis=1)
        y = df['Class']
        return train_test_split(
            X, y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=y
        )

    def apply_smote(self, X_train, y_train):
        """Apply SMOTE oversampling to balance the training set.

        Args:
            X_train (pd.DataFrame or np.ndarray): Training features.
            y_train (pd.Series or np.ndarray): Training labels.

        Returns:
            tuple: (X_resampled, y_resampled) — balanced training data.
        """
        sm = SMOTE(random_state=self.random_state)
        return sm.fit_resample(X_train, y_train)

    def fit_transform(self, df):
        """Run the full preprocessing pipeline.

        Convenience method that chains scale_features → split_data →
        apply_smote and returns the final train/test arrays.

        Args:
            df (pd.DataFrame): Raw input DataFrame with 'Time', 'Amount',
                'Class', and PCA feature columns.

        Returns:
            tuple: (X_train_resampled, X_test, y_train_resampled, y_test)
        """
        df = self.scale_features(df)
        X_train, X_test, y_train, y_test = self.split_data(df)
        X_train_res, y_train_res = self.apply_smote(X_train, y_train)
        return X_train_res, X_test, y_train_res, y_test
