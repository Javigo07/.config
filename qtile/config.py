from typing import List  # noqa: F401

from modules.keys import keys
from modules.screens import screens, layouts, floating_layout
from modules.groups import groups
from modules.colors import colors

from libqtile import hook

import os
import subprocess

@hook.subscribe.startup_once
def startup(): 
    subprocess.Popen(['.config/qtile/autostart.sh'])
 
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
cursor_warp = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
