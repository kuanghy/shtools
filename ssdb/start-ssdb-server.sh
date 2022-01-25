#! /bin/bash

pidfile="/data/ssdb/ssdb.pid"
if [ -e "$pidfile" ]; then
     pid=`head -1 $pidfile`
     kill $pid
     rm "$pidfile"
fi
sleep 1
exec /home/server/local/ssdb/ssdb-server /home/server/local/ssdb/ssdb.conf
