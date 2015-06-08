#!/usr/bin/env python2

import re
import util

def load(file):
    for l in file.readlines():
        l = l.rstrip('\n').strip()
        if l.startswith('{'):
            l = l[1:]
        if l.endswith('}'):
            l = l[:-1]
        if l.startswith('---Type <return>'):
            continue
        for si in l.split(','):
            si = si.strip()
            if not si:
                continue
            m = re.match(r'(\d+) <repeats (\d+) times>', si)
            if m:
                val = float(m.group(1))
                for i in xrange(int(m.group(2))):
                    yield val
            else:
                yield float(si)

if __name__ == '__main__':
    for i in load(util.input_file()):
        print(i)

