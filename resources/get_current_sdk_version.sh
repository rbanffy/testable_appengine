#!/bin/sh

if [ -f /usr/bin/curl ]
then
    curl -s https://storage.googleapis.com/appengine-sdks/featured/VERSION | grep release | awk -F '\"' '{print $2}'
else
    wget -q -O - https://storage.googleapis.com/appengine-sdks/featured/VERSION | grep release | awk -F '\"' '{print $2}'
fi
