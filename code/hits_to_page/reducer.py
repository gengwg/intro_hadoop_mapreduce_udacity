#!/usr/bin/python

import sys

hitsTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the hits for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitsTotal
        oldKey = thisKey;
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += float(thisHit)
    # we have not processed the last key when we exit out of the loop

# process last key
# without this we will miss the sale for the last store
if oldKey != None:
    print oldKey, "\t", hitsTotal

