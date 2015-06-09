#!/usr/bin/env python2

import sys

def moving_average(data, window_size):
	out_data = []
	tmp = sum(data[0:window_size-1])
	for i in range(window_size, len(data)):
		tmp += data[i] - data[i - window_size + 1]
		out_data.append(tmp / window_size)
	return out_data

def log_into_file(data, file_out):
	f = open(file_out, "w")
	f.writelines([ "%.1f" % i + "\n" for i in data ])
	f.close()

# http://people.irisa.fr/Michele.Basseville/kniga/kniga.pdf
# Example 2.3.4
def GLR_detector(data):
	pass

# Determine fault by change in mean
def mean_value_detector(data):
	pass

def load_data(fname):
	f = open(fname, "r")
	return [ float(x) for x in f.read().splitlines() ]


def main():
	window_sz = 5
	
	filename = sys.argv[1]
	data_in = load_data(filename)
	filtered_data = moving_average(data_in, window_sz)
	log_into_file(filtered_data, filename + ".out")

	mean_value_detector(filtered_data)

if __name__ == "__main__":
	main()
