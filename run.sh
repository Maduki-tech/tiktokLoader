#!/bin/bash
export DISPLAY=127.0.0.1:0.0
docker run -it -u=$(id -u $USER):$(id -g $USER) --pid=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v $(pwd)/app:/app --rm tiktokloader

