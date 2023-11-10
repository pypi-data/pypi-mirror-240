from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

__version__ = '0.1.0'


class WhiskerOutliers(BaseEstimator, TransformerMixin):

    def __init__(self, threshold=3.0, add_indicator=False):
        self.threshold = threshold
        self.indicator = add_indicator
        self.min_ = None
        self.max_ = None

    def fit(self, X, y=None):
        """
        Fit the instance on X.
        :param X: array-like shape of (n_samples, n_features)
        :param y: ignored
        :return: The fitted WhiskerOutliers instance
        """
        # calculate quantiles
        if isinstance(X, (pd.Series, pd.DataFrame)):
            q1 = X.quantile(0.25)
            q3 = X.quantile(0.75)
        else:  # elif isinstance(X, np.ndarray):
            q1 = np.quantile(X, q=0.25, axis=0)
            q3 = np.quantile(X, q=0.75, axis=0)
        # else:
        #     raise TypeError('X must be pandas.Series, pandas.DataFrame o numpy.array')

        # calculate iqr
        iqr = abs(q3 - q1)

        # calculate and retain the minimum and maximum limits of valid data
        self.min_ = q1 - (iqr * self.threshold)
        self.max_ = q3 + (iqr * self.threshold)

        return self

    def transform(self, X, y=None):
        """
        Replace the outlier values by numpy.nan using the limits identified by the `fit` method.
        :param X: array-like shape of (n_samples, n_features)
        :param y: ignored
        :return: The dataset where the outliers has been removed.
        """
        # procedure when the outlier indicator is not required
        if not self.indicator:
            if isinstance(X, (pd.Series, pd.DataFrame)):
                return X.mask(X < self.min_, np.nan).mask(X > self.max_, np.nan)
            else:  # elif isinstance(X, np.ndarray):
                return np.where(X > self.max_, np.nan, np.where(X < self.min_, np.nan, X))

        # procedure when the outlier indicator is required
        else:  # self.add_indicator
            if isinstance(X, pd.DataFrame):
                return (X.mask(X < self.min_, np.nan).mask(X > self.max_, np.nan)) \
                    .merge((pd.DataFrame(data=0, columns=X.columns, index=X.index))
                           .mask(X < self.min_, -1).mask(X > self.max_, 1),
                           how='inner', left_index=True, right_index=True, suffixes=('', '_outlier')
                           )
            elif isinstance(X, pd.Series):
                return (pd.DataFrame(X.mask(X < self.min_, np.nan).mask(X > self.max_, np.nan))) \
                    .merge((pd.DataFrame(data=0, columns=[X.name], index=X.index))
                           .mask(X < self.min_, -1).mask(X > self.max_, 1),
                           how='inner', left_index=True, right_index=True, suffixes=('', '_outlier')
                           )
            else:  # elif isinstance(X, np.ndarray):
                return np.c_[
                    np.where(X > self.max_, np.nan, np.where(X < self.min_, np.nan, X)),
                    np.where(X > self.max_, 1, np.where(X < self.min_, -1, 0))
                ]

    def fit_transform(self, X, y=None):
        """
        Fit to data, then transform it.
        :param X: array-like of shape (n_samples, n_features)
        :param y: ignored
        :return: The transformed dataset.
        """
        self.fit(X)
        return self.transform(X)

    def get_params(self, deep=True):
        """
        Returns a dictionary with the parameters used in the instance.
        :param deep: bool, indicates if deep copy is required.
        :return: dict
        """
        return {'threshold': self.threshold,
                'add_indicator': self.indicator}
