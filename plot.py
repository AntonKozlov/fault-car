#!/usr/bin/env python2

import numpy as np
import matplotlib.pyplot as plt
import pylab

import util

def load(file):
    return [ float(x) for x in file.read().splitlines() ]

def plot(data):
    plt.plot(data)
    pylab.show()

if __name__ == '__main__':
    plot(load(util.input_file()))
