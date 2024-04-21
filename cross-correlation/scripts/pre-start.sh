path=`pwd`/`dirname "$0"`

chmod +x $path/start-pairs.sh
chmod +x $path/start-stripes.sh
chmod +x $path/createdirs.sh
chmod +x $path/../checks_creator.py
chmod +x $path/../client.py

chmod +x $path/../pairs/map.py
chmod +x $path/../pairs/reduce.py
chmod +x $path/../stripes/map.py
chmod +x $path/../stripes/reduce.py

sh $path/createdirs.sh