#!/bin/bash

sleep 0.2s &
doas ln -s ~/Extras/.hidden/distfiles /var/cache/distfiles
ln -s ~/.config/keepassxc/KeepassCache/keepassxc ~/.cache/keepassxc
ln -s ~/.config/wal/walcache ~/.cache/wal
ln -s ~/.config/wal/walcache/colors-rofi-dark.rasi ~/.config/rofi/config.rasi
wal -R &
xcalib /home/javigo07/LG.icc &
gentoo-pipewire-launcher &
picom &
flashfocus &
keepassxc &
dunst &


