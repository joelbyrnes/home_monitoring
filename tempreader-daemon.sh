#!/bin/bash

# TODO add LSB header here

DAEMON=/usr/bin/screen
DIR=/home/pi/home_monitoring
ARGS="-D -m -S tempreader $DIR/tempreader.sh"
PIDFILE=/var/run/tempreader.pid
DAEMON_LOGFILE=$DIR/daemon.log

# TODO don't use screen -D and s-s-d -b find some way to get the right PID

case "$1" in
  start)
    echo "Starting server"
    /sbin/start-stop-daemon --start --oknodo --pidfile $PIDFILE --make-pidfile \
        -b --exec $DAEMON -- $ARGS >> $DAEMON_LOGFILE
    ;;
  stop)
    echo "Stopping server"
    /sbin/start-stop-daemon --stop --pidfile $PIDFILE --verbose >> $DAEMON_LOGFILE
    ;;
  *)
    echo "Usage: tempreader-daemon {start|stop}"
    exit 1
    ;;
esac

exit 0

