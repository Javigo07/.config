#!/bin/bash

sleep 0.2s &

pipewire &
pipewire-pulse &
wireplumber &
discord --start-minimized &
openrgb --startminimized &
xcalib /home/javigo07/Samsung.icc &
picom &
flashfocus &
keepassxc &
dunst &
notify-send "WM started" &
~/.local/bin/wal -R &
