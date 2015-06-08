# fault-car
## Convert old logs
```
./convert.py old_log > new_log.txt
```
Convert all logs
```
for i in car_logs_*/*; do ./convert.py $i > txt/$i.txt; done
```
## Plot
```
./plot.py txt/car_logs_road/1.txt
```
