import datetime
import dateutil.parser

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

def plot_datetimes_vs_value(data, xlim=True, scatter=False, title=False):
    x = [d[0] for d in data]
    y = [d[1] for d in data]

    x = [dateutil.parser.parse(xe) for xe in x]
    x = [xe.replace(tzinfo=None) for xe in x]

    fig, ax = plt.subplots()

    if title:
        ax.set_title(y[-1])

    if scatter:
        ax.scatter(x, y, s=1)
    else:
        ax.plot(x, y, linewidth=1)

    if xlim:
        datemin = np.datetime64(x[0], 'M')
        datemax = np.datetime64(x[-1], 'M') + np.timedelta64(1, 'M')
        ax.set_xlim(datemin, datemax)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
    ax.grid(True)

def plot_timeseries(x, y, xlim=True, scatter=False, title=False):
    x = [dateutil.parser.parse(xe) for xe in x]
    x = [xe.replace(tzinfo=None) for xe in x]

    fig, ax = plt.subplots()

    if title:
        ax.set_title(y[-1])

    if scatter:
        ax.scatter(x, y, s=1)
    else:
        ax.plot(x, y, linewidth=1)

    if xlim:
        datemin = np.datetime64(x[0], 'M')
        datemax = np.datetime64(x[-1], 'M') + np.timedelta64(1, 'M')
        ax.set_xlim(datemin, datemax)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
    ax.grid(True)

    plt.show()
