from libqtile import bar, widget, layout
from libqtile.config import Screen, Match
from .colors import colors

layouts = [
    layout.Columns(margin = 8, num_columns=3, border_focus_stack=colors[5], margin_on_single=4),
    layout.Max(margin = 8),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='zoom'),
])

widget_defaults = dict(
    font='Iosevka',
    fontsize=14,
   # padding=5, 
    foreground=colors[5],
)


extension_defaults = widget_defaults.copy()
Sep = widget.Sep(size_percent=1110)  
Stretch = widget.Spacer(bar.STRETCH)
GroupBoxx = widget.GroupBox(background=colors[2], inactive='000000', this_current_screen_border='aa6682', this_screen_border='aa6682',rounded=False, other_screen_border='240b0b', other_current_screen_border='240b0b', spacing=3, borderwidth=2) 

bgbar = '#00000000'

screens = [
   Screen(
        #wallpaper="/home/javigo07/Pictures/Wallpapers/Wallpaper 24.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(background=colors[2]),
                Sep,
                widget.CurrentLayout(background=colors[2], padding=0),
                widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
                widget.Prompt(),
                widget.Spacer(bar.STRETCH), 
                #Sep,
                widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
                GroupBoxx,
                widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
                #Sep,
                widget.Spacer(bar.STRETCH),
                #Sep,
                widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
                widget.Clock(format='%H:%M:%S', background=colors[2]),
            ],
            24,
            background=bgbar,
            margin=[0, 0, 0, 0]
        ),
        bottom=bar.Bar(
           [  
               widget.PulseVolume(background=colors[2]),
               widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
               widget.Spacer(bar.STRETCH),
               #Sep,
               widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
               widget.WindowName(empty_group_string="None", background=colors[2]),
               widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),#Sep,
               widget.Spacer(bar.STRETCH),
               widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0), 
               widget.QuickExit(default_text='無効にする', background=colors[2], fontsize=16),
               Sep,
               widget.Systray(background=colors[2]),
           ],
           24,
           background=bgbar,
           margin=[0, 0, 0, 0]
        ),
    ),
Screen(
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(background=colors[2]),
                Sep,
                widget.CurrentLayout(background=colors[2], padding=0),
                widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
                widget.Prompt(),
                widget.Spacer(bar.STRETCH), 
                #Sep,
                widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
                GroupBoxx,
                widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
                                #Sep,
                widget.Spacer(bar.STRETCH),
                widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
                widget.Clock(format='%H:%M:%S', background=colors[2]),
            ],
            24,
            background=bgbar,
            foreground='#ff0000',
            margin=[0, 0, 0, 0]
        ),
        bottom=bar.Bar(
           [  
               widget.PulseVolume(background=colors[2]),
               widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
               widget.Spacer(bar.STRETCH),
               widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
               widget.WindowName(empty_group_string="None", background=colors[2]),
               widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),               
               widget.Spacer(bar.STRETCH),
               widget.TextBox(text='', fontsize=20, foreground=colors[2], padding=0),
               widget.Mpris2(background=colors[2])
              ],
           24,
           background=bgbar,
           margin=[0, 0, 0, 0]
        ),
 ),
      

]
