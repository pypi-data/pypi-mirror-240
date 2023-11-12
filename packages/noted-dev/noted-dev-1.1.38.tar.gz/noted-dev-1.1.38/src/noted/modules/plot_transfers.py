# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file "LICENCE.txt". In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

from numpy import float64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy import linalg
import matplotlib.dates as mdates

pd.set_option('display.width', None)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', None, 'display.max_columns', None)

filename_all_transfers = 'tests_lhcone/test_31th_august_2022/transfer_broker_all_transfers_1661866663.txt' # Main plot used in NOTED slides
filename_src_transfers = 'tests_lhcone/test_31th_august_2022/transfer_broker_src_rcsite_1661866663.txt'    # Main plot used in NOTED slides
filename_dst_transfers = 'tests_lhcone/test_31th_august_2022/transfer_broker_dst_rcsite_1661866663.txt'    # Main plot used in NOTED slides
title = 'LHCONE 31th of August 2022' # Main plot used in NOTED slides

# filename_all_transfers = 'tests_sc22/test_triumf/transfer_broker_all_transfers_1668267745.txt' # SC22 plot
# filename_src_transfers = 'tests_sc22/test_triumf/transfer_broker_src_rcsite_1668267745.txt'    # SC22 plot
# filename_dst_transfers = 'tests_sc22/test_triumf/transfer_broker_src_rcsite_1668267745.txt'    # SC22 plot
# title = 'LHCONE SC22' # SC22 plot

filename_all_transfers = 'tests_lhcone/test_17th_july_2023/modif_transfer_broker_all_transfers_1689583695.txt'
filename_src_transfers = 'tests_lhcone/test_17th_july_2023/transfer_broker_src_rcsite_1689583695.txt'
filename_dst_transfers = 'tests_lhcone/test_17th_july_2023/transfer_broker_src_rcsite_1689583695.txt'
title = '[CH, GB, IT, FR, ES, DE, US] to Tier 1s - 17th July 2023'

# Threshold to show with in red points
threshold_data       = 200   # Amount of data [GB]
threshold_throughput = 150   # Throughput [Gbps]
threshold_parallel   = 1200  # TCP parallel transfers
threshold_queued     = 55000 # Queued transfers

dict_all_transfers = pd.read_csv(filename_all_transfers, delimiter = ',', header = None, names = ['Timestamp', 'Datetime', 'Data [GB]', 'Throughput [Gbps]', 'Parallel transfers', 'Queued transfers']).to_dict()
dict_src_transfers = pd.read_csv(filename_src_transfers, delimiter = ',', header = None, names = ['Timestamp', 'Datetime', 'Data [GB]', 'Throughput [Gbps]', 'Parallel transfers', 'Queued transfers']).to_dict()
dict_dst_transfers = pd.read_csv(filename_dst_transfers, delimiter = ',', header = None, names = ['Timestamp', 'Datetime', 'Data [GB]', 'Throughput [Gbps]', 'Parallel transfers', 'Queued transfers']).to_dict()
df_all_transfers   = pd.DataFrame.from_dict(dict_all_transfers)
df_src_transfers   = pd.DataFrame.from_dict(dict_src_transfers)
df_dst_transfers   = pd.DataFrame.from_dict(dict_dst_transfers)

