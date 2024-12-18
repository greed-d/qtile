from libqtile import layout
from libqtile.config import (
    Click,
    Drag,
    Key,
    KeyChord,
)
from libqtile.lazy import lazy
from libqtile.widget import backlight
from qtile_extras.popup.templates.mpris2 import COMPACT_LAYOUT, DEFAULT_LAYOUT

mod = "mod4"
terminal = "ghostty"
file_manager = "thunar"

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
keys = [
    # Key([mod], "x", lazy.group["scratchpad"].dropdown_toggle("term")),
    # Key([], "F12", lazy.group["scratchpad"].dropdown_toggle("bashtop")),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.widget["backlight"].change_backlight(backlight.ChangeDirection.UP),
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.widget["backlight"].change_backlight(backlight.ChangeDirection.DOWN),
    ),
    Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("wpctl set-volume -l 1.5 @DEFAULT_AUDIO_SINK@ 5%+"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),
    ),
    Key(
        [],
        "XF86AudioMedia",
        lazy.spawn("playerctl play-pause"),
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
    ),
    Key(
        [],
        "XF86AudioStop",
        lazy.spawn("playerctl stop"),
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl prev"),
    ),
    Key(
        [mod],
        "m",
        lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"),
    ),
    # Key([mod], "p", lazy.widget["mpris2"].toggle_player()),
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "i", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.spawn("betterlockscreen -l", shell=True),
        desc="Move window to the left",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "mod1"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "mod1"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "mod1"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "mod1"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "backslash", lazy.window.toggle_maximize(), desc="Mimic monocle mode"),
    # Toggle between split and unsplit sides of stack. Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    KeyChord(
        [mod],
        "z",
        [
            Key([], "g", lazy.layout.grow()),
            Key([], "s", lazy.layout.shrink()),
            Key([], "n", lazy.layout.normalize()),
            Key([], "m", lazy.layout.maximize()),
        ],
        mode=True,
        name="Windows",
    ),  # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Launch File Manager"),
    Key([mod], "v", lazy.spawn("clipmenu"), desc="Launch File Manager"),
    Key(
        [mod],
        "t",
        lazy.spawn("kill -s USR1 $(pidof deadd-notification-center)", shell=True),
        desc="Show notification center",
    ),
    Key(
        [],
        "print",
        lazy.spawn(
            "/home/greed/.local/scripts/screenshot.sh --screenshot",
            shell=True,
        ),
        desc="Launch File Manager",
    ),
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn(
            "/home/greed/.local/scripts/screenshot.sh --screen-selection-buffer",
            shell=True,
        ),
    ),
    Key(
        [mod, "shift"],
        "q",
        lazy.spawn(
            "shutdown now",
            shell=True,
        ),
    ),
    Key(
        [mod, "mod1"],
        "s",
        lazy.spawn(
            "maim | xclip -selection clipboard -t image/png && notify-send 'Screenshot' 'Screenshot copied to buffer'",
            shell=True,
        ),
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "s",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "space",
        lazy.spawn(
            "pkill rofi || rofi -show drun -theme ~/.config/rofi/catppuccin.qtile.rasi",
            shell=True,
        ),
        desc="Spawn a command using a prompt widget",
    ),
]
