from data.data import generate_df


def filter_df(roi):
    '''Inputs a datafram and applies various filters and sorts input dataframe and returns the new dataframe'''

    roi['wk'] = roi['wk'].astype('int')

    roi = roi.sort_values('wk', ascending=True).reset_index()

    del roi['index']

    roi['t'] = roi.index + 1

    return roi


def regression(df):
    '''Inputs a dataframe, runs a linear regression and returns a new datafram with predictions'''

    import statsmodels.formula.api as sm
    from scipy import stats
    import pandas as pd
    import numpy as np

    df = filter_df(df)

    #regression
    regression = sm.ols(formula="vol ~ t", data=df).fit()

    #prediction dataframe
    predict = pd.DataFrame({'t': range(1,53)})

    #setting varibales based on regression output
    intercept = regression.params.Intercept
    slope = regression.params.t
    se_regression = np.sqrt(regression.scale)
    observations = regression.nobs
    avg = np.mean(predict['t'])
    stdev = np.std(predict['t'])
    df_residual = regression.df_resid
    t_crit = stats.t.ppf(1-.025, df_residual)

    #creating prediction column in dataframe
    predict['prediction'] = (intercept + predict['t']*slope)

    #Creating columns for upper and lower bound of the prediciton based on 95% confidence interval
    predict['SE_of_prediction'] = se_regression*(np.sqrt(1+(1/observations)+((predict['t']-avg)**2)/((stdev**2)*(observations-1))))

    predict['margin_of_error'] = predict['SE_of_prediction'] * t_crit

    predict['Lower Bound'] = predict['prediction'] - predict['margin_of_error']
    predict['Upper Bound'] = predict['prediction'] + predict['margin_of_error']

    #show regression results in terminal
    print(regression.summary())

    return predict
