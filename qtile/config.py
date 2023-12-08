                                                                                                                                                           
# _______ _    _ _____  ______ ______ _______ _____ _      ______ 
#|__   __| |  | |  __ \|  ____|  ____|__   __|_   _| |    |  ____|
#   | |  | |__| | |__) | |__  | |__     | |    | | | |    | |__   
#   | |  |  __  |  _  /|  __| |  __|    | |    | | | |    |  __|  
#   | |  | |  | | | \ \| |____| |____   | |   _| |_| |____| |____ 
#   |_|  |_|  |_|_|  \_\______|______|  |_|  |_____|______|______|
#                                                                                                                                                                 
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#  __  __               _   _ _                         __ _         _
# |  \/  |             | | (_) |                       / _(_)       | |
# | \  / |_   _    __ _| |_ _| | ___    ___ ___  _ __ | |_ _  __ _  | |
# | |\/| | | | |  / _` | __| | |/ _ \  / __/ _ \| '_ \|  _| |/ _` | | |
# | |  | | |_| | | (_| | |_| | |  __/ | (_| (_) | | | | | | | (_| | |_|
# |_|  |_|\__, |  \__, |\__|_|_|\___|  \___\___/|_| |_|_| |_|\__, | (_)
#          __/ |     | |                                      __/ |
#         |___/      |_|                                     |___/
#
#
#
#
#
#
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#####################################
# ---------- @@@@@@@@@@@ ---------- #
# ---------- @ IMPORTS @ ---------- #
# ---------- @@@@@@@@@@@ ---------- #
#####################################

import colors
import os
import time
import subprocess
from libqtile import qtile
from libqtile import bar, layout, hook, extension
from libqtile.widget import base
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.config import EzKey as Key2
from datetime import datetime 
from qtile_extras import widget 
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupText, PopupWidget
from qtile_extras.widget.mixins import ExtendedPopupMixin
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration, BorderDecoration



######################################
# ----------@@@@@@@@@@@@@ ---------- #
# ----------@ VARIABLES @ ---------- #
# ----------@@@@@@@@@@@@@ ---------- #
######################################

#KEYS
mod = "mod4"
alt = "mod1"

#PATHS
home = os.path.expanduser("~")

rofi_path_dmenu1 = home + "/.config/rofi/launchers/type-1/launcher.sh"
rofi_path_dmenu2 = home + "/.config/rofi/launchers/type-2/launcher.sh"
rofi_path_dmenu3 = home + "/.config/rofi/launchers/type-3/launcher.sh"
rofi_path_dmenu4 = home + "/.config/rofi/launchers/type-4/launcher.sh"
rofi_path_dmenu5 = home + "/.config/rofi/launchers/type-5/launcher.sh"
rofi_path_dmenu6 = home + "/.config/rofi/launchers/type-6/launcher.sh"
rofi_path_dmenu7 = home + "/.config/rofi/launchers/type-7/launcher.sh"
rofi_path_powermenu1 = home + "/.config/rofi/powermenu/type-1/powermenu.sh"
rofi_path_powermenu2 = home + "/.config/rofi/powermenu/type-2/powermenu.sh"
rofi_path_powermenu3 = home + "/.config/rofi/powermenu/type-3/powermenu.sh"
rofi_path_powermenu4 = home + "/.config/rofi/powermenu/type-4/powermenu.sh"
rofi_path_powermenu5 = home + "/.config/rofi/powermenu/type-5/powermenu.sh"
rofi_path_powermenu6 = home + "/.config/rofi/powermenu/type-6/powermenu.sh"

#APPS
terminal = "kitty"
browser = "librewolf"
browser2 = "brave"
file_browser = "thunar"
dc = "discord"
obi = "obsidian"
vs = "vscodium"
music = "spotify"
film = "freetube"
em = "emacs"
nv = "kitty -e nvim"
wall = "nitrogen"
mail = "thunderbird"
#terminal = guess_terminal()


###################
#COLORS AND THEMES#  
###################

colors = colors.DoomOne

# If using transparency, make sure you add (background="#00000000") to 'Screen' line(s).
# Then, you can use RGBA color codes to add transparency to the colors below.
# For ex: colors = [["#282c34ee", "#282c34dd"], ...

