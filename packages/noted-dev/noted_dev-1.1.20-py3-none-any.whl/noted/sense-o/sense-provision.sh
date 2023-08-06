#!/bin/sh

echo "------------------------------------------------------------------" >> log/sense.log
date >> log/sense.log
echo "Received provision request from NOTED for $2"  >> noted/logs/sense.log

STATUS=`/usr/local/bin/sense_util.py -s -u $1`
echo "$2 current status:" ${STATUS} >> log/sense.log

if [ "$STATUS" = "CANCEL - READY" ]
then
  echo "$2 is down: OK to provision" >> log/sense.log
  /usr/local/bin/sense_util.py -r -u $1 >> log/sense.log
  date >> log/sense.log
  echo "$2 done" >> log/sense.log
else
  echo "ERROR to provision" >> log/sense.log
fi

exit 0