#!/bin/bash
echo $#
echo $2
echo $1

#start work default
if [ "$1"  = "start" ]
then
    work="video2format"
    log=$work.out
    nohup python3 ./main.py  $work &>$log&
    exit
fi

##stop work
if [ "$1"  = "stop" ]
then
    ps -ef  |grep main.py  |awk '{print $2}'  |while read pid
        do
            kill -9 $pid
        done
fi

##restart work
if [ "$1"  = "restart" ]
then
    ps -ef  |grep main.py  |awk '{print $2}'  |while read pid
        do
            kill -9 $pid
        done

    work="feature"
    log=$work.out
    nohup python3 ./main.py  $work &>$log&
    exit
fi