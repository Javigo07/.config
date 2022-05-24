from libqtile.config import Key
from libqtile.lazy import lazy

from .settings import mod, terminal
from .traverse import *
mod = "mod4"

keys = [
    # Switch between windows
    Key([mod], "j", lazy.function(left), desc="Move focus to left"),
    Key([mod], "ntilde", lazy.function(right), desc="Move focus to right"),
    #Key([mod], "h", lazy.layout.left(), desc="Move focus down"),
    #Key([mod], "s", lazy.layout.right(), desc="Move focus up"), 
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "l", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "space", lazy.layout.floating(), desc="Focus floatin"),
   
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "ntilde", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "ntilde", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "l", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "d", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Restart Qtile"),
    Key(["mod1"], "p", lazy.spawn("flameshot gui"), desc="Restart Qtile"),
    Key([mod, "control"], "apostrophe", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.spawn("rofi -show drun"),
        desc="Show rofi -show drun uwur window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Fullscreen"),
    Key([mod], "o", lazy.window.static(),
        desc="Sticky window"),
    Key([mod], "Print", lazy.spawn("bluetoothctl connect 40:30:04:10:11:2E"),
        desc="Flameshot fullscreen"),
    Key([], "Print", lazy.spawn("flameshot gui"),
            desc="Flameshot gui (¿no es obvio? xd)"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
            desc="Pulseaudio Mute"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%"),
            desc="Pulseaudio VolDown"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"),
            desc="Pulseaudio VolUp"),
    Key([mod], "Hiragana_Katakana", lazy.spawn("pkill -9 mpv"),
            desc="Kill mpv"),
    Key([], "XF86AudioPlay", lazy.spawn("sh /home/javigo07/.scripts/pause_mpv.sh"),
            desc="Pause mpv"),
    Key([mod], "F12", lazy.spawn("sh /home/javigo07/.scripts/yt-r"), 
        desc="Ytfzf"),
    #Key([mod], "KP_Add", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"),
     #      desc="Pulseaudio VolUp")
]

