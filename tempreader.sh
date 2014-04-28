#!/bin/sh

#DEBUG=true # pass it in on cmdline eg: DEBUG=true ./run.sh

DIR=`dirname $0`

#echo $DIR

. $DIR/settings.env
python $DIR/tempreader.py
