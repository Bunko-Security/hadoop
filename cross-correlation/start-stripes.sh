#/bin/bash
hdfs dfs -rm -r /cross-correlation/stripes

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
-D mapreduce.job.name="Cross Correlation Stripes" \
-files `pwd`/stripes/map.py,`pwd`/stripes/reduce.py \
-input /cross-correlation/input \
-output /cross-correlation/stripes \
-mapper `pwd`/stripes/map.py \
-reducer `pwd`/stripes/reduce.py