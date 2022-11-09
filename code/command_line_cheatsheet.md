* set: expose all environment vars
* mkdir: Make directory
* pwd: print working directory
* cd: change directory
* cd .. : move up one directory level
* rm -R: remove file/directory
* ps-ef: list processes
* ls: list files in working directory
* ls -a: list hidden files as well
* cat <filename>: print the contents of a file to the command linef
* cat .ssh/id_rsa.pub > id_rsa.txt: assign the contents of a file to another file
* cat .ssh/id_rsa.pub >> id_rsa.txt : append the contents of a file to an existing file
* df: file system disk free
* du -sh /home/: disk usage - space in home dir 17 
* du -sh *: used space in next level down (subfolders of current dir)
* du -sh /home/xxxx/* | sort -h 19 
* watch df (disk free)
* du -h -d1 (disk usage 1 directory down; without this it is recursive) 
* watch ls -LR (recursive 1s)
* top: shows memory usage and processes. VIRT = capacity, RES = used memory. For Spark context, java represents spark processing (with Python wrapper).
    * Note that Java is greedy and if no pressure on memory will not perform garbage collection. Give Java more memory than you think you'll need
    * Rule of thumb for Java memory allocation: say 1 row is 1000B, for 1000 rows need 1MB of memory
    * If CPU sitting at low number (~100-400) for long periods of time, process not going to complete. >1000 is good. Anything above 400 is acutally processing data
    * Memory usage to watch: RES vs VIRT
    * KiB Swap: Far right number gives bytes available on Jupyter server. If too high, then server may kill job.
    * Option 1: individual CPU usage (for everyone on server). "us": usage, "sy": system usage,
* top -b -p <pid> > top_output.txt : pipe contents of top to a file for a given process ID
* cat /proc/meminfo: shows detailed memory metdata
* cat /proc/cpuinfo: shows all CPU metadata

## Searching things
* grep -l ""correlation_id":"xxxxx" 
* grep -l ""correlation_id":"xxxx" 
* grep -C 20 "correlation_id":"xxxx" \\ (C gives context above and below by 20 chars)
* grep -l -v "blah" \\ everything excluding blah, case insensitive
* wc -1 filename.txt \\ word count lines number of lines in file 
* head -n10 filename.txt \\ shows first 10 lines

## On the fly computations
* xxx - | head : View contents of file (top)
* awk: sum up the amount of disk usage per parquet file
    `aws s3 ls s3://ndhprod-curated-nab/AFS/BA0586/DATA/2021/12/20/DOIBACTHIST/DELTA/ | awk '{ sum+=$3 } END {print sum}'`

## Spark and memory
* Spark goal: maximise CPU usage. If Java process is spending lots of time garbage collecting, % CPU usage will be low.
* With 64 cores, theoretically expect 64,000 
* With Pyspark local, running 1 executor with N cores. So memory is collective
* Optimal partition:core ratio is 1.5-2 for computational efficiency, assuming sufficient memory without having to do garbage collection too often

## Spark Compute troubleshooting
1. check Top for memory usage - is it excessive?
2. If writing, check whether Spark temporary directory is at capacity. Unless explicitly set, this is usually $HOME/.tmp or $HOME/ tmp. Use df to check file usage

## Write out memory usage to file during a job every 1 second (execute as shel Multiply result by 4 to get RES in bytes
``` bash
# statm.sh
date
FILE="/proc/$1/statm"
while [ -f "$FILE" ]
do
cat /proc/$1/statm | awk '{print $2*4 }'
sleep 1;
done
```
* generate stats
./statm.sh <pid> > output.txt www
* read stats
```python
df_mem = pd.read_csv("filename.txt", sep=" ", skip rows=[0], header=None)
(df_mem [0]/1024000).plot();
print (f"max memory usage: {df_mem.max()/1024000}")
```

## Convert Jupyter notebook to HTML document
* jupyter nbconvert --output-dir='.' mynotebook.ipynb --to html --TemplateExporter.exclude_input=True --no-prompt