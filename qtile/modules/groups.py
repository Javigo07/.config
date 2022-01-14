from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from .keys import keys
from .settings import mod


group_names = [("0"), ("一"), ("二"), ("三"),
        ("四"), ("五"), ("六"),
        ("七"), ("八"), ("九")]


groups = [Group(name) for name in group_names if name != "0"]

for i, name in enumerate(group_names):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen(toggle=True)))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))


