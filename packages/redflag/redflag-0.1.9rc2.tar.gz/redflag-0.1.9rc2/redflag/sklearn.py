"""
Scikit-learn components.

Author: Matt Hall, agilescientific.com
Licence: Apache 2.0

Copyright 2022 Agile Scientific

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import warnings
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils import check_array
from sklearn.pipeline import Pipeline
from sklearn.covariance import EllipticEnvelope
from scipy.stats import wasserstein_distance
from scipy.stats import cumfreq

from .utils import is_clipped, proportion_to_stdev, stdev_to_proportion
from .target import is_continuous
from .independence import is_correlated
from .outliers import has_outliers, expected_outliers
from .imbalance import imbalance_degree, imbalance_ratio, minority_classes


def formatwarning(message, *args, **kwargs):
    """
    A custom warning format function.
    """
    return f"{message}\n"

warnings.formatwarning = formatwarning


class BaseRedflagDetector(BaseEstimator, TransformerMixin):

    def __init__(self, func, warning, **kwargs):
        self.func = lambda X: func(X, **kwargs)
        self.warning = warning

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        """
        Checks X (and y, if it is continuous data) for suspect values.
        """
        X = check_array(X)

        positive = [i for i, feature in enumerate(X.T) if self.func(feature)]
        if n := len(positive):
            pos = ', '.join(str(i) for i in positive)
            warnings.warn(f"🚩 Feature{'s' if n > 1 else ''} {pos} may have {self.warning}.")

        if (y is not None) and is_continuous(y):
            if np.asarray(y).ndim == 1:
                y_ = y.reshape(-1, 1)
            for i, target in enumerate(y_.T):
                if self.func(target):
                    warnings.warn(f"🚩 Target {i} may have {self.warning}.")

        return X


class ClipDetector(BaseRedflagDetector):
    """
    Transformer that detects features with clipped values.

    Example:
        >>> from sklearn.pipeline import make_pipeline
        >>> pipe = make_pipeline(ClipDetector())
        >>> X = np.array([[2, 1], [3, 2], [4, 3], [5, 3]])
        >>> pipe.fit_transform(X)  # doctest: +SKIP
        redflag/sklearn.py::redflag.sklearn.ClipDetector
          🚩 Feature 1 may have clipped values.
        array([[2, 1],
               [3, 2],
               [4, 3],
               [5, 3]])
    """
    def __init__(self):
        super().__init__(is_clipped, "clipped values")


class CorrelationDetector(BaseRedflagDetector):
    """
    Transformer that detects features correlated to themselves.

    Example:
        >>> from sklearn.pipeline import make_pipeline
        >>> pipe = make_pipeline(CorrelationDetector())
        >>> rng = np.random.default_rng(0)
        >>> X = np.stack([rng.uniform(size=20), np.sin(np.linspace(0, 1, 20))]).T
        >>> pipe.fit_transform(X)  # doctest: +SKIP
        redflag/sklearn.py::redflag.sklearn.CorrelationDetector
          🚩 Feature 1 may have correlated values.
        array([[0.38077051, 0.        ],
               [0.42977406, 0.05260728]
               ...
               [0.92571458, 0.81188195],
               [0.7482485 , 0.84147098]])
    """
    def __init__(self):
        super().__init__(is_correlated, "correlated values")


class UnivariateOutlierDetector(BaseRedflagDetector):
    """
    Transformer that detects if there are more than the expected number of
    outliers in each feature considered separately. (To consider all features
    together, use the `OutlierDetector` instead.)

    **kwargs are passed to `has_outliers`.

    Example:
        >>> from sklearn.pipeline import make_pipeline
        >>> pipe = make_pipeline(UnivariateOutlierDetector())
        >>> rng = np.random.default_rng(0)
        >>> X = rng.normal(size=(1_000, 2))
        >>> pipe.fit_transform(X)  # doctest: +SKIP
        redflag/sklearn.py::redflag.sklearn.UnivariateOutlierDetector
          🚩 Features 0, 1 may have more outliers (in a univariate sense) than expected.
        array([[ 0.12573022, -0.13210486],
               [ 0.64042265,  0.10490012],
               [-0.53566937,  0.36159505],
               ...,
               [ 1.24972527,  0.75063397],
               [-0.55581573, -2.01881162],
               [-0.90942756,  0.36922933]])
        >>> pipe = make_pipeline(UnivariateOutlierDetector(factor=2))
        >>> pipe.fit_transform(X)  # No warning.
        array([[ 0.12573022, -0.13210486],
               [ 0.64042265,  0.10490012],
               [-0.53566937,  0.36159505],
               ...,
               [ 1.24972527,  0.75063397],
               [-0.55581573, -2.01881162],
               [-0.90942756,  0.36922933]])
    """
    def __init__(self, **kwargs):
        super().__init__(has_outliers, "more outliers (in a univariate sense) than expected", **kwargs)


class MultivariateOutlierDetector(BaseEstimator, TransformerMixin):
    """
    Transformer that detects if there are more than the expected number of
    outliers when the dataset is considered as a whole, in a mutlivariate
    sense. (To consider feature distributions separately, use the
    `UnivariateOutlierDetector` instead.)

    Example:
        >>> from sklearn.pipeline import make_pipeline
        >>> pipe = make_pipeline(MultivariateOutlierDetector())
        >>> rng = np.random.default_rng(0)
        >>> X = rng.normal(size=(1_000, 2))
        >>> pipe.fit_transform(X)  # doctest: +SKIP
        redflag/sklearn.py::redflag.sklearn.MultivariateOutlierDetector
          🚩 Dataset may have more outliers (in a multivariate sense) than expected.
        array([[ 0.12573022, -0.13210486],
               [ 0.64042265,  0.10490012],
               [-0.53566937,  0.36159505],
               ...,
               [ 1.24972527,  0.75063397],
               [-0.55581573, -2.01881162],
               [-0.90942756,  0.36922933]])
        >>> pipe = make_pipeline(MultivariateOutlierDetector(factor=2))
        >>> pipe.fit_transform(X)  # No warning.
        array([[ 0.12573022, -0.13210486],
               [ 0.64042265,  0.10490012],
               [-0.53566937,  0.36159505],
               ...,
               [ 1.24972527,  0.75063397],
               [-0.55581573, -2.01881162],
               [-0.90942756,  0.36922933]])
    """
    def __init__(self, p=0.99, threshold=None, factor=1):
        self.p = p if threshold is None else None
        self.threshold = threshold
        self.factor = factor

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        """
        Checks X (and y, if it is continuous data) for outlier values.
        """
        X = check_array(X)

        if X.shape[1] < 2:
            warnings.warn("MultiVariateOutlierDetector requires at least 2 features; use UnivariateOutlierDetector on this dataset.")
            return X

        outliers = has_outliers(X, p=self.p, threshold=self.threshold, factor=self.factor)

        if outliers:
            warnings.warn(f"🚩 Dataset may have more outliers (in a multivariate sense) than expected.")

        if (y is not None) and is_continuous(y):
            if np.asarray(y).ndim == 1:
                y_ = y.reshape(-1, 1)
            if has_outliers(y_, p=self.p, threshold=self.threshold, factor=self.factor):
                    warnings.warn(f"🚩 Target may have more outliers (in a multivariate sense) than expected.")

        return X


class DistributionComparator(BaseEstimator, TransformerMixin):
    """
    Transformer that raises warnings if validation or prediction data is not
    in the same distribution as the training data.

    Methods:
        fit_transform(): Called when fitting. In this transformer, we don't
            transform the data, we just learn the distributions.
        transform(): Called when transforming validation or prediction data.
        fit(): Called by fit_transform() when fitting the training data.
    """

    def __init__(self, threshold=1.0, bins=200, warn=True, warn_if_zero=False):
        """
        Constructor for the class.

        Args:
            threshold (float): The threshold for the Wasserstein distance.
            bins (int): The number of bins to use when computing the histograms.
            warn (bool): Whether to raise a warning or raise an error.
            warn_if_zero (bool): Whether to raise a warning if the histogram is
                identical to the training data.
        """
        self.threshold = threshold
        self.bins = bins
        self.warn = warn
        self.warn_if_zero = warn_if_zero

    def fit(self, X, y=None):
        """
        Record the histograms of the input data, using 200 bins by default.
       
        Normally we'd compute Wasserstein distance directly from the data, 
        but that seems memory-expensive.

        Args:
            X (np.ndarray): The data to learn the distributions from.
            y (np.ndarray): The labels for the data. Not used for anything.

        Returns:
            self.
        """
        X = check_array(X)
        hists = [cumfreq(feature, numbins=self.bins) for feature in X.T]
        self.hist_counts = [h.cumcount for h in hists]
        self.hist_lowerlimits = [h.lowerlimit for h in hists]
        self.hist_binsizes = [h.binsize for h in hists]
        return self

    def transform(self, X, y=None):
        """
        Compare the histograms of the input data X to the histograms of the
        training data. We use the Wasserstein distance to compare the
        distributions.

        This transformer does not transform the data, it just compares the
        distributions and raises a warning if the Wasserstein distance is
        above the threshold.

        Args:
            X (np.ndarray): The data to compare to the training data.
            y (np.ndarray): The labels for the data. Not used for anything.

        Returns:
            X.
        """
        X = check_array(X)
        
        # If there aren't enough samples, just return X.
        # training_examples = self.hist_counts[0][-1]
        if len(X) <  100:
            return X

        # If we have enough samples, let's carry on.
        wasserstein_distances = []
        for i, (weights, lowerlimit, binsize, feature) in enumerate(zip(self.hist_counts, self.hist_lowerlimits, self.hist_binsizes, X.T)):

            values = lowerlimit + np.linspace(0, binsize*weights.size, weights.size)
            
            hist = cumfreq(feature, numbins=self.bins)
            f_weights = hist.cumcount
            f_values = hist.lowerlimit + np.linspace(0, hist.binsize*f_weights.size, f_weights.size)

            w = wasserstein_distance(values, f_values, weights, f_weights)
            wasserstein_distances.append(w)

        zeros = np.where(np.array(wasserstein_distances)==0)[0]
        if n := zeros.size and self.warn_if_zero:
            warnings.warn(f"🚩 Feature{'s' if n > 1 else ''} {pos} {'are' if n > 1 else 'is'} identical to the training data.")

        positive = np.where(np.array(wasserstein_distances) > self.threshold)[0]
        if n := positive.size:
            pos = ', '.join(str(i) for i in positive)
            if self.warn:
                warnings.warn(f"🚩 Feature{'s' if n > 1 else ''} {pos} {'have distributions that are' if n > 1 else 'has a distribution that is'} different from training.")
            else:
                raise ValueError(f"🚩 Feature{'s' if n > 1 else ''} {pos} {'have distributions that are' if n > 1 else 'has a distribution that is'} different from training.")

        return X
    
    def fit_transform(self, X, y=None):
        """
        This is called when fitting, if it is present. We can make our call to self.fit()
        and not bother calling self.transform(), because we're not actually transforming
        anything, we're just getting set up for applying our test later during prediction.

        Args:
            X (np.ndarray): The data to compare to the training data.
            y (np.ndarray): The labels for the data. Not used for anything.

        Returns:
            X.
        """
        # Call fit() to learn the distributions.
        self = self.fit(X, y=y)
        
        # When fitting, we do not run transform() (actually a test).
        return X


class OutlierDetector(BaseEstimator, TransformerMixin):
    """
    Transformer that raises warnings if data has more outliers than expected
    for the size and dimensionality of dataset. The data are considered in a
    multivariate sense.

    Methods:
        fit_transform(): Called when fitting. In this transformer, we don't
            transform the data, we just learn the distribution's properties.
        transform(): Called when transforming validation or prediction data.
        fit(): Called by fit_transform() when fitting the training data.
    """
    def __init__(self, p=0.99, threshold=None, factor=1.0):
        """
        Constructor for the class.

        Args:
            p (float): The confidence level.
            threshold (float): The threshold for the Wasserstein distance.
        """
        self.threshold = threshold
        self.p = p if threshold is None else None
        self.factor = factor

    def _actual_vs_expected(self, z, n, d):
        """
        Calculate the expected number of outliers in the data.
        """
        # Calculate the Mahalanobis distance threshold if necessary.
        if self.threshold is None:
            self.threshold = proportion_to_stdev(p=self.p, d=d)
        else:
            self.p = stdev_to_proportion(self.threshold, d=d)

        # Decide whether each point is an outlier or not.
        idx, = np.where((z < -self.threshold) | (z > self.threshold))

        # Calculate the expected number of outliers in the training data.
        expected = int(self.factor * expected_outliers(n, d, threshold=self.threshold))

        # If the number of outliers is greater than the expected number, raise a warning.
        return idx.size, expected

    def fit(self, X, y=None):
        """
        Record the robust location and covariance.

        Args:
            X (np.ndarray): The data to learn the distributions from.
            y (np.ndarray): The labels for the data. Not used for anything.

        Returns:
            self.
        """
        X = check_array(X)
        n, d = X.shape

        # Fit the distributions.
        self.ee = EllipticEnvelope(support_fraction=1.0).fit(X)

        # Compute the Mahalanobis distance of the training data.
        z = np.sqrt(self.ee.dist_)

        actual, expected = self._actual_vs_expected(z, n, d)
        if actual > expected:
            warnings.warn(f"🚩 There are more outliers than expected in the training data ({actual} vs {expected}).")

        return self


    def transform(self, X, y=None):
        """
        Compute the Mahalanobis distances using the location and covarianced
        learned from the training data.

        This transformer does not transform the data, it just compares the
        distributions and raises a warning if there are more outliers than
        expected, given the confidence level or threshold specified at
        instantiation.

        Args:
            X (np.ndarray): The data to compare to the training data.
            y (np.ndarray): The labels for the data. Not used for anything.

        Returns:
            X.
        """
        X = check_array(X)
        n, d = X.shape

        # Compute the Mahalanobis distances for the given data, using the
        # learned location and covariance.
        z = np.sqrt(self.ee.mahalanobis(X))

        actual, expected = self._actual_vs_expected(z, n, d)
        if actual > expected:
            warnings.warn(f"🚩 There are more outliers than expected in the data ({actual} vs {expected}).")

        return X

    def fit_transform(self, X, y=None):
        """
        This is called when fitting, if it is present. We can make our call to self.fit()
        and not bother calling self.transform(), because we're not actually transforming
        anything, we're just getting set up for applying our test later during prediction.
        The warning about outliers in the data will come from self.fit().

        Args:
            X (np.ndarray): The data to compare to the training data.
            y (np.ndarray): The labels for the data. Not used for anything.

        Returns:
            X.
        """
        self = self.fit(X, y=y)
        
        # When fitting, we do not run transform().
        return X


class ImbalanceDetector(BaseEstimator, TransformerMixin):

    def __init__(self, method='id', threshold=0.4, classes=None):
        """
        Constructor for the class.

        Args:
            method (str): The method to use for imbalance detection. In general,
                'id' is the best method for multi-class classification problems
                (but can be used for binary classification problems as well).
            threshold (float): The threshold for the imbalance, default 0.5.
                For 'id', the imbalance summary statistic is in [0, 1). See
                Ortigosa-Hernandez et al. (2017) for details. For 'ir', the
                threshold is a ratio of the majority class to the minority class
                and ranges from 1 (balanced) to infinity (nothing in the
                minority class).
            classes (list): The names of the classes present in the data, even
                if they are not present in the array `y`.
        """
        if method not in ['id', 'ir']:
            raise ValueError(f"Method must be 'id' or 'ir' but was {method}")

        if (method == 'ir') and (threshold <= 1):
            raise ValueError(f"Method is 'ir' but threshold <= 1. For IR, the measure is the ratio of the majority class to the minority class; for example use 2 to trigger a warning if there are twice as many samples in the majority class as in the minority class.")

        if (method == 'id') and (threshold >= 1):
            raise ValueError(f"Method is 'id' but threshold >= 1. For ID, the measure is always in [0, 1).")

        self.method = method
        self.threshold = threshold
        self.classes = classes

    def fit(self, X, y=None):

        # If there's no target or y is continuous (probably a regression), we're done.
        if y is None or is_continuous(y):
            warnings.warn("Target y is None or seems continuous, so no imbalance detection.")
            return self

        methods = {'id': imbalance_degree, 'ir': imbalance_ratio}
        imbalance = methods[self.method](y)
        
        if self.method == 'id':
            imbalance = imbalance - int(imbalance)

        min_classes = minority_classes(y, classes=self.classes)

        imbalanced = (len(min_classes) > 0) and (imbalance > self.threshold)

        if imbalanced and self.method == 'id':
            warnings.warn(f"🚩 The labels are imbalanced by more than the threshold ({imbalance:0.3f} > {self.threshold:0.3f}).")
        if imbalanced and self.method == 'ir':
            warnings.warn(f"🚩 The labels are imbalanced by more than the threshold ({imbalance:0.1f} > {self.threshold:0.1f}).")

        return self

    def transform(self, X, y=None):
        """
        Checks y for imbalance.
        """
        return check_array(X)


pipeline = Pipeline(
    steps=[
        ("rf.imbalance", ImbalanceDetector()),
        ("rf.clip", ClipDetector()),
        ("rf.correlation", CorrelationDetector()),
        ("rf.outlier", OutlierDetector()),
        ("rf.distributions", DistributionComparator()),
    ]
)