# Function to format data
def format_data(df_data):
    # Format data
    df_data['Datetime']  = df_data['Datetime'].str.split('datetime:', expand = True)[1].astype(str)               # Format datetime: 2022-05-15 01:20:05.848425  -> 2022-05-15 01:20:05.848425
    df_data['Datetime']  = df_data['Datetime'].str.replace('\..*', '', regex = True)                              # Format datetime: 2022-05-15 01:20:05.848425  -> 2022-05-15 01:20:05
    df_data['Datetime']  = df_data['Datetime'].str[:-2] + '00'                                                    # Format datetime: 2022-05-15 01:20:05  -> 2022-05-15 01:20:00
    df_data['Datetime']  = pd.to_datetime(df_data['Datetime'].str.strip(), format = '%Y-%m-%d %H:%M:%S') + pd.DateOffset(hours = 2)
    df_data['Data [GB]'] = df_data['Data [GB]'].str.split(' ', expand = True)[3].astype(float64)                  # Format data: data_gigabytes [GB]: 5.89805632 -> 5.89805632
    df_data['Timestamp'] = df_data['Timestamp'].str.split(' ', expand = True)[1].astype(int)                      # Format timestamp: timestamp: 1648645043578 [milliseconds] -> 1648645043578
    df_data['Queued transfers']   = df_data['Queued transfers'].str.split(' ', expand = True)[2].astype(int)      # Format queue: queued_transfers: 2126 -> 2126
    df_data['Throughput [Gbps]']  = df_data['Throughput [Gbps]'].str.split(' ', expand = True)[3].astype(float64) # Format throughput: throughput_gigabits [Gb/s]: 5.89805632 -> 5.89805632
    df_data['Parallel transfers'] = df_data['Parallel transfers'].str.split(' ', expand = True)[2].astype(int)    # Format TCP transfers: parallel_transfers: 252 -> 252
    df_data.set_index(pd.DatetimeIndex(df_data['Datetime']), inplace = True)
    return df_data

# Function to plot data XY Graph
def generate_plots(axis, data, ylabel, x_xticks_datetime, title, color, fig, stats):
    x_axis = np.linspace(0, data.shape[0]-1, num = data.shape[0])
    axis.plot(x_xticks_datetime, data, color = color, linewidth = 2, zorder = 1)
    if color == 'tab:orange': axis.fill_between(x_xticks_datetime, 0, data, where = data, color = color, alpha = 0.15)
    if stats:
        axis.scatter(x_xticks_datetime, data, color = color, marker = '.', zorder = 1, s = 2)
        axis.axhline(data.mean(), color = color, linestyle = '-.', linewidth = 1, zorder = 1, label = 'Mean = ' + str(round(data.mean(), 2))) # Mean value
        # Statistics: Linear Regression
        linear_regression = linregress(x_axis, data)
        m = linear_regression.slope
        b = linear_regression.intercept
        axis.plot(x_xticks_datetime, m*x_axis+b, color = 'xkcd:tan', linewidth = 1, zorder = 1, label = 'Linear regresion: \n$y = mx + b \longrightarrow m = $' + str(round(m, 2)) + '$, b = $' + str(round(b, 2)))
        # Statistics: Linear Least-Squares
        # Compute least-squares solution to equation Ax = b.
        # Compute a vector x such that the 2-norm |b - A x| is minimized
        # https://docs.scipy.org/doc/scipy/tutorial/stats.html
        # https://docs.scipy.org/doc/scipy/tutorial/linalg.html
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lstsq.html
        M = x_axis[:, np.newaxis]**[0, 2]      # Fit a quadratic polynomial of the form y = a + b*x**2 to data. We first form the “design matrix” M, with a constant column of 1s and a column containing x**2
        p, res, rnk, s = linalg.lstsq(M, data) # Find the least-squares solution to M.dot(p) = y, where p is a vector with length 2 that holds the parameters a and b
        yy = p[0] + p[1]*x_axis**2             # y = a + b*x**2
        axis.plot(x_xticks_datetime, yy, color = 'xkcd:lightblue', linewidth = 1, zorder = 1, label = 'Linear least-squares: \n$y = a + bx^2 \longrightarrow a = $' + str(round(p[0], 2)) + '$, b = $' + str(round(p[1], 2)))
        # Title, legend, ylabel, grid and xticks labels
        fig.suptitle(title)
        axis.grid(axis = 'x', linestyle = ':')
        axis.set_ylabel(ylabel)
        axis.legend(loc = 'upper right', fontsize = 6)
        # Date format in x-axis
        format = mdates.DateFormatter('%d/%m/%Y\n%H:%M:%S')
        axis.xaxis.set_major_formatter(format)

# Function to plot threshold values
def generate_plots_threshold(axis, df_all_data, str_data, color, threshold):
    df_data = df_all_data[df_all_data[str_data] > threshold]
    axis.scatter(df_data['Datetime'], df_data[str_data], color = color, linewidth = 2, marker = '.', zorder = 2)

