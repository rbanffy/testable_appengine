#!/bin/sh

# curl -s https://appengine.google.com/api/updatecheck | grep release | awk -F '\"' '{print $2}'

# Please see https://code.google.com/p/googleappengine/issues/detail?id=11604
echo 1.9.17
