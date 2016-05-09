#!/bin/bash

#export AUTOSSH_PIDFILE="/var/run/autossh.pid"
export AUTOSSH_POLL=60
export AUTOSSH_FIRST_POLL=30
export AUTOSSH_GATETIME=0
export AUTOSSH_DEBUG=1

HOST="101.200.217.122"
USER=""
PASS=""
PORT="23456"
CMD=$@
 
VAR=$(expect -c "
spawn /usr/bin/autossh -M 23456 $USER@$HOST -p $PORT $CMD
match_max 100000
expect \"*?password:*\"
send -- \"$PASS\r\"
send -- \"\r\"
interact
")
echo "==============="
echo "$VAR"
