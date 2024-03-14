#/bin/bash
hdfs dfs -rm -r /cross-correlation/pairs

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
-D mapreduce.job.name="Cross Correlation Pairs" \
-files `pwd`/pairs/map.py,`pwd`/pairs/reduce.py \
-input  /cross-correlation/input \
-output  /cross-correlation/pairs \
-mapper `pwd`/pairs/map.py \
-reducer `pwd`/pairs/reduce.py