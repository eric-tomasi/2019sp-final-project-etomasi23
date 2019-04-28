from model import filter_df, regression


def plot_trend(roi):
    '''Input a dataframe, smooth actual data, run regression and plot the predicted values'''

    import numpy as np
    from scipy.interpolate import interp1d

    #smoothing actual data
    x = roi['t']
    y = roi['vol']

    x_smooth = np.linspace(x.min(),x.max(), 500)

    f = interp1d(x, y, kind='quadratic')
    y_smooth = f(x_smooth)


    #input plotting libraries
    import matplotlib.pyplot as plt
    import seaborn as sns

    #generate predict dataframe
    predict = regression(roi)

    #set up figure and alter settings
    fig, ax1 = plt.subplots(figsize=(20,8.5))
    plt.rcParams.update({'font.size':14})
    sns.set()

    #plot smoothed actuals and regression with upper and lower bounds
    ax1.plot(x_smooth,y_smooth, color='xkcd:cobalt', label='VOL', linewidth=3.5)
    ax1.plot(predict['t'], predict['prediction'], color='xkcd:darkgreen',label='Prediction', linestyle=':', linewidth=2.5)
    ax1.plot(predict['t'], predict['Lower Bound'], color='xkcd:darkgreen',label='Lower Bound', linestyle=':', linewidth=1)
    ax1.plot(predict['t'], predict['Upper Bound'], color='xkcd:darkgreen',label='Upper Bound', linestyle=':', linewidth=1)
    ax1.set_xlabel('Time Period (Weeks)')
    ax1.set_ylabel('Volume')
    ax1.set_xlim(0,52)
    ax1.set_ylim(0,350000)
    ax1.set_xticks(range(0, 53, 2))

    #set title, legened, and savefig
    plt.title('Final Target Contest Trend')
    plt.legend(loc='lower center')
    fig.savefig('data/trend.png', dpi=fig.dpi)