DoomOne = [
    ["#282c34", "#282c34"], # bg
    ["#bbc2cf", "#bbc2cf"], # fg
    ["#1c1f24", "#1c1f24"], # color01
    ["#ff6c6b", "#ff6c6b"], # color02
    ["#98be65", "#98be65"], # color03
    ["#da8548", "#da8548"], # color04
    ["#51afef", "#51afef"], # color05
    ["#c678dd", "#c678dd"], # color06
    ["#46d9ff", "#46d9ff"]  # color15
    ]

Dracula  = [
    ["#282a36", "#282a36"], # bg
    ["#f8f8f2", "#f8f8f2"], # fg
    ["#000000", "#000000"], # color01
    ["#ff5555", "#ff5555"], # color02
    ["#50fa7b", "#50fa7b"], # color03
    ["#f1fa8c", "#f1fa8c"], # color04
    ["#bd93f9", "#bd93f9"], # color05
    ["#ff79c6", "#ff79c6"], # color06
    ["#9aedfe", "#9aedfe"]  # color15
    ]

GruvboxDark  = [
    ["#282828", "#282828"], # bg
    ["#ebdbb2", "#ebdbb2"], # fg
    ["#000000", "#000000"], # color01
    ["#fb4934", "#fb4934"], # color02
    ["#98971a", "#98971a"], # color03
    ["#d79921", "#d79921"], # color04
    ["#83a598", "#83a598"], # color05
    ["#d3869b", "#d3869b"], # color06
    ["#b8bb26", "#b8bb26"], # color11
    ]
MonokaiPro = [
    ["#2D2A2E", "#2D2A2E"], # bg
    ["#FCFCFA", "#FCFCFA"], # fg
    ["#403E41", "#403E41"], # color01
    ["#FF6188", "#FF6188"], # color02
    ["#A9DC76", "#A9DC76"], # color03
    ["#FFD866", "#FFD866"], # color04
    ["#FC9867", "#FC9867"], # color05
    ["#AB9DF2", "#AB9DF2"], # color06
    ["#78DCE8", "#78DCE8"]  # color07
    ]

Nord = [
    ["#2E3440", "#2E3440"], # bg
    ["#D8DEE9", "#D8DEE9"], # fg
    ["#3B4252", "#3B4252"], # color01
    ["#BF616A", "#BF616A"], # color02
    ["#A3BE8C", "#A3BE8C"], # color03
    ["#EBCB8B", "#EBCB8B"], # color04
    ["#81A1C1", "#81A1C1"], # color05
    ["#B48EAD", "#B48EAD"], # color06
    ["#88C0D0", "#88C0D0"]  # color07
    ]

OceanicNext = [
    ["#1b2b34", "#1b2b34"], # bg
    ["#d8dee9", "#d8dee9"], # fg
    ["#29414f", "#29414f"], # color01
    ["#ec5f67", "#ec5f67"], # color02
    ["#99c794", "#99c794"], # color03
    ["#fac863", "#fac863"], # color04
    ["#6699cc", "#6699cc"], # color05
    ["#c594c5", "#c594c5"], # color06
    ["#5fb3b3", "#5fb3b3"]  # color07
    ]

Palenight = [
    ["#292d3e", "#292d3e"], # bg
    ["#d0d0d0", "#d0d0d0"], # fg
    ["#434758", "#434758"], # color01
    ["#f07178", "#f07178"], # color02
    ["#c3e88d", "#c3e88d"], # color03
    ["#ffcb6b", "#ffcb6b"], # color04
    ["#82aaff", "#82aaff"], # color05
    ["#c792ea", "#c792ea"], # color06
    ["#89ddff", "#89ddff"]  # color15
    ]

SolarizedDark = [
    ["#002b36", "#002b36"], # bg
    ["#839496", "#839496"], # fg
    ["#073642", "#073642"], # color01
    ["#dc322f", "#dc322f"], # color02
    ["#859900", "#859900"], # color03
    ["#b58900", "#b58900"], # color04
    ["#268bd2", "#268bd2"], # color05
    ["#d33682", "#d33682"], # color06
    ["#2aa198", "#2aa198"]  # color15
    ]

SolarizedLight = [
    ["#fdf6e3", "#fdf6e3"], # bg
    ["#657b83", "#657b83"], # fg
    ["#ece5ac", "#ece5ac"], # color01
    ["#dc322f", "#dc322f"], # color02
    ["#859900", "#859900"], # color03
    ["#b58900", "#b58900"], # color04
    ["#268bd2", "#268bd2"], # color05
    ["#d33682", "#d33682"], # color06
    ["#2aa198", "#2aa198"]  # color15
    ]

