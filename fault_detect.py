#!/usr/bin/env python2

import sys
from util import load_data, write_data

def moving_average(data, window_size):
	out_data = []
	tmp = sum(data[0:window_size-1])
	for i in range(window_size, len(data)):
		tmp += data[i] - data[i - window_size + 1]
		out_data.append(tmp / window_size)
	return out_data

# http://people.irisa.fr/Michele.Basseville/kniga/kniga.pdf
# Example 2.3.4
def GLR_detector(data):
	pass

# Determine fault by change in mean
def mean_value_detector(data):
	pass

def main():
	window_sz = 5
	
	filename = sys.argv[1]
	data_in = load_data(filename)
	filtered_data = moving_average(data_in, window_sz)
	write_data(filtered_data, filename + ".out")

	mean_value_detector(filtered_data)

if __name__ == "__main__":
	main()
