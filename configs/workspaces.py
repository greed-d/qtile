from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from keybinds import keys

mod = "mod4"

groups = [
    Group(
        "1",
        label=" ",
        matches=[
            Match(wm_class="zen-alpha"),
            Match(wm_class="Firefox"),
        ],
    ),
    Group(
        "2",
        label="󰄛 ",
        matches=[
            Match(wm_class="Navigator"),
        ],
    ),
    Group("3", label=""),
    Group("4", label=""),
    Group("5", label="5"),
    Group(
        "6",
        label="6",
        matches=[
            Match(wm_class="thunar"),
        ],
    ),
    Group("7", label="7"),
    Group(
        "8", label="8", matches=[Match(wm_class="spotify"), Match(wm_class="Spotify")]
    ),
    Group(
        "9", label="9", matches=[Match(wm_class="spotify"), Match(wm_class="armcord")]
    ),
]

# Magic behind groups
for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
