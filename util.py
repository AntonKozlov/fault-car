import sys

def input_file():
    if len(sys.argv) < 2 or sys.argv[1] == "-":
        return sys.stdin
    else:
        return open(sys.argv[1], "r")
