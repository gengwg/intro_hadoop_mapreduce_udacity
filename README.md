Test code before running the MR job:
```
cat testdata | ./mapper.py | sort | ./reducer.py

or

head -n7 ../../data/purchases.txt | ./mapper.py | sort | ./reducer.py
```

Run the MR job:
```
hadoop fs -mkdir myinput2
hadoop fs -put ../../data/access_log myinput2
hs mapper.py reducer.py myinput2 myoutput_hits_to_page
hadoop fs -get  myoutput_hits_to_page/part-00000 hits_to_page.txt
```

Most popular file:
```
hadoop fs -get  myoutput_most_popular_files/part-00000 most_popular_files.txt
sort -n -k 2,2 most_popular_files.txt  | tail
117352
```
