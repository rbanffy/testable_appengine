#!/bin/sh

LAST_KNOWN_GOOD_VERSION="1.9.40"

if [ -f $(which curl) ]
then
    VERSION=$(curl -s https://storage.googleapis.com/appengine-sdks/featured/VERSION | grep release | awk -F '\"' '{print $2}')
else
    VERSION=$(wget -q -O - https://storage.googleapis.com/appengine-sdks/featured/VERSION | grep release | awk -F '\"' '{print $2}')
fi

if [ VERSION="0.0.0" ]
then
    VERSION=$LAST_KNOWN_GOOD_VERSION
fi

echo $VERSION
