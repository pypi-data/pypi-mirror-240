import numpy as np
from datetime import datetime

import matplotlib as mpl

from pyearth.system.define_global_variables import *
from pyearth.visual.calculate_ticks_space import calculate_ticks_space

def plot_time_series_data_monthly_fill_with_zoom(aTime,
                                                 aData,
                                                 sFilename_out,
                                                 iDPI_in=None,
                                                 iFlag_trend_in=None,
                                                 iReverse_Y_in=None,
                                                 iSize_X_in=None,
                                                 iSize_Y_in=None,
                                                 dMax_Y_in=None,
                                                 dMin_Y_in=None,
                                                 sMarker_in=None,
                                                 sLabel_Y_in=None,
                                                 sLabel_legend_in=None,
                                                 sTitle_in=None):

    if iDPI_in is not None:
        iDPI = iDPI_in
    else:
        iDPI = 300

    if iFlag_trend_in is not None:
        iFlag_trend = 1
    else:
        iFlag_trend = 0

    if iReverse_Y_in is not None:
        iReverse_Y = 1
    else:
        iReverse_Y = 0

    if iSize_X_in is not None:
        iSize_X = iSize_X_in
    else:
        iSize_X = 12
    if iSize_Y_in is not None:
        iSize_Y = iSize_Y_in
    else:
        iSize_Y = 9

    if sLabel_Y_in is not None:
        sLabel_Y = sLabel_Y_in
    else:
        sLabel_Y = ''
    if sLabel_legend_in is not None:
        sLabel_legend = sLabel_legend_in
    else:
        sLabel_legend = ''
    if sTitle_in is not None:
        sTitle = sTitle_in
    else:
        sTitle = ''

    if sMarker_in is not None:
        sMarker = sMarker_in
    else:
        sMarker = '+'

    nstress = len(aTime)
    nan_index = np.where(aData == missing_value)
    aData[nan_index] = np.nan
    good_index = np.where(~np.isnan(aData))

    if dMax_Y_in is not None:
        dMax_Y = dMax_Y_in
    else:
        dMax_Y = np.nanmax(aData) * 1.2
    if dMin_Y_in is not None:
        dMin_Y = dMin_Y_in
    else:
        dMin_Y = np.nanmin(aData)  # if it has negative value, change here
    if (dMax_Y <= dMin_Y):
        return

    fig = mpl.pyplot.figure(dpi=iDPI)
    fig.set_figwidth(iSize_X)
    fig.set_figheight(iSize_Y)
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    pYear = mpl.dates.YearLocator(5)   # every year
    pMonth = mpl.dates.MonthLocator()  # every month
    sYear_format = mpl.dates.DateFormatter('%Y')
    x1 = aTime
    y1 = (aData[1])[0]
    y_top = (aData[0])[0]
    y_bot = (aData[2])[0]
    ax.fill_between(x1, y_top, y_bot,  facecolor='tomato')
    ax.plot(x1, y1,
            color='red', linestyle='--',
            marker=sMarker, markeredgecolor='blue',
            label=sLabel_legend)

    # calculate linear regression
    if iFlag_trend == 1:
        x_dummy = np.array([i.timestamp() for i in x1])
        x_dummy = x_dummy[good_index]
        y_dummy = y1[good_index]
        coef = np.polyfit(x_dummy, y_dummy, 1)
        poly1d_fn = np.poly1d(coef)
        mn = np.min(x_dummy)
        mx = np.max(x_dummy)
        x2 = [mn, mx]
        y2 = poly1d_fn(x2)
        x2 = [datetime.fromtimestamp(i) for i in x2]
        ax.plot(x2, y2, color='orange', linestyle='-.',  linewidth=0.5)

    ax.axis('on')
    ax.grid(which='major', color='grey', linestyle='--', axis='y')
    # ax.grid(which='minor', color='#CCCCCC', linestyle=':') #only y axis grid is

    # ax.set_aspect(dRatio)  #this one set the y / x ratio
    ax.xaxis.set_major_locator(pYear)
    ax.xaxis.set_minor_locator(pMonth)
    ax.xaxis.set_major_formatter(sYear_format)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)

    ax.set_xmargin(0.05)
    ax.set_ymargin(0.15)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel(sLabel_Y, fontsize=12)
    ax.set_title(sTitle, loc='center', fontsize=15)
    # round to nearest years...
    x_min = np.datetime64(aTime[0], 'Y')
    x_max = np.datetime64(aTime[nstress-1], 'Y') + np.timedelta64(1, 'Y')
    ax.set_xlim(x_min, x_max)
    if dMax_Y < 1000 and dMax_Y > 0.1:
        ax.yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%.1f'))
    else:
        ax.yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%.1e'))
    dummy = calculate_ticks_space(
        [y1, y_top, y_bot], nstep_in=5, iFlag_small_in=1)
    dSpace = dummy[0]
    if (dSpace <= 0):
        ax.invert_yaxis()

    else:
        ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(dSpace))
        dMin_Y = dummy[1]
        dMax_Y = dummy[2]
        if (iReverse_Y == 1):
            ax.set_ylim(dMax_Y, dMin_Y)
        else:
            ax.set_ylim(dMin_Y, dMax_Y)
    ax.legend(bbox_to_anchor=(0.0, 1.0), loc="upper left", fontsize=12)

    zoom_left = 0.55
    zoom_right = 0.85
    zoom_bot = 0.7
    zoom_top = 0.85

    # plot zoom part
    ax_zoom = fig.add_axes(
        [zoom_left, zoom_bot, zoom_right-zoom_left, zoom_top-zoom_bot])
    ax_zoom.plot(x1, y1,
                 color='red', linestyle='--',
                 marker=sMarker, markeredgecolor='blue',
                 label=sLabel_legend)
    x_min = np.datetime64(aTime[int(nstress*0.8)], 'Y')
    x_max = x_min + np.timedelta64(2, 'Y')
    ax_zoom.set_xlim(x_min, x_max)
    y_mean = np.mean(y1)
    ax_zoom.set_ylim(y_mean*0.99, y_mean * 1.01)
    pYear2 = mpl.dates.YearLocator(1)
    pMonth2 = mpl.dates.MonthLocator()
    ax_zoom.xaxis.set_major_locator(pYear2)
    ax_zoom.xaxis.set_minor_locator(pMonth2)
    # draw lines connecting zoom with parent

    mpl.pyplot.savefig(sFilename_out, bbox_inches='tight')

    mpl.pyplot.close('all')
    mpl.pyplot.clf()
    # print('finished plotting')
