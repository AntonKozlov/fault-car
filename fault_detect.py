#!/usr/bin/env python2

import sys
from util import load_data, write_data

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

def main():
	filename = sys.argv[1]
	data_in = load_data(filename)

	# moving average
	threshold = 3000
	window_sz = 50

	filtered_data = moving_average(data_in, window_sz)
	res = mean_value_detector(filtered_data, threshold)
	write_data(res, filename + ".out")

if __name__ == "__main__":
	main()
