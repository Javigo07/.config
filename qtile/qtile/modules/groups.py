from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from .keys import keys
from .settings import mod


group_names = [("一",""), ("二",""), ("三",""),
        ("四",""), ("五",""), ("六",""),
        ("七",""), ("八",""), ("九", "max")]

def match(name):
   # if name == group_names[8][0]:
    #    return [Match(wm_class='firefox')]
    if name == group_names[1][0]:
        return [Match(wm_class='Telegram')] 
    return [] 

groups = [Group(name, layout=layout, matches=match(name)) for name, layout in group_names]

for i, name in enumerate(group_names):
    keys.append(Key([mod], str(i+1), lazy.group[name[0]].toscreen(toggle=True)))
    keys.append(Key([mod, "shift"], str(i+1), lazy.window.togroup(name[0])))
    
