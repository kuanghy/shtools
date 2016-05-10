#!/bin/bash

if [ -z $R_HOST -o -z $R_USER ]; then
    echo "Please set the env \$R_HOST and \$R_USER, and then try again."
    exit 1
fi

if [ ! -d ~/.autossh ]; then
    mkdir -p ~/.autossh
fi

USER_AUTOSSH_DIR="$HOME/.autossh"

if [ -s $USER_AUTOSSH_DIR/autossh.log ]; then
    TEN_MBYTE=`expr 10 \* 1024 \* 1024`
    logsize=`du -b $USER_AUTOSSH_DIR/autossh.log | awk '{ print $1 }'`
    if [ "$logsize" -gt "$TEN_MBYTE" ]; then
        timestamp=`date +%Y``date +%m``date +%d``date +%H``date +%M``date +%S`
        (
            cd $USER_AUTOSSH_DIR
            tar czvf autossh_${timestamp}.log.tar.gz autossh.log 
            rm -rf $USER_AUTOSSH_DIR/autossh.log
        ) > /dev/null
    fi
fi

export AUTOSSH_PIDFILE="$USER_AUTOSSH_DIR/autossh.pid"
export AUTOSSH_LOGFILE="$USER_AUTOSSH_DIR/autossh.log"
export AUTOSSH_FIRST_POLL=30
export AUTOSSH_POLL=60
export AUTOSSH_GATETIME=0
export AUTOSSH_DEBUG=1

random() {
    while true; do
        if [ "$RANDOM" -gt 20000 ]; then
            echo $RANDOM
            break
        fi
    done
}

MONITOR_PORT=$(random)
[[ -n $R_PORT ]] && P_PORT="-p $R_PORT" || P_PORT=""
 
expect -c "
spawn /usr/bin/autossh -M $MONITOR_PORT $R_USER@$R_HOST $P_PORT $@
expect \"*?password:*\"
send -- \"$R_PASS\r\"
send -- \"\r\"
interact
"

