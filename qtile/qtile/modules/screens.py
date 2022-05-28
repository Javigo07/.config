from libqtile import bar, layout
from qtile_extras import widget
from libqtile.config import Screen, Match
from .colors import colors
from .cuswidgets import ExpandingClock

#from qtile_extras import widget as widgetEx 

layouts = [
    layout.Columns(margin = 5, num_columns=3, border_focus_stack=colors[5], margin_on_single=[6, 8, 6, 8]),
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
    Match(wm_class='Telegram', title='Media viewer'),
    Match(wm_class='leagueclientux.exe'),
    Match(wm_class='osu!.exe')
])

bgwidgets = [colors[1]+'80', colors[0]+'80']
bgbar = colors[0]+'80'
bglyphs = colors[0]+'00'
fglyphs = colors[1]+'40'

widget_defaults = dict(
    font='Iosevka Term Nerd Font Complete',
    fontsize=18,
    padding=-2, 
    foreground=colors[0],
    font_colour=colors[8])


extension_defaults = widget_defaults.copy()

Sep = widget.Sep(
        size_percent=100,
        background=bgwidgets,
        foreground='#ffffff',
        linewidth=1,
        padding=4)  

GroupBoxx = widget.GroupBox(
        background=bgwidgets,
        inactive=colors[0],
        this_current_screen_border=[colors[3],colors[1]],
        this_screen_border=[colors[1],colors[3]],
        rounded=True,
        other_screen_border=[colors[1],colors[3]],
        other_current_screen_border=[colors[3],colors[1]], 
        spacing=3, 
        borderwidth=3,
        highlight_method='line',
        highlight_color=[colors[1]+'4D',colors[0]+'4D']
        ) 




screens = [
   Screen(
        #wallpaper="/home/javigo07/Pictures/Wallpapers/Wallpaper 24.png",
        #wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    text='',
                    fontsize=24,
                    background=bgwidgets,
                    foreground=bglyphs,
                    padding=-2),
                widget.CurrentLayoutIcon(
                    background=bgwidgets),
                Sep,
                widget.Spacer(
                    length=2,
                    background=bgwidgets
                    ),
                widget.AGroupBox(
                    background=bgwidgets,
                    padding_x=2,
                    borderwidth=0),
                widget.Prompt(
                    background=bgwidgets),
                Sep,
                widget.GlobalMenu(),
                #    background=bgwidgets,
                 #   ),
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,
                    padding=-12),  
                widget.Spacer(bar.STRETCH),
                widget.TextBox(text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs, 
                    padding=-12),  
                GroupBoxx,
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,
                    padding=-12),
                widget.Spacer(
                    bar.STRETCH),
                #widget.Systray(background=bgbar), 
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,
                    padding=-12),
                ExpandingClock(
                    format="%H:%M:%S",
                    background=bgwidgets
                    ),
                widget.TextBox(text='',
                    fontsize=24,
                    foreground=bglyphs,
                    background=bgwidgets,
                    padding=-2),
            ],
            28,
            background=bgbar,
            margin=[2, 10, 0, 10]
        ),
        bottom=bar.Bar(
           [  
               widget.TextBox(
                   text='',
                   fontsize=24,
                   foreground=bglyphs,
                   background=bgwidgets,
                   padding=-2), 
               widget.ALSAWidget(background=bgwidgets),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgwidgets,
                   foreground=bglyphs,
                   padding=-12),  
               #widget.Spacer(bar.STRETCH), 
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgwidgets,
                   foreground=bglyphs,
                   padding=-2),
               widget.WindowName(
                   empty_group_string="None",
                   background=bgwidgets),
               widget.TextBox(text='',
                   fontsize=60,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-15),
               #widget.Spacer(bar.STRETCH),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-12),  
               widget.QuickExit(
                   default_text='',
                   background=bgwidgets,
                   fontsize=10), 
               widget.TextBox(
                   text='',
                   fontsize=24,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-2),
           ],
           28,
           background=bgbar,
           margin=[0, 650, 2, 650]
        ),

    ),
Screen(
        #wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    text='',
                    fontsize=24,
                    background=bgwidgets,
                    foreground=bglyphs,
                    padding=-2),
                widget.CurrentLayoutIcon(
                    background=bgwidgets),
                Sep,
                widget.Spacer(
                    length=2,
                    background=bgwidgets
                    ),
                widget.AGroupBox(
                    background=bgwidgets,
                    padding_x=2,
                    borderwidth=0),
                widget.Prompt(
                    background=bgwidgets),
                Sep,
                #widget.GlobalMenu(),
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,
                    padding=-12),  
                widget.Spacer(bar.STRETCH),
                widget.TextBox(text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs, 
                    padding=-12),
                GroupBoxx,
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,  
                    padding=-12),
                widget.Spacer(bar.STRETCH), 
                widget.TextBox(
                    text='',
                    fontsize=60,
                    background=bgwidgets,
                    foreground=bglyphs,  
                    padding=-12),
                ExpandingClock(
                    format="%H:%M:%S",
                    background=bgwidgets
                    ),
                widget.TextBox(
                    text='', 
                    fontsize=24, 
                    background=bgwidgets,
                    foreground=bglyphs,  
                    padding=-2),
           ],
            28,
            background=bgbar,
            foreground=bgwidgets,
            margin=[2, 10, 0, 10]
        ),
        bottom=bar.Bar(
           [  
               widget.TextBox(
                   text='',
                   fontsize=24,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-2), 
               widget.Mpris2(
                   name='Cider',
                   objname=None,
                   display_metadata = ['xesam:title', 'xesam:artist'],
                   stop_pause_text= 'Paused',
                   background=bgwidgets),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-12),  
               widget.Spacer(bar.STRETCH), 
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-10),
               widget.WindowName(
                   empty_group_string="None",
                   background=bgwidgets),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-15),
               widget.Spacer(bar.STRETCH),
               widget.TextBox(
                   text='',
                   fontsize=60,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-12),
               widget.Mpris2(
                   background=bgwidgets), 
               widget.TextBox(
                   text='',
                   fontsize=24,
                   background=bgwidgets,
                   foreground=bglyphs,  
                   padding=-2),
              ],
           28,
           background=bgbar,
           margin=[0, 150, 2, 150]
        ),

 )
      

]
