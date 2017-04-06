import re

file = open("testdata", "r")

p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )

for line in file.readlines():
    m = p.match(line)
    if not m:
        continue
    host, ignore, user, date, request, status, size = m.groups()
    print m.groups()
