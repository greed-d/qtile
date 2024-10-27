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
import subprocess
from os import path

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from configs.keybinds import keys
from configs.path import qtile_path
from configs.panel import screens

mod = "mod4"


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, "autostart.sh")])


# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [
    Group(
        "1",
        label="",
        matches=[
            Match(wm_class="zen-alpha"),
            Match(wm_class="Firefox"),
        ],
    ),
    Group(
        "2",
        label="󰄛",
        matches=[
            Match(wm_class="Navigator"),
        ],
    ),
    Group("3", label=""),
    Group("4", label=""),
    Group(
        "5",
        label="",
        matches=[
            Match(wm_class="TelegramDesktop"),
            Match(wm_class="telegram-desktop"),
        ],
    ),
    Group(
        "6",
        label="󰉋",
        matches=[
            Match(wm_class="thunar"),
            Match(wm_class="Thunar"),
        ],
    ),
    Group("7", label=""),
    Group(
        "8",
        label="󰓇",
        matches=[Match(wm_class="spotify"), Match(wm_class="Spotify")],
        spawn="spotify-launcher",
    ),
    Group(
        "9",
        label="󰙯",
        matches=[
            Match(wm_class="armcord"),
            Match(wm_class="vesktop"),
        ],
        spawn="vesktop",
    ),
    Group(
        "0",
        label="",
    ),
    # ScratchPad(
    #     "`",
    #     [
    #         # define a drop down terminal.
    #         # it is placed in the upper third of screen by default.
    #         DropDown("term", "kitty", opacity=0.8),
    #         # define another terminal exclusively for ``qtile shell` at different position
    #         DropDown(
    #             "bashtop",
    #             "kitty -e btop",
    #             x=0.05,
    #             y=0.4,
    #             width=0.9,
    #             height=0.6,
    #             opacity=0.9,
    #             on_focus_lost_hide=True,
    #         ),
    #     ],
    # ),
]

# for i, group in enumerate(groups):
#     actual_key = str(i+1)
#     keys.extend(
#         [
#             Key(
#                 [mod],
#                 actual_key,
#                 lazy.spawn(f"/home/greed/.config/picom/workspace_animation.sh {actual_key}")
#
#             ),
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name),
#                 desc="move focused window to group {}".format(i.name),
#             )
#         ]
#     )

# Magic behind groups
for i in groups:
    if int(i.name) == 0:
        actual_key = int(9)
    else:
        actual_key = int(i.name) - 1

    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.spawn(
                    f"/home/greed/.config/picom/workspace_animation.sh {actual_key}"
                ),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Bsp(
        border_width=2, margin=10, border_focus="#cba6f7", border_normal="#24273A"
    ),
    layout.Max(margin=4),
    layout.Columns(margin=4, border_focus_stack=["#cba6f7", "#24273A"], border_width=3),
    layout.Matrix(margin=4),
    # layout.MonadTall(margin=4),
    # layout.MonadWide(margin=4),
    layout.Tile(margin=4),
    # layout.RatioTile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Google Sans Medium",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()


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
        Match(wm_class="xdm-app"),  # ssh-askpass
        Match(wm_class="Xdm-app"),  # ssh-askpass
        Match(wm_class="nwg-look"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Download Complete"),  # GPG key password entry
        Match(title="Delete profile"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
