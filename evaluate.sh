#!/bin/sh

CMD=$1
[ -z $CMD ] && CMD=./myprocess.py
shift

LOGS="$@"
[ -z $LOGS ] && LOGS="car_logs_*2/[123]_acc_x_values"

while true; do
	for log in $LOGS; do 
		echo $log
	       	$CMD $log
	done
	echo repeat
done
