import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class FeatureEngineering:
    def __init__(self, df: pd.DataFrame, logging):
        self.df = df.copy()
        self.processed_df = None
        self.scaler = StandardScaler()  # Change to MinMaxScaler() if needed
        self.logging = logging
        self.logging.info("FeatureEngineering class initialized with the provided DataFrame.")

    def handle_missing_values(self):
        self.logging.info("Handling missing values...")
        try:
            # Fill missing MonthlyIncome with median
            self.df['MonthlyIncome'].fillna(self.df['MonthlyIncome'].median(), inplace=True)

            # Fill missing NumberOfDependents with mode (most common value)
            self.df['NumberOfDependents'].fillna(self.df['NumberOfDependents'].mode()[0], inplace=True)

            self.logging.info("Missing values handled successfully.")
        except Exception as e:
            self.logging.error("Error in handling missing values: %s", e)
            raise

    # def normalize_numerical_features(self):
    #     self.logging.info("Normalizing numerical features...")
    #     try:
    #         numerical_features = [
    #             'RevolvingUtilizationOfUnsecuredLines', 'age', 'DebtRatio', 'MonthlyIncome',
    #             'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate', 'NumberRealEstateLoansOrLines',
    #             'NumberOfTime30-59DaysPastDueNotWorse', 'NumberOfTime60-89DaysPastDueNotWorse', 'NumberOfDependents'
    #         ]
            
    #         # Apply StandardScaler
    #         self.df[numerical_features] = self.scaler.fit_transform(self.df[numerical_features])

    #         self.logging.info("Numerical features normalized successfully.")
    #     except Exception as e:
    #         self.logging.error("Error in normalizing numerical features: %s", e)
    #         raise
    from sklearn.preprocessing import MinMaxScaler

    def normalize_numerical_features(self):
        self.logging.info("Normalizing numerical features using MinMaxScaler...")
        try:
            numerical_features = [
                'RevolvingUtilizationOfUnsecuredLines', 'age', 'DebtRatio', 'MonthlyIncome',
                'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate', 'NumberRealEstateLoansOrLines',
                'NumberOfTime30-59DaysPastDueNotWorse', 'NumberOfTime60-89DaysPastDueNotWorse', 'NumberOfDependents'
            ]
    
            # Use MinMaxScaler to scale values between 0 and 1
            scaler = MinMaxScaler()
            self.df[numerical_features] = scaler.fit_transform(self.df[numerical_features])
    
            self.logging.info("Numerical features scaled successfully using MinMaxScaler.")
        except Exception as e:
            self.logging.error("Error in normalizing numerical features: %s", e)
            raise

    def feature_engineering(self):
        self.logging.info("Creating new features...")
        try:
            # Example Feature: Debt-to-Income Ratio (DebtRatio * MonthlyIncome)
            self.df['DebtToIncome'] = self.df['DebtRatio'] * self.df['MonthlyIncome']

            # Example Feature: Total Delinquency Count
            self.df['TotalLatePayments'] = (
                self.df['NumberOfTime30-59DaysPastDueNotWorse'] +
                self.df['NumberOfTime60-89DaysPastDueNotWorse'] +
                self.df['NumberOfTimes90DaysLate']
            )

            self.logging.info("New features created successfully.")
        except Exception as e:
            self.logging.error("Error in feature engineering: %s", e)
            raise

    def pipeline(self):
        self.logging.info("Starting the feature engineering pipeline...")
        try:
            self.handle_missing_values()
            self.normalize_numerical_features()
            self.feature_engineering()

            # Drop unnecessary columns (if required)
            cols_exclude = ['Unnamed: 0']
            self.df.drop(columns=[col for col in cols_exclude if col in self.df.columns], inplace=True)

            self.processed_df = self.df
            self.logging.info("Feature engineering pipeline executed successfully.")
        except Exception as e:
            self.logging.error("Error in the feature engineering pipeline: %s", e)
            raise

    def get_processed_data(self) -> pd.DataFrame:
        self.logging.info("Retrieving processed data...")
        if self.processed_df is None:
            self.logging.error("Data has not been processed. Run the pipeline() method first.")
            raise ValueError("Data has not been processed. Run the pipeline() method first.")
        self.logging.info("Processed data retrieved successfully.")
        return self.processed_df
