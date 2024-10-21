from libqtile import bar, widget
from libqtile.config import Screen
from qtile_extras import widget as ex_widget
from qtile_extras.popup.templates.mpris2 import DEFAULT_LAYOUT
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.groupbox2 import GroupBoxRule
from configs.window_map import CustomWindowName

decoration_group = {
    "decorations": [
        RectDecoration(colour="#1e1e2e", radius=6, filled=True, padding_y=5, group=True)
    ],
    "padding": 10,
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=7),
                CustomWindowName(foreground="#f2cdcd", **decoration_group),
                widget.Spacer(length=7),
                # CustomMpris2(
                #     foreground="#cba6f7",  # Customize foreground color
                #     max_chars=30,  # Adjust character limit for display
                #     **decoration_group,  # Apply decorations if needed
                # ),
                ex_widget.Mpris2(
                    foreground="#cba6f7",
                    max_chars=30,
                    paused_text="   {track}",
                    format="{xesam:player} {xesam:title}",
                    popup_layout=DEFAULT_LAYOUT,
                    **decoration_group,
                ),
                widget.Spacer(length=7),
                ex_widget.CPU(
                    foreground="#f38ba8",
                    format="   {load_percent}%",
                    **decoration_group,
                ),
                widget.Spacer(length=7),
                ex_widget.Systray(margin_x=40, **decoration_group),
                widget.Spacer(),
                ex_widget.GroupBox2(
                    padding_x=10,
                    fontsize=16,
                    highlight_method="border",
                    width=1,
                    rules=[
                        GroupBoxRule(
                            text_colour="#a6e3a1", line_colour="#a6e3a1", line_width=4
                        ).when(screen=GroupBoxRule.SCREEN_THIS),
                        GroupBoxRule(text_colour="#89b4fa").when(occupied=True),
                        GroupBoxRule(text_colour="#585b70"),
                    ],
                    **decoration_group,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(),
                ex_widget.CheckUpdates(
                    colour_have_updates="#f38ba8",
                    colour_no_updates="#cba6f7",
                    no_update_string="Fully Updated!",
                    distro="Arch_checkupdates",
                    display_format="   {updates} Updates",
                    **decoration_group,
                ),
                widget.Spacer(length=7),
                ex_widget.Memory(
                    foreground="#f9e2af",
                    format="  {MemPercent}%",
                    **decoration_group,
                ),
                widget.Spacer(length=7),
                ex_widget.Wlan(
                    foreground="#cba6f7",
                    show_image=True,
                    show_text=True,
                    **decoration_group,
                ),
                widget.Spacer(length=7),
                ex_widget.CurrentLayout(foreground="#89dceb", **decoration_group),
                widget.Spacer(length=7),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                ex_widget.Clock(
                    foreground="#fab387", format="󰥔  %H:%M:%S", **decoration_group
                ),
                widget.Spacer(length=7),
                ex_widget.ScriptExit(
                    default_text="[ 󰐥 ]",
                    countdown_format="[Loggin out in : {} secs]",
                    **decoration_group,
                ),
                widget.Spacer(length=7),
            ],
            40,
            background="#45475a",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            margin=7,
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]
