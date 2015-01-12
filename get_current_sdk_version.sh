#!/bin/sh

curl -s https://appengine.google.com/api/updatecheck | grep release | awk -F '\"' '{print $2}'
