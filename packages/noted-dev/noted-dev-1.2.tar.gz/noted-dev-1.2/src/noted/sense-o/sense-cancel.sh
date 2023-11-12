#!/bin/sh

echo "------------------------------------------------------------------" >> noted/src/noted/logs/sense.log
date >> noted/src/noted/logs/sense.log
echo "Received cancel request from NOTED for $2" >> noted/src/noted/logs/sense.log

STATUS=`sense_util.py -s -u $1`
echo "$2 current status:" ${STATUS} >> noted/src/noted/logs/sense.log

if [ "$STATUS" = "REINSTATE - READY" ] || [ "$STATUS" = "REINSTATE - COMMITTED" ] || [ "$STATUS" = "CREATE - READY" ]
then
  echo "$2 is up: OK to cancel" >> noted/src/noted/logs/sense.log
  sense_util.py -ca -u $1 >> noted/src/noted/logs/sense.log
  date >> noted/src/noted/logs/sense.log
  echo "$2 done" >> noted/src/noted/logs/sense.log
else
  echo "ERROR to cancel" >> noted/src/noted/logs/sense.log
fi

exit 0