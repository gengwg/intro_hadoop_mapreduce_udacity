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
    page = request.strip().split()[1]
    if page.startswith("http://www.the-associates.co.uk"):
        print "{0}\t{1}".format(page[31:], 1)
    else:
        print "{0}\t{1}".format(page, 1)
