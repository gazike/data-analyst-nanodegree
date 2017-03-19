from matplotlib import pyplot as plt
import seaborn
import numpy as np
import pandas as pd


def count_nan(series: pd.Series):
    return series[series.isnull()].size


def nans_count_by_column(df: pd.DataFrame) -> pd.DataFrame:
    return df.apply(count_nan).to_frame().transpose()

