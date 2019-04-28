from data.data import generate_df
from model import filter_df, regression


def smooth_data(df):

    import numpy as np
    from scipy.interpolate import interp1d

    #smoothing actual data
    x = df['t']
    y = df['vol']

    x_smooth = np.linspace(x.min(),x.max(), 500)

    f = interp1d(x, y, kind='quadratic')
    y_smooth = f(x_smooth)

    return df


df = generate_df('data/roi.sql')

df = filter_df(df)

df = smooth_data(df)