# Function to remove plotting discontinuities
def remove_plotting_discontinuities(df_all, df_trf):
    list_trf_datetime = df_trf['Datetime'].to_list()
    df_not_trf = df_all[~df_all['Datetime'].isin(list_trf_datetime)]['Datetime']
    df_trf = pd.concat([df_trf, df_not_trf])
    df_trf = df_trf.sort_index()
    return df_trf

# Main function
def main():
    # Format data
    df_all_trf = format_data(df_all_transfers)
    df_src_trf = format_data(df_src_transfers)
    df_dst_trf = format_data(df_dst_transfers)
    df_all_trf = df_all_trf.drop_duplicates(subset = ['Timestamp'])
    # Fill with NaN the datetime where there were no transfers [remove lines while plotting discontinuities]
    df_src_trf = remove_plotting_discontinuities(df_all_trf, df_src_trf)
    df_dst_trf = remove_plotting_discontinuities(df_all_trf, df_dst_trf)
    # Plot data
    fig, axs = plt.subplots(4, 1)
    generate_plots(axs[0], df_all_trf['Data [GB]'], 'Amount of Data [GB]', df_all_trf['Datetime'], title, 'tab:blue',   fig, True)
    generate_plots(axs[0], df_src_trf['Data [GB]'], 'Amount of Data [GB]', df_src_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots(axs[0], df_dst_trf['Data [GB]'], 'Amount of Data [GB]', df_dst_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots(axs[1], df_all_trf['Throughput [Gbps]'],  'Throughput [Gbps]',  df_all_trf['Datetime'], title, 'tab:blue',   fig, True)
    generate_plots(axs[1], df_src_trf['Throughput [Gbps]'],  'Throughput [Gbps]',  df_src_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots(axs[1], df_dst_trf['Throughput [Gbps]'],  'Throughput [Gbps]',  df_dst_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots(axs[2], df_all_trf['Parallel transfers'], 'Parallel transfers', df_all_trf['Datetime'], title, 'tab:blue',   fig, True)
    generate_plots(axs[2], df_src_trf['Parallel transfers'], 'Parallel transfers', df_src_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots(axs[2], df_dst_trf['Parallel transfers'], 'Parallel transfers', df_dst_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots(axs[3], df_all_trf['Queued transfers'], 'Queued transfers', df_all_trf['Datetime'], title, 'tab:blue',   fig, True)
    generate_plots(axs[3], df_src_trf['Queued transfers'], 'Queued transfers', df_src_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots(axs[3], df_dst_trf['Queued transfers'], 'Queued transfers', df_dst_trf['Datetime'], title, 'tab:orange', fig, False)
    # Plot thresholds
    generate_plots_threshold(axs[0], df_all_trf, 'Data [GB]', 'red', threshold_data)
    generate_plots_threshold(axs[1], df_all_trf, 'Throughput [Gbps]',  'red', threshold_throughput)
    generate_plots_threshold(axs[2], df_all_trf, 'Parallel transfers', 'red', threshold_parallel)
    generate_plots_threshold(axs[3], df_all_trf, 'Queued transfers',   'red', threshold_queued)
    # Share x-axis and remove space between them
    axs[3].get_shared_x_axes().join(axs[3], axs[2], axs[1], axs[0])
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()
    # Plot just throughput -> CHEP conference plots
    fig, axs = plt.subplots(1, 1)
    generate_plots(axs, df_all_trf['Throughput [Gbps]'],  'Throughput [Gbps]',  df_all_trf['Datetime'], title, 'tab:blue',   fig, True)
    generate_plots(axs, df_src_trf['Throughput [Gbps]'],  'Throughput [Gbps]',  df_src_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots(axs, df_dst_trf['Throughput [Gbps]'],  'Throughput [Gbps]',  df_dst_trf['Datetime'], title, 'tab:orange', fig, False)
    generate_plots_threshold(axs, df_all_trf, 'Throughput [Gbps]',  'red', threshold_throughput)
    plt.tight_layout()
    plt.ylim(bottom = 0)
    plt.show()

main()
