__author__ = "Yarik Menchaca Resendiz"

import pandas as pd


def drawdown(return_series: pd.Series, investment: float = 1) -> pd.DataFrame:
    """
    Takes a time series of assets returns and computes: The wealth index,
    the previous peaks, and percent drawdowns
    :param return_series: percentage of returns (e.g 0.1, 0.08, -0.01)
        equivalent to (10% return 1st period, 8% 2nd and -1% 3rd)
    :param investment: amount of money invest
    :return: DataFrame that contains: wealth index,
    the previous peaks, and percent drawdowns
    """

    wealth_index = investment*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdown_series = (wealth_index - previous_peaks)/previous_peaks
    return pd.DataFrame({"Wealth": wealth_index, "Peaks": previous_peaks,
                         "Drawdown": drawdown_series})
