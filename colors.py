import os

colors = []
cache='/home/javigo07/.config/wal/walcache/colors'

def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(16):
            colors.append(file.readline().strip())
load_colors(cache)



