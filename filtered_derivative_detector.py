#!/usr/bin/env python2

import os
import sys
import math
from util import load_data, write_data
from plot import plot
from fault_detect import moving_average

def data_abs(data):
	return [ abs(x) for x in data ]

def filtered_derivative_detector(data, window_size, n):
	out_data = []
	window = [0] * window_size
	mid = window_size / 2
	for x in data:
		window = window[1:] + [x]
		out_data.append((sum(window[mid:window_size]) - sum(window[:mid])) / window_size)
	return out_data

def d_k(data, i, k, K):
	s = sum(data[i-k:i+k+1]) / (2*k + 1)
	r = 2*K / (math.sqrt(2*k + 1))
	return (s - r, s + r)

def intersect(a, b):
	return (max(a[0], b[0]), min(a[1], b[1]))

def adaptive_window_avg(data, N, K):
	data_new = [0] * N + data + [0] * N
	out_data = []
	for i in range(N, len(data)-N):
		k = 0
		interval = d_k(data, i, 0, K)
		while interval[0] < interval[1]:
			interval = intersect(interval, d_k(data, i, k, K))
			k = k + 1
		out_data.append(sum(data[i-k:i+k+1]) / (2*k + 1))
	return out_data

def main():
    window_size = 150
    threshold = 3000

    filename = sys.argv[1]
    data_in = load_data(filename)

    # second arg - maximum size of the window of interest
    # third arg - some threshold
    data_filtered = adaptive_window_avg(data_in, 100, 10)
    abs_data = data_abs(data_filtered)
    out_data = filtered_derivative_detector(abs_data, window_size, 0, 0)
    tline = [threshold] * len(out_data)

    plot(data_in)
    plot(data_filtered)
    plot(out_data, tline)

if __name__ == "__main__":
    main()

