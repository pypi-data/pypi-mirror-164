#!/bin/bash

BUILDS='
cp310-manylinux_x86_64
cp310-manylinux_i686
cp310-musllinux_x86_64
cp310-musllinux_i686
cp311-manylinux_x86_64
cp311-manylinux_i686
cp311-musllinux_x86_64
cp311-musllinux_i686'

WINDOW="cibuildwheel"
DIR=$(dirname $(readlink -f $0))

echo $0
echo $DIR

WINDOW_CREATED=""
for build in $BUILDS; do
    COMMAND='pwd;pipx run cibuildwheel --platform linux; sleep 15'
    if [ -z "$WINDOW_CREATED" ]; then
        tmux new-window -d -c "$DIR" -n "$WINDOW" -e "CIBW_BUILD=${build}" "$COMMAND"
        WINDOW_CREATED="yes"
    else
        tmux split-window -d -c "$DIR" -t "$WINDOW" -e "CIBW_BUILD=${build}" "$COMMAND"
    fi
    tmux select-layout -t "$WINDOW" tile
done
tmux select-window -t "$WINDOW"
