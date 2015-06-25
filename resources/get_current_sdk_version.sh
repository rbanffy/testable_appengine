#!/bin/sh

curl -s https://storage.googleapis.com/appengine-sdks/featured/VERSION | grep release | awk -F '\"' '{print $2}'
