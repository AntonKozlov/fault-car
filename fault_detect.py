#!/usr/bin/env python2

import sys
from util import load_data, write_data
from plot import plot

def moving_average(data, window_size):
	out_data = []
	window = [0] * window_size
	for x in data:
		window = window[1:] + [x]
		out_data.append(sum(window) / window_size)
	return out_data

def exp_moving_average(data, window_size):
	out_data = []
	a = 2.0 / (window_size + 1)
	ema = data[0];

	for x in data:
		# Formula: ema = a*x + (1 - a)*ema
		ema += a * (x - ema)
		out_data.append(ema)

	return out_data

# http://people.irisa.fr/Michele.Basseville/kniga/kniga.pdf
# Example 2.3.4
def GLR_detector(data):
	pass

# Determine fault by change in mean
def mean_value_detector(data, threshold):
	return [0 if abs(x) < threshold else 1 for x in data]

def average_diff(data, func, window_size):
	normal = func(data, window_size)
	double = func(data, window_size * 2)
	return map(lambda x: x[0] - x[1], zip(normal, double))

def main():
	threshold = 750
	window_size = 100

	filename = sys.argv[1]
	data_in = load_data(filename)

	# Uncomment for more realistic first values. First window_size/4 values
	# should not be taken into account in the output data and plots.
	# data_in[:0] = [sum(data_in[:(window_size/4)])/(window_size/4)]

	filtered_ma = average_diff(data_in, moving_average, window_size)
	filtered_ema = average_diff(data_in, exp_moving_average, window_size)

	plot([0] * len(data_in),
	     filtered_ma,
	     filtered_ema,
	     [threshold] * len(data_in),
	     [-threshold] * len(data_in),
	     )

	mean_ma  = mean_value_detector(filtered_ma,  threshold)
	mean_ema = mean_value_detector(filtered_ema, threshold)

	plot(mean_ema)
	plot(mean_ma)

	write_data(mean_ema, filename + ".out")

if __name__ == "__main__":
	main()
