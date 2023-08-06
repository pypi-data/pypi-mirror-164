"""Test redflag"""
import pytest
import numpy as np
from sklearn.pipeline import make_pipeline

import redflag as rf

"""
NB Most of redflag is tested by its doctests, but doctest cannot test
   for warnings. Most of the tests in this file are of the sklearn API.
"""

def test_clip_detector():
    """
    Checks for clipped data. Detects clipping by looking for multiple values
    of max and/or min.
    """
    pipe = make_pipeline(rf.ClipDetector())
    X = np.array([[2, 1], [3, 2], [4, 3], [5, 3]])
    with pytest.warns(UserWarning, match="Feature 1 may have clipped values."):
        pipe.fit_transform(X)

    # Does not warn:
    X = np.array([[2, 1], [3, 2], [4, 3], [5, 4]])
    pipe.fit_transform(X)


def test_correlation_detector():
    """
    Checks for data which is correlated to itself.
    """
    pipe = make_pipeline(rf.CorrelationDetector())
    rng = np.random.default_rng(0)
    X = np.stack([rng.uniform(size=20), np.sin(np.linspace(0, 1, 20))]).T
    with pytest.warns(UserWarning, match="Feature 1 may have correlated values."):
        pipe.fit_transform(X)


def test_distribution_comparator():
    """
    Checks that the distribution of test data (i.e. transformed only) is the
    same as the distribution of the training data (i.e. fit and transformed).
    """
    pipe = make_pipeline(rf.DistributionComparator(threshold=0.5))
    rng = np.random.default_rng(0)
    X = rng.normal(size=(1_000, 2))
    pipe.fit_transform(X)  # fit() never throws a warning, just learns the distribution.

    # Throws a warning on test data (tested against training statistics):
    X_test = 1 + rng.normal(size=(500, 2))
    with pytest.warns(UserWarning, match="Features 0, 1 have distributions that are different from training."):
        pipe.transform(X_test)

    # Does not warn if distribution is the same:
    X_test = rng.normal(size=(500, 2))
    pipe.fit_transform(X)


def test_univariate_outlier_detector():
    # Use a factor of 0.5 to almost guarantee that this will throw a warning.
    pipe = make_pipeline(rf.UnivariateOutlierDetector(factor=0.5))
    rng = np.random.default_rng(0)
    X = rng.normal(size=1_000).reshape(-1, 1)
    with pytest.warns(UserWarning, match="Feature 0 may have more outliers"):
        pipe.fit_transform(X)

    # Does not warn with factor of 2.5:
    pipe = make_pipeline(rf.UnivariateOutlierDetector(factor=2.5))
    pipe.fit_transform(X)


def test_multivariate_outlier_detector():
    # Use a factor of 0.5 to almost guarantee that this will throw a warning.
    pipe = make_pipeline(rf.MultivariateOutlierDetector(factor=0.5))
    rng = np.random.default_rng(0)
    X = rng.normal(size=(1_000, 2))
    with pytest.warns(UserWarning, match="Dataset may have more outliers"):
        pipe.fit_transform(X)

    # Does not warn with factor of 2.5:
    pipe = make_pipeline(rf.MultivariateOutlierDetector(factor=2.5))
    pipe.fit_transform(X)


def test_outlier_detector():
    # Use a factor of 0.5 to almost guarantee that this will throw a warning.
    pipe = make_pipeline(rf.OutlierDetector(factor=0.5))
    rng = np.random.default_rng(0)
    X = rng.normal(size=(1_000, 2))
    with pytest.warns(UserWarning, match="There are more outliers than expected in the training data"):
        pipe.fit_transform(X)

    # Throws a warning on test data (tested against training statistics):
    X_test = rng.normal(size=(500, 2))
    with pytest.warns(UserWarning, match="There are more outliers than expected in the data"):
        pipe.transform(X_test)

    # Does not warn with factor of 2:
    pipe = make_pipeline(rf.OutlierDetector(factor=2.0))
    pipe.fit_transform(X)


def test_imbalance_detector():
    pipe = make_pipeline(rf.ImbalanceDetector())
    rng = np.random.default_rng(0)
    X = rng.normal(size=(100, 1))
    y = rf.generate_data([20, 80])
    with pytest.warns(UserWarning, match="The labels are imbalanced"):
        pipe.fit_transform(X, y)

    # Check other method.
    pipe = make_pipeline(rf.ImbalanceDetector(method='ir', threshold=2))
    with pytest.warns(UserWarning, match="The labels are imbalanced"):
        pipe.fit_transform(X, y)

    # Does not warn with higher threshold (summary statistic for this y is 0.6):
    pipe = make_pipeline(rf.ImbalanceDetector(threshold=0.7))
    pipe.fit_transform(X, y)

    # Warns about wrong kind of y:
    y = rng.normal(size=100)
    with pytest.warns(UserWarning, match="Target y is None or seems continuous"):
        pipe.fit_transform(X, y)

    # Raises error because method doesn't exist:
    with pytest.raises(ValueError) as e:
        pipe = make_pipeline(rf.ImbalanceDetector(method='foo'))

    # Raises error because threshold is wrong.
    with pytest.raises(ValueError) as e:
        pipe = make_pipeline(rf.ImbalanceDetector(method='ir', threshold=0.5))

    # Raises error because threshold is wrong.
    with pytest.raises(ValueError) as e:
        pipe = make_pipeline(rf.ImbalanceDetector(method='id', threshold=2))
