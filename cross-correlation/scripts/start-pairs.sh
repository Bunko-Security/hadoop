#/bin/bash
hdfs dfs -rm -r /cross-correlation/pairs

path=`pwd`/`dirname "$0"`

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
-D mapreduce.job.name="Cross Correlation Pairs" \
-files $path/../pairs/map.py,$path/../pairs/reduce.py \
-input  /cross-correlation/input \
-output  /cross-correlation/pairs \
-mapper $path/../pairs/map.py \
-reducer $path/../pairs/reduce.py