TomorrowNight = [
    ["#1d1f21", "#1d1f21"], # bg
    ["#c5c8c6", "#c5c8c6"], # fg
    ["#373b41", "#373b41"], # color01
    ["#cc6666", "#cc6666"], # color02
    ["#b5bd68", "#b5bd68"], # color03
    ["#e6c547", "#e6c547"], # color04
    ["#81a2be", "#81a2be"], # color05
    ["#b294bb", "#b294bb"], # color06
    ["#70c0ba", "#70c0ba"]  # color15
    ]

TokyoNight = {
    "black": ["#0F0F1C", "#1A1C31"],
    "red": ["#D22942", "#DE4259"],
    "green": ["#17B67C", "#3FD7A0"],
    "yellow": ["#F2A174", "#EEC09F"],
    "blue": ["#8B8AF1", "#A7A5FB"],
    "magenta": ["#D78AF1", "#E5A5FB"],
    "cyan": ["#4FCFEB", "#82E3F8"],
    "grey": ["#B4C0EC", "#B4C0EC"],
    "white": ["#CAD3F5", "#CAD3F5"],
    }


tokyo_black = "#0F0F1C"
tokyo_light_black = "#1A1C31"
tokyo_red = "#D22942"
tokyo_light_red = "#DE4259"
tokyo_green = "#17B67C"
tokyo_light_green = "#3FD7A0"
tokyo_yellow = "#F2A174"
tokyo_light_yellow = "#EEC09F"
tokyo_blue = "#8B8AF1"
tokyo_light_blue = "#A7A5FB"
tokyo_magenta = "#D78AF1"
tokyo_light_magenta = "#E5A5FB"
tokyo_cyan = "#4FCFEB"
tokyo_light_cyan = "#82E3F8"
tokyo_grey = "#B4C0EC"
tokyo_white = "#CAD3F5"

#Catppuccin

cat_mauve = "#DDB6F2"
cat_pink = "#F5C2E7"
cat_maroon = "#E8A2AF"
cat_red = "#F28FAD"
cat_peach = "#F8BD96"


#Solarized Dark
sol_base00 = "#657b83"
sol_base0 = "#839496"
sol_base01 = "#586e75"
sol_base02 = "#073642"
sol_base03 = "#002b36"
sol_base1 = "#93a1a1"
sol_base2 = "#eee8d5"
sol_base3 = "#fdf6e3"
sol_yellow = "#b58900"
sol_orange ="#cb4b16"
sol_red ="#dc322f"
sol_magenta ="#d33682"
sol_violet = "#6c71c4"
sol_blue = "#268bd2"
sol_cyan = "#2aa198"
sol_green = "#859900"
sol_dark_green = "1D1D1D"








###################################################
# --------------- @@@@@@@@@@@@@@@ --------------- #
# --------------- @ KEYBINDINGS @ --------------- #
# --------------- @@@@@@@@@@@@@@@ --------------- #
###################################################

