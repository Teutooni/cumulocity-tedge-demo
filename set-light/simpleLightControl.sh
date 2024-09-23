#!/bin/bash

. /home/pi/thinedge-demo/config.sh

log=/home/pi/thinedge-demo/simpleLightControl.log

echo $1 > $log

command="${1#*,*,}"
lightid="${command%,*}"
on="${command#*,}"

echo "Setting light $lightid on to $on." >> $log

url="http://$HueIpAddress/api/$HueUserToken/lights/$lightid/state"

payload="{ \"on\": $on }"

curl -X PUT $url -H "$ContentJson" -d "$payload" >> $log

echo "{'status': 'SUCCESS'}"
