#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )


for line in sys.stdin:
    m = p.match(line)
    if not m:
        continue
    host, ignore, user, date, request, status, size = m.groups()
    print "{0}\t{1}".format(request.strip().split()[1], 1)
