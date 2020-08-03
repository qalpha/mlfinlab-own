"""
Matrix Flag labeling method.
"""


class MatrixFlagLabels:
    """
    The Matrix Flag labeling method is featured in the paper: Cervelló-Royo, R., Guijarro, F. and Michniuk, K., 2015.
    Stock market trading rule based on pattern recognition and technical analysis: Forecasting the DJIA index with
    intraday data.

    The method of applying a matrix template was first introduced, and explained in greater detail, in the paper:
    Leigh, W., Modani, N., Purvis, R. and Roberts, T., 2002. Stock market trading rule discovery using technical
    charting heuristics.

    Cervelló-Royo et al. expand on Leigh et al.'s work by proposing a new bull flag pattern which ameliorates some
    weaknesses in Leigh's original template. Additionally, he applies this bull flag labeling method to intraday
    candlestick data, rather than just closing prices.

    To find the total weight for a given day, the current price as well as the preceding window days number of prices is
    used. The data window is split into 10 buckets each containing a chronological tenth of the data window. Each point
    in 1 bucket is put into a decile corresponding to a position in a column based on percentile relative to the entire
    data window. Bottom 10% on lowest row, next 10% on second lowest row etc.
    The proportion of points in each decile is reported to finalize the column. The first tenth of the data is
    transformed to the leftmost column, the next tenth to the next column on the right and so on until finally a 10 by
    10 matrix is achieved. This matrix is then multiplied element-wise with the 10 by 10 template, and the sum of all
    columns is the total weight for the day. If desired, the user can specify a threshold to determine positive and
    negative classes. The value of the threshold depends on how strict of a classifier the user desires, and the
    allowable values based on the template matrix.
    """

    def __init__(self, prices, window, template_name=None):
        """
        :param prices: (pd.Series) Price data for one stock.
        :param window: (int) Length of preceding data window used when generating the fit matrix for one day.
        :param template_name: (str) Name of the an available template in the template library. Allowable names:
                            ``leigh_bear``, ``leigh_bull``, ``cervelloroyo_bear``, ``cervellororo_bull``.
        """
        pass

    def set_template(self, template):
        """
        :param template: (pd.DataFrame) Template to override the default template. Must be a 10 by 10 pd.DataFrame.
                            NaN values not allowed, as they will not automatically be treated as zeros.
        """
        pass

    def apply_labeling_matrix(self, threshold=None):
        """
        :param threshold: (float) If None, labels will be returned numerically as the score for the day. If not None,
                        then labels are returned categorically, with the positive category for labels that are equal to
                        or exceed the threshold.
        :return: (pd.Series) Total scores for the data series on each eligible day (meaning for indices self.window and
                    onwards).
        """
        pass
