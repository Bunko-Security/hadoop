#/bin/bash
hdfs dfs -rm -r /cross-correlation/stripes

path=`pwd`/`dirname "$0"`

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
-D mapreduce.job.name="Cross Correlation Stripes" \
-files $path/../stripes/map.py,$path/../stripes/reduce.py \
-input /cross-correlation/input \
-output /cross-correlation/stripes \
-mapper $path/../stripes/map.py \
-reducer $path/../stripes/reduce.py