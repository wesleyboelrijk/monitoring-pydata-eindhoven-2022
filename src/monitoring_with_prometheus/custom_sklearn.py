import numpy as np
import pandas as pd
from sklearn import impute
from sklearn import preprocessing

from monitoring_with_prometheus.metrics import MODEL_CATEGORICAL, IMPUTED


def get_feature_names(X):
    if isinstance(X, pd.DataFrame):
        return X.columns
    else:
        return list(range(X.shape[1]))


class OneHotEncoder(preprocessing.OneHotEncoder):
    """OneHotEncoder that adds metrics to the prometheus metric registry"""

    def transform(self, X):
        """
        Transform method that adds the count for each category in each feature to the prometheus
        metric registry
        """
        transformed_X = super().transform(X)
        features = get_feature_names(X)

        # Use inverse method on transformed_X to get all missing values back as 'None'
        categories = self.inverse_transform(transformed_X)

        for idx, row in enumerate(categories.T):
            for category in row:
                if category is None:
                    category = "missing"
                MODEL_CATEGORICAL.labels(feature=str(features[idx]), category=str(category)).inc()
        return transformed_X


class SimpleImputer(impute.SimpleImputer):
    """SimpleImputer that adds metrics to the prometheus metric registry"""

    def transform(self, X):
        """Transform methods that increment counter when missing data is imputed"""
        features = get_feature_names(X)

        missing = np.isnan(X).sum(axis=0)
        for idx, feature in enumerate(features):
            IMPUTED.labels(feature=feature, method="SimpleImputer").inc(missing[idx])

        return super().transform(X)
