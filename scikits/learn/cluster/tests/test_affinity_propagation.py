"""
Testing for Clustering methods

"""

import numpy as np
from numpy.testing import assert_equal, assert_array_equal

from ..affinity_propagation_ import AffinityPropagation, \
                        affinity_propagation
from .common import generate_clustered_data


n_clusters = 3
X = generate_clustered_data(n_clusters=n_clusters)


def test_affinity_propagation():
    """
    Affinity Propagation algorithm

    """
    # Compute similarities
    X_norms = np.sum(X*X, axis=1)
    S = - X_norms[:, np.newaxis] - X_norms[np.newaxis, :] + 2 * np.dot(X, X.T)
    p = 10*np.median(S)

    # Compute Affinity Propagation
    cluster_centers_indices, labels = affinity_propagation(S, p)

    n_clusters_ = len(cluster_centers_indices)

    assert_equal(n_clusters, n_clusters_)

    af = AffinityPropagation()
    labels = af.fit(S, p).labels_
    cluster_centers_indices = af.cluster_centers_indices_

    n_clusters_ = len(cluster_centers_indices)
    assert_equal(np.unique(labels).size, n_clusters_)
    assert_equal(n_clusters, n_clusters_)

    # Test also with no copy
    _, labels_no_copy = affinity_propagation(S, p, copy=False)
    assert_array_equal(labels, labels_no_copy)
