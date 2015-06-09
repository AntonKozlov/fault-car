#!/usr/bin/env python2

import sys
import struct

def log_values(fname, data):
	f = open(fname, "w")
	f.writelines([ "%.1f" % i + "\n" for i in data ])
	f.close()

def get_h_values(f, count):
	return [ struct.unpack('<h', f.read(2))[0] for i in range(0, count) ]

def get_f_values(f, count):
	return [ struct.unpack('<f', f.read(4))[0] for i in range(0, count) ]

sz = int(sys.argv[3])
f = open(sys.argv[2], "rb")
nameprefix = sys.argv[1]
log_values(nameprefix + "_" + "acc_x_values", get_h_values(f, sz)) 
log_values(nameprefix + "_" + "acc_y_values", get_h_values(f, sz)) 
log_values(nameprefix + "_" + "acc_z_values", get_h_values(f, sz)) 

#log_values(nameprefix + "_" + "gyro_x_values", get_f_values(f, 2176)) 
#log_values(nameprefix + "_" + "gyro_y_values", get_f_values(f, 2176)) 
#log_values(nameprefix + "_" + "gyro_z_values", get_f_values(f, 2176)) 
