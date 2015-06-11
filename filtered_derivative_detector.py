#!/usr/bin/env python2

import sys
from util import load_data, write_data
from plot import plot

def data_abs(data):
	return [ abs(x) for x in data ]

def filtered_derivative_detector(data, window_size, h, n):
	out_data = []
	window = [0] * window_size
	mid = window_size / 2
	for x in data:
		window = window[1:] + [x]
		out_data.append(sum(window[mid:window_size]) - sum(window[:mid]))
	return out_data

def calc_max_mean(filename, window_size):
	data = load_data(filename)
	window = [0] * window_size
	for x in data:
		

def main():
    window_size = 400

    filename = sys.argv[1]
    data_in = load_data(filename)

    abs_data = data_abs(data_in)
    out_data = filtered_derivative_detector(abs_data, window_size, 0, 0)

    plot(data_in)
    plot(out_data)

if __name__ == "__main__":
    main()

