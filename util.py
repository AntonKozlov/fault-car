import sys

def load_data(file):
    with open(file, "r") as f:
        return [ float(x) for x in f.read().splitlines() ]

def write_data(data, file_out):
    with open(file_out, "w") as f:
        f.writelines([ "%.1f" % i + "\n" for i in data ])

def input_file():
    if len(sys.argv) < 2 or sys.argv[1] == "-":
        return sys.stdin
    else:
        return open(sys.argv[1], "r")
