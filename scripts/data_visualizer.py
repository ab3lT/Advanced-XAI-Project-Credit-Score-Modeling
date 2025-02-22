import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataVisualizer:
    """
    A class to visualize distributions and relationships in a dataset for exploratory data analysis (EDA).
    """

    def __init__(self, data_df, numerical_features, categorical_features, target_col, logger):
        """
        Initializes the DataVisualizer with a dataset, feature lists, a target column, and a logger.
        """
        self.data_df = data_df
        self.numerical_features = numerical_features
        self.categorical_features = categorical_features
        self.target_col = target_col
        self.logger = logger

    def plot_histograms(self):
        """
        Plots histograms for the numerical features in the dataset.
        """
        self.logger.info("Plotting histograms for numerical features.")
        self.data_df[self.numerical_features].hist(figsize=(12, 8), bins=30, edgecolor="black")
        plt.suptitle("Histograms of Numerical Features", fontsize=14)
        plt.show()

    def plot_categorical_counts(self):
        """
        Plots count plots for the categorical features in the dataset.
        """
        self.logger.info("Plotting categorical count distributions.")
        plt.figure(figsize=(10, 4))
        for i, feature in enumerate(self.categorical_features, 1):
            plt.subplot(1, len(self.categorical_features), i)
            sns.countplot(data=self.data_df, x=feature, palette="coolwarm")
            plt.title(f'Distribution of {feature}')
            plt.xlabel(feature)
            plt.ylabel('Count')
        plt.tight_layout()
        plt.show()

    def plot_boxplots(self):
        """
        Plots boxplots for numerical features to detect outliers.
        """
        self.logger.info("Plotting boxplots for numerical features.")
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.data_df[self.numerical_features])
        plt.xticks(rotation=90)
        plt.title("Boxplot of Numerical Features")
        plt.show()

    def plot_correlation_heatmap(self):
        """
        Displays a heatmap of the correlation matrix.
        """
        self.logger.info("Plotting correlation heatmap.")
        plt.figure(figsize=(10, 8))
        corr = self.data_df[self.numerical_features].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Correlation Heatmap of Numerical Features")
        plt.show()

    def plot_pairwise_relationships(self):
        """
        Plots pairwise relationships among numerical features.
        """
        self.logger.info("Plotting pairwise relationships.")
        sns.pairplot(self.data_df, vars=self.numerical_features, hue=self.target_col, palette='husl', plot_kws={'alpha': 0.6})
        plt.suptitle('Pair Plot of Numerical Features by Class', y=1.02)
        plt.show()