keys = [

    ########################
    #SWITCH BETWEEN WINDOWS#
    ########################
    Key(
        [mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),

    Key(
        [mod], "l", 
        lazy.layout.right(),
        desc="Move focus to right"
    ),

    Key(
        [mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"
    ),

    Key(
        [mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"),
    Key(
        [mod], "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
    ),


    #############
    #MOVE WINDOW#
    #############
    Key(
        [mod, "shift"], "h", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"
    ),

    Key(
        [mod, "shift"], "l",
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
    ),

    Key(
        [mod, "shift"], "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
    ),

    Key(
        [mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
    ),


    #############
    #GROW WINDOW#
    #############
    Key(
        [mod, "control"], "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
    ),

    Key(
        [mod, "control"], "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
    ),

    Key(
        [mod, "control"], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),

    Key(
        [mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),

    Key(
        [mod], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ),

    Key(
        [mod, "shift"], "Return", 
        lazy.layout.toggle_split(), 
        desc="Toggle between split and unsplit sides of stack"
    ),

    Key(
        [mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
    ),

    #############
    #SCREENSHOTS#
    #############
    Key(
        [mod, "shift"], "p", 
        lazy.spawn("flameshot"), 
        desc="Launch Flameshot"
    ),

    Key(
        [mod, alt], "p", 
        lazy.spawn("scrot 'Screenshot_%Y-%m-%d_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) ; viewnior $$(xdg-user-dir PICTURES)/$f'"), 
        desc="Takes a Screenshot"
    ),


    #############
    #LAUNCH APPS#
    #############
    Key(
        [mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),

    Key(
        [mod], "w", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),

    Key(
        [mod, "shift"], "b", 
        lazy.spawn(browser2), 
        desc="Launch Brave"
    ),

    Key(
        [mod, "shift"], "l", 
        lazy.spawn(browser), 
        desc="Launch LibreWolf"
    ),

    Key(
        [mod, "shift"], "t", 
        lazy.spawn(file_browser), 
        desc="Launch file browser"
    ),

    Key(
        [mod, "shift"], "o", 
        lazy.spawn(obi), 
        desc="Launch Obsidian"
    ),

    Key([mod, "shift"], "d", 
        lazy.spawn(dc), 
        desc="Launch Discord"
    ),

    Key(
        [mod, "shift"], "s", 
        lazy.spawn(music), 
        desc="Launch Spotify"
    ),

    Key(
        [mod, "shift"], "y", 
        lazy.spawn(film), 
        desc="Launch FreeTube"
    ),

    Key(
        [mod, "shift"], "v", 
        lazy.spawn(vs), 
        desc="Launch VSCodium"
    ),

    Key(
        [mod, "shift"], "e", 
        lazy.spawn(em), 
        desc="Launch Emacs"
    ),

    Key(
        [mod, "shift"], "n", 
        lazy.spawn(nv), 
        desc="Launch Neovim"
    ),

    Key(
        [mod, "shift"], "w", 
        lazy.spawn(wall), 
        desc="Launch Nitrogen"
    ),

    Key(
        [mod, "shift"], "m", 
        lazy.spawn(mail), 
        desc="Launch Thunderbird"
    ),


    ######
    #MISC#
    ######
    Key(
        [mod], "f", 
        lazy.window.toggle_fullscreen(), 
        desc="Toggle fullscreen on the focused window"
    ),

    Key(
        [mod], "t", 
        lazy.window.toggle_floating(), 
        desc="Toggle floating on the focused window"
    ),

    Key(
        [mod, "control"], "r", 
        lazy.reload_config(), 
        desc="Reload the config"
    ),

    Key(
        [mod, "control"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),

    Key(
        [mod], "r", 
        lazy.spawn(rofi_path_dmenu2), 
        desc="Launch dmenu"
    ),

    Key(
        [mod], "p", 
        lazy.spawn(rofi_path_powermenu2), 
        desc="Launch powermenu"
    ),

    #Key(
    #    [mod], "r", 
    #    lazy.spawn("rofi -show drun -show-icons"), 
    #    desc="Launch rofi app-launcher"
    #),

    Key(
        [mod], "l", 
        lazy.spawn("betterlockscreen -l"), 
        desc="Lock screen"
    ),


    #######
    #AUDIO#
    #######
    Key(
        [], "XF86AudioRaiseVolume", 
        lazy.spawn("amixer -D pulse sset Master 1%+"),
        desc="Raise volume"
    ),

    Key(
        [], "XF86AudioLowerVolume", 
        lazy.spawn("amixer -D pulse sset Master 1%-"),
        desc="Lower volume"
    ),

    Key(
        [], "XF86AudioMute", 
        lazy.spawn("amixer set Master toggle"),
        desc="Mute"
    ),
]



####################################
# ---------- @@@@@@@@@@ ---------- #
# ---------- @ GROUPS @ ---------- #
# ---------- @@@@@@@@@@ ---------- #
####################################


groups = [
    Group(
        "1", 
        matches=[Match(wm_class=["LibreWolf"])],
        spawn=browser, label=""
    ),

    Group(
        "2",
        matches=[Match(wm_class=["VSCodium"])],
        label=""
    ),

    Group(
        "3", 
        matches=[Match(wm_class=["obsidian"])], 
        label=""
    ),

    Group(
        "4",
        matches=[Match(wm_class=["FreeTube"])], 
        label=""
    ),

    Group(
        "5",
        matches=[Match(wm_class=["Thunar"])], 
        label=""
    ),

    Group(
        "6",
        matches=[Match(wm_class=["Spotify"])], 
        label=""
    ),

    Group(
        "7", 
        matches=[Match(wm_class=["discord", "Signal"])], 
        spawn=dc, label=""
    ),
]

#Labels
# "߷"
# "֎"
# "০"
# "১"
# "২"
# "ೱ"
# "࿋"
# "࿌"
# "᳃"
# "⌘"
# "" Firefox
# "" Terminal
# "", ""Spotify
# "" Thunar
# "" Code
# "" Server
# "" Games
# "" Media


#groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )



#############
#  LAYOUTS  #
#############

layouts = [
    #layout.Columns(
    #    border_focus=tokyo_grey, 
    #    border_normal=tokyo_black, 
    #    border_on_single=True, 
    #    border_width=3,
    #    margin=10
    #),
    layout.MonadThreeCol(
        border_focus=tokyo_grey,
        border_normal=tokyo_light_black,
        border_width=3,
        border_on_single=True,
        margin=10
    ),


    #layout.Max(
    #    border_focus=tokyo_grey,
    #    border_normal=tokyo_black,
    #    border_width=3,
    #    margin=10
    #),

    #layout.Stack(
    #    num_stacks=2,
    #    border_focus=tokyo_grey,
    #    border_normal=tokyo_black,
    #    border_width=3,
    #    margin=10
    #),

    # layout.Bsp(),

    # layout.Matrix(),

    layout.MonadTall(
        border_focus=tokyo_grey,
        border_normal=tokyo_light_black,
        border_width=3,
        margin=10
    ),

    # layout.MonadWide(),

    # layout.RatioTile(),

    # layout.Slice(),

    layout.Spiral(
        border_focus=tokyo_grey,
        border_normal=tokyo_light_black,
        border_width=3,
        margin=10
    ),

    # layout.Stack(),

    # layout.Tile(),

    layout.TreeTab(),

    # layout.VerticalTile(),

    # layout.Zoomy(),

    layout.Floating(
        border_focus=tokyo_grey,
        border_normal=tokyo_light_black,
        border_width=3,
        fullscreen_border_width=3
    ),

]



#################################
# ---------- @@@@@@@ ---------- #
# ---------- @ BAR @ ---------- #
# ---------- @@@@@@@ ---------- #
#################################

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def open_neofetch(qtile):
    qtile.cmd_spawn('kitty -e neofetch')



def init_widgets_list():
    widgets_list = [
            widget.Spacer(
                length = 2,
                background = tokyo_light_black 
            ),

            widget.Image(
                filename = "~/.config/qtile/archlogo.png",
                background = tokyo_light_black,
                margin = 3,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(
                        f'{terminal} -e nvim {home}/.config/qtile/config.py'
                    )
                },
                #mouse_callbacks = {
                #  'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e bash-pipes")
                #}
            ),

            widget.Spacer(
                length = 20,
                background = tokyo_light_black,
            ),

            widget.GroupBox(
                font = "Iosevka Nerd Font",
                fontsize = 18,
                foreground = sol_red,
                background = tokyo_light_black,
                borderwidth = 8,
                highlight_method = "block",
                this_current_screen_border = tokyo_blue,
                inactive = sol_base3,
                active = sol_orange,
            ),

            widget.Spacer(
                length = 20,
                background = tokyo_light_black,
            ),

            widget.WindowName(
                background = tokyo_light_black,
                foreground = sol_base3,
                empty_group_string = "",
                fontsize = 15,
                decorations = [
                    PowerLineDecoration(path="arrow_right") 
                ]
            ),

            #widget.Spacer(
            #    length = 70,
            #    background = tokyo_light_magenta,
            #    decorations = [
            #        PowerLineDecoration()
            #    ]
            #),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_light_black
            #),

            widget.Spacer(
                length = 10,
                background = tokyo_light_black,
                decorations = [
                    PowerLineDecoration(path="arrow_right") 
                ]

            ),
            #widget.Spacer(
            #   length = 10,
            #    background =sol_base03, 
            #    decorations = [
            #        PowerLineDecoration(path="arrow_right") 
            #    ]
#
#            ),
            #widget.Image(
            #    filename = "~/.config/qtile/volume.png",
            #    background = tokyo_light_cyan,
            #    foreground = tokyo_grey,
            #    margin = 3,
            #    decorations = [
            #        PowerLineDecoration()
            #    ]
            #),
            widget.NvidiaSensors(
                foreground = sol_base3,
                fmt = "GPU: {}",
                background = cat_mauve,
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            widget.Volume(
                foreground = sol_base3,
                background = cat_peach,
                fmt = '🕫  Vol: {}',
                #emoji = True, 
                #emoji_list = ['🔇', '🔈', '🔉', '🔊'],
                fontsize = 15,
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            #widget.Spacer(
            #    length = 10,
            #    background = tokyo_light_black
            #),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_light_black
            #),

            widget.CurrentLayout(
                foreground = sol_base3,
                background = tokyo_green,
                fontsize = 15,
                padding = 10,
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_light_black
            #),

            #widget.Spacer(
            #    length = 10,
            #    background = tokyo_light_black
            #),

            widget.Image(
                filename = "~/.config/qtile/cpu.png",
                background = sol_cyan,
                foreground = tokyo_cyan,
                margin = 3,

           ),

            widget.CPU(
                format = "{load_percent}% ",
                foreground = sol_base3, 
                background = sol_cyan,
                fontsize = 15,
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e gtop")
                },
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            #widget.Spacer(
            #    length = 10,
            #    background = tokyo_light_black
            #),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_light_black
            #),

            #widget.Spacer(
            #     length = 10,
            #     background = tokyo_light_black
            #),

            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 17,
                text = "",
                #text= "",
                foreground = sol_base2,
                background = sol_red,
            ),

            widget.Memory(
                background = sol_red,
                foreground = sol_base3,
                fontsize = 15,
                mouse_callbacks = {
                  'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e htop")
                },
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            #widget.MemoryGraph(
            #    background = tokyo_light_black,
            #    graph_color = tokyo_magenta,
            #    fill_color = tokyo_magenta,
            #    border_color = tokyo_black,
            #    mouse_callbacks = {
            #      'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e htop")
            #    }
            #),

            #widget.Spacer(
            #    length = 10,
            #    background = tokyo_light_black
            #),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_grey
            #),

            #widget.Spacer(
            #    length = bar.STRETCH,
            #    background = sol_base01,
            #    decorations = [
            #        PowerLineDecoration()
            #    ]
            #),

            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = sol_base3,
                background = sol_violet
            ),

            widget.Net(
                format = "{down} ↓↑ {up}",
                foreground = sol_base3,
                background = sol_violet,
                update_interval = 2,
                #mouse_callbacks = {
                #    'Button1': lambda : qtile.cmd_spawn(f"networkmanager_dmenu {dmenu_conf}")
                #}
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            #widget.Sep(
            #    size_percent = 60,
            #    linewidth = 3,
            #    background = tokyo_light_black
            #),

            #widget.Spacer(
            #    length = 5,
            #    background = tokyo_light_black
            #),

            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = sol_base3,
                background = sol_blue,
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            widget.Clock(
                format = '%b %d-%Y',
                foreground = sol_base3,
                background = sol_blue,
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = sol_base3,
                background = sol_yellow
            ),

            widget.Clock(
                format = '%I:%M:%S %p',
                foreground = sol_base3,
                background = sol_yellow,
                decorations = [
                    PowerLineDecoration(path="arrow_right")
                ]
            ),

            widget.Systray(
                background = sol_magenta 
            ),

            widget.Spacer(
                length = 5,
                background =sol_magenta 
            )
        ]
    return widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), size=30, opacity=0.9, margin=[5,10,0,10]))]

screens = init_screens()
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,

# Drag floating layouts.
mouse = [
    Drag(
        [mod], "Button1", 
        lazy.window.set_position_floating(), 
        start=lazy.window.get_position()
    ),

    Drag(
        [mod], "Button3", 
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),

    Click(
        [mod], "Button2", 
        lazy.window.bring_to_front()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=tokyo_grey,
    border_normal=tokyo_light_black,
    border_width=3,
    fullscreen_border_width=3
        
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


#################################################
# ---------- @@@@@@@@@@@@@@@@@@@@@@@ ---------- #
# ---------- @ HOOKS AND AUTOSTART @ ---------- #
# ---------- @@@@@@@@@@@@@@@@@@@@@@@ ---------- #
#################################################

@hook.subscribe.startup_once
def autostart():
    auto_home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([auto_home])
    time.sleep(2)
    subprocess.call(["picom", "--experimental-backends", "-b"])












# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
