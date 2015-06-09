#!/usr/bin/env python2

import sys

import matplotlib.pyplot as plt
import pylab

import util

def plot(*datas):
    for data in datas:
        plt.plot(data)
    pylab.show()

if __name__ == '__main__':
    plot(*[util.load_data(f) for f in sys.argv[1:]])
