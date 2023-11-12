#!/bin/sh

echo "------------------------------------------------------------------" >> noted/src/noted/logs/sense.log
date >> noted/src/noted/logs/sense.log
echo "Received provision request from NOTED for $2"  >> noted/src/noted/logs/sense.log

STATUS=`sense_util.py -s -u $1`
echo "$2 current status:" ${STATUS} >> noted/src/noted/logs/sense.log

if [ "$STATUS" = "CANCEL - READY" ] || [ "$STATUS" = "CANCEL - COMMITTED" ]
then
  echo "$2 is down: OK to provision" >> noted/src/noted/logs/sense.log
  sense_util.py -r -u $1 >> noted/src/noted/logs/sense.log
  date >> noted/src/noted/logs/sense.log
  echo "$2 done" >> noted/src/noted/logs/sense.log
else
  echo "ERROR to provision" >> noted/src/noted/logs/sense.log
fi

exit 0