"""
Optimal Number of Clusters (ONC Algorithm)
Detection of False Investment Strategies using Unsupervised Learning Methods
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3167017
"""


def cluster_kmeans_top(corr_mat: pd.DataFrame, repeat: int = 10) -> Union[pd.DataFrame, dict, pd.Series, bool]:
    """
    Improve the initial clustering by leaving clusters with high scores unchanged and modifying clusters with
    below average scores.

    :param corr_mat: (pd.DataFrame) Correlation matrix
    :param repeat: (int) Number of clustering algorithm repetitions.
    :return: (tuple) [correlation matrix, optimized clusters, silh scores, boolean to rerun ONC]
    """
    pass


def get_onc_clusters(corr_mat: pd.DataFrame, repeat: int = 10) -> Union[pd.DataFrame, dict, pd.Series]:
    """
    Optimal Number of Clusters (ONC) algorithm described in the following paper:
    `Marcos Lopez de Prado, Michael J. Lewis, Detection of False Investment Strategies Using Unsupervised
    Learning Methods, 2015 <https://papers.ssrn.com/sol3/abstract_id=3167017>`_;
    The code is based on the code provided by the authors of the paper.

    The algorithm searches for the optimal number of clusters using the correlation matrix of elements as an input.

    The correlation matrix is transformed to a matrix of distances, the K-Means algorithm is applied multiple times
    with a different number of clusters to use. The results are evaluated on the t-statistics of the silhouette scores.

    The output of the algorithm is the reordered correlation matrix (clustered elements are placed close to each other),
    optimal clustering, and silhouette scores.

    :param corr_mat: (pd.DataFrame) Correlation matrix of features
    :param repeat: (int) Number of clustering algorithm repetitions
    :return: (tuple) [correlation matrix, optimized clusters, silh scores]
    """

    pass
