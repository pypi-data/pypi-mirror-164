#!/bin/sh

echo "------------------------------------------------------------------" >> log/sense.log
date >> log/sense.log
echo "Received cancel request from NOTED for $2" >> noted/logs/sense.log

STATUS=`/usr/local/bin/sense_util.py -s -u $1`
echo "$2 current status:" ${STATUS} >> log/sense.log

if [ "$STATUS" = "REINSTATE - READY" ] || [ "$STATUS" = "REINSTATE - COMMITTED" ] || [ "$STATUS" = "CREATE - READY" ]
then
  echo "$2 is up: OK to cancel" >> log/sense.log
  /usr/local/bin/sense_util.py -ca -u $1 >> log/sense.log
  date >> log/sense.log
  echo "$2 done" >> log/sense.log
else
  echo "ERROR to cancel" >> log/sense.log
fi

exit 0