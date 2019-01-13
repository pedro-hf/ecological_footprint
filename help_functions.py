import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

fs = 14
mpl.rcParams['font.size'] = fs
mpl.rcParams['axes.labelsize'] = fs
mpl.rcParams['xtick.labelsize'] =  fs
mpl.rcParams['ytick.labelsize'] =  fs
mpl.rcParams['legend.fontsize'] =  fs
mpl.rcParams['axes.titlesize'] =  fs


def top_k_pie(df, col, k, ax=None):
    """
    Plots the top k values of a column of a dataframe in a pie plot on a certain axes.
    :param df: DataFrame containing the data
    :param col: Name of the column to plot from the data frame
    :param k: Number of top values to plot
    :param ax: optional, axes object to plot on. By default it will create a new plot
    :return: return the axis
    """
    if not ax:
        fig, ax = plt.subplots()
    topk = df.set_index('code')[col].sort_values(ascending=False)[:k]
    total = df.set_index('code')[col].sum()
    topk['rest'] = total - topk.sum()
    ax.pie(topk, labels=topk.index)
    ax.set_title(col)
    return ax


def plot_eco_balance(data, feature, subfeature):
    """
    Function that will plot  biocapacity and ecological footprint for a certain subfeature (crop_land, carbon, ...)
    :param data: DataFrame containing the data
    :param feature: main feature to plot with biocapacity (EFConsTotGHA for example)
    :param subfeature: subfeature to plot (total, crop_land, carbon, ...)
    :return: figure and axes object with the plot.
    """
    bio = 'BiocapTotGHA_' + subfeature
    ef = feature + '_' + subfeature
    wd = data[data.country == 'World'].set_index('year')[[bio, ef]]
    wd['Balance'] = wd[bio] - wd[ef]
    y_even = wd[wd[bio] > wd[ef]].index.max()
    if y_even is np.nan:
        y_even = wd.index.max()-1
        print('We never had the capacity')
    elif y_even == wd.index.max():
        print('We have always capacity')
    else:
        print('The last year with a ecological footprint lower than our world\'s biocapacity was {}'.format(y_even))

    wd_plus = wd.loc[:y_even+1, :]
    wd_minus = wd.loc[y_even+1:, :]
    fig, ax = plt.subplots(figsize=(16,8))
    wd[[bio, ef]].plot(ax=ax, linewidth=4)
    plt.fill_between(wd_plus.index, wd_plus[bio], wd_plus[ef], alpha=0.2)
    plt.fill_between(wd_minus.index, wd_minus[bio], wd_minus[ef], alpha=0.2)

    subax = plt.axes([.67, .42, .25, .25],  aspect='equal')
    d2010 = data[data.year == 2010].set_index('country')[[bio, ef, 'code']]
    d2010.drop('World', inplace=True)
    var = 'Debtors 2010'
    d2010[var] = d2010[ef] - d2010[bio]
    top_k_pie(d2010[d2010[var] > 0], var, 5, ax=subax)

    subax2 = plt.axes([.10, .42, .25, .25],  aspect='equal')
    d1965 = data[data.year == 1965].set_index('country')[[bio, ef, 'code']]
    d1965.drop('World', inplace=True)
    var = 'Debtors 1965'
    d1965[var] = d1965[ef] - d1965[bio]
    top_k_pie(d1965[d1965[var] > 0], var, 5, ax=subax2)
    return fig, ax


def ef_linear_regression(df, year=2014, feat=['GDP', 'HDI', 'HLI', 'PD']):
    """
    Calculates a linear regresson for the 'EFConsTotGHA_percap'
    :param df: DataFrame containing the data
    :param year: year from the DataFrame to plot
    :param feat: list of features to use for the regression
    :return: regression model, r2 score, and scaler used for the regression
    """
    data_year = df[df.year == year].copy(deep=True)
    data_year.loc[:, 'PD'] = data_year.population / data_year.area
    data_year.drop(['area', 'population'], axis=1, inplace=True)
    data_year.dropna(inplace=True)
    X = data_year.loc[:, feat]
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    y = data_year[['EFConsTotGHA_percap']]
    lr = LinearRegression()
    lr.fit(X, y)
    r2 = lr.score(X, y)
    return lr, r2, scaler
