#!/usr/bin/env python2

import sys, os
from util import load_data
from plot import plot
from math import sqrt
from fault_detect import moving_average

def stat(data, window_size):
    e = []
    d = []
    window = data[:window_size]
    data = data[window_size:]
    for x in data:
        window = window[1:] + [x]
        _e = sum(window) / window_size
        _d = (sum(map(lambda x: x*x, window)) - _e * _e * window_size) / (window_size + 1)
        e.append(_e)
        d.append(_d)
    return e, d

if __name__ == "__main__":
    dirname = sys.argv[1]

    to_plot_e = [[0] * 2500]
    to_plot_d = [[0] * 2500]

    for filename in os.listdir(dirname):
        data_in = load_data(dirname + '/' + filename)
        e, d = stat(map(abs, moving_average(data_in, 50)), 100)
        to_plot_e.append(e)
        to_plot_d.append(map(sqrt, d))

    plot(*to_plot_d)
    plot(*to_plot_e)
