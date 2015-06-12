#!/usr/bin/env python2

import sys

import numpy as np

from plot import plot
from util import load_data, input_file

def pushwin(x, win):
    return [x] + win[:-1]
def afilter(xw, yw, data):
    out = []
    xwin = [0] * len(xw)
    ywin = [0] * len(yw)
    for x in data:
        xwin = pushwin(x, xwin)
        yf = np.dot(xwin, xw)
        yo = np.dot(pushwin(yf, ywin), yw)
        out.append(yo)
        ywin = pushwin(yo, ywin)
    return out

def desceding(r, data):
    return afilter([1], [r, 1 - r], data)

def average(win_sz, data):
    return afilter([1. / win_sz] * win_sz, [1.], data)

def derivative(win_sz, data):
    hsz = win_sz / 2
    lsz = win_sz - hsz
    return afilter([1.] * lsz + [-1.] * hsz, [1], data)

def imp(len):
    return [1.0] + [0.] * (len - 1)

def load_xy_data():
    xdata, ydata = [ load_data(sys.argv[i]) for i in 1, 2 ]
    return 0.5 * np.sum([xdata, ydata], axis = 0)

def load_x_data():
    return load_data(sys.argv[1])

if __name__ == '__main__':
    win_sz = 200

    data = load_x_data()
    data = average(win_sz, data)

    #mean_curve = desceding(.01, data)
    mean_curve = average(40, data)
    diff_curve = np.absolute(np.subtract(mean_curve, data))
    threshold = 1.25 * np.max(diff_curve[win_sz : len(diff_curve) / 2])
    fault = threshold < diff_curve

    plot(data,
        [ 1000.0 if x else 0 for x in fault ],
        mean_curve,
        [x + threshold for x in mean_curve],
        [x - threshold for x in mean_curve],
        )
