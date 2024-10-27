from libqtile import bar, widget
import os
from libqtile.lazy import lazy
from libqtile.config import Screen
from qtile_extras import widget as ex_widget
from configs.components.power_menu import show_power_menu

# from qtile_extras.popup.templates.mpris2 import DEFAULT_LAYOUT

from configs.components.mpris2_popup import DEFAULT_LAYOUT
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.groupbox2 import GroupBoxRule

from configs.components.window_map import CustomWindowName

# from configs.window_map import CustomWindowName

# from configs.volume_widget import VOLUME_NOTIFICATION

# from configs.mpris_custom import CustomMprisWidget


# Dictionary mapping player names to their icons
# You can customize these icons based on your needs
def draw_bottom_line_margin(line_colour="fff", line_width=2, margin=0):
    def _wrapper(box):
        ctx = box.drawer.ctx
        ctx.set_line_width(line_width)
        ctx.new_sub_path()
        ctx.move_to(0, box.bar.height - margin + 2)
        ctx.line_to(box.size, box.bar.height - margin + 2)
        box.drawer.set_source_rgb(line_colour)
        ctx.stroke()

    return _wrapper


ws_decoration = {
    "decorations": [
        RectDecoration(
            colour="#242438",
            radius=9,
            filled=True,
            padding_y=5,
            group=True,
            line_colour="#F5C2E7",
            line_width=1,
        ),
    ],
    "padding": 10,
}
layout_group = {
    "decorations": [
        RectDecoration(
            colour="#242438",
            radius=9,
            filled=True,
            padding_y=5,
            # margin_x=7,
            group=True,
        )
    ],
    # "padding": 10,
}

decoration_group = {
    "decorations": [
        RectDecoration(colour="#242438", radius=9, filled=True, padding_y=5, group=True)
    ],
    "padding": 10,
}
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=7),
                ex_widget.CurrentLayoutIcon(
                    scale=0.4,
                    width=26,
                    **decoration_group,
                ),
                # ex_widget.CurrentLayout(
                #     foreground="#a6e3a1", padding=10, **layout_group
                # ),
                widget.Spacer(length=7),
                CustomWindowName(
                    foreground="#f2cdcd", max_chars=30, **decoration_group
                ),
                # ex_widget.WindowName(width=200, **decoration_group),
                widget.Spacer(length=7),
                # CustomMpris2(
                #     name="mpris2",
                #     foreground="#cba6f7",
                #     width=200,
                #     max_chars=30,
                #     display_metadata=["xesam:title"],  # Only show title
                #     stopped_text="No player",
                #     popup_layout=DEFAULT_LAYOUT,
                #     popup_show_args={
                #         "relative_to": 2,
                #         "relative_to_bar": True,
                #         "x": -700,
                #     },
                #     mouse_callbacks={"Button1": lazy.widget["mpris2"].toggle_player()},
                #     **decoration_group,
                # ),
                # CustomMprisWidget(
                #     foreground="#cba6f7",
                #     max_chars=30,
                #     stopped_text="No music",
                #     popup_layout=DEFAULT_LAYOUT,
                #     popup_show_args={
                #         "relative_to": 2,
                #         "relative_to_bar": True,
                #         "x": -700,
                #     },
                #     **decoration_group,
                # ),
                ex_widget.Mpris2(
                    foreground="#cba6f7",
                    max_chars=30,
                    paused_text="   {track}",
                    format="{xesam:title}",
                    # format=lambda text, data: f"{get_player_icon(data.get('qtile:player', ''))} {data.get('xesam:title', '')}",
                    popup_layout=DEFAULT_LAYOUT,
                    popup_show_args={
                        "relative_to": 2,
                        "relative_to_bar": True,
                        "x": -700,
                        "y": 0,
                    },
                    stopped_text="󰝚  Media",
                    mouse_callbacks={"Button1": lazy.widget["mpris2"].toggle_player()},
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
                widget.Spacer(length=7),
                ex_widget.CheckUpdates(
                    colour_have_updates="#fab387",
                    colour_no_updates="#cba6f7",
                    no_update_string="   Fully Updated!",
                    distro="Arch_checkupdates",
                    display_format="   {updates} Updates",
                    **decoration_group,
                ),
                widget.Spacer(),
                ex_widget.GroupBox2(
                    padding_x=12,
                    fontsize=16,
                    highlight_method="line",
                    width=1,
                    rules=[
                        GroupBoxRule(
                            text_colour="#a6e3a1",
                            custom_draw=draw_bottom_line_margin(
                                line_colour="#a6e3a1",
                                # line_width=2,
                                margin=10,
                            ),
                        ).when(screen=GroupBoxRule.SCREEN_THIS),
                        GroupBoxRule(text_colour="#89b4fa").when(occupied=True),
                        # GroupBoxRule(text_colour="#ff00ff").when(
                        #     group_name="3", occupied=True
                        # ),
                        GroupBoxRule(text_colour="#585b70"),
                    ],
                    **ws_decoration,
                ),
                widget.Spacer(length=7),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    **decoration_group,
                ),
                widget.Spacer(),
                # ex_widget.PulseVolume(emoji=True, hide_after=0.5, **decoration_group),
                ex_widget.Memory(
                    foreground="#f9e2af",
                    format="  {MemPercent}%",
                    **decoration_group,
                ),
                widget.Spacer(length=7),
                # ex_widget.IWD(show_image=True, **decoration_group),
                ex_widget.Wlan(
                    foreground="#cba6f7",
                    scale=0.5,
                    show_image=True,
                    show_text=True,
                    format="󰤨   {essid} ({percent:2.0%})",
                    **decoration_group,
                ),
                widget.Spacer(length=7),
                ex_widget.PulseVolumeExtra(
                    mode="both",
                    icon_size=20,
                    bar_colour_normal="#a6e3a1",
                    bar_colour_loud="#f38ba8",
                    bar_colour_high="#fab387",
                    bar_text_foreground="#585b70",
                    bar_width=70,
                    bar_height=17,
                    hide_after=1,
                    theme_path="~/.config/qtile/audio-icon-svg",
                    **decoration_group,
                ),
                # ex_widget.PulseVolumeExtra(
                #     popup_layout=VOLUME_NOTIFICATION,
                #     # mouse_callbacks={"Button1": lazy.widget[""].toggle_player()},
                # ),
                widget.Spacer(length=7),
                ex_widget.BatteryIcon(
                    theme_path="~/.config/qtile/battery-icons-svg",
                    foreground="#f5c2e7",
                    width=47,
                    scale=2.5,
                    # padding=5,
                    **layout_group,
                ),
                ex_widget.Battery(
                    # padding=10,
                    width=45,
                    foreground="#f5c2e7",
                    format="{percent:2.0%}",
                    **layout_group,
                ),
                widget.Spacer(length=7),
                ex_widget.Backlight(
                    foreground="#f9e2af",
                    backlight_name="amdgpu_bl1",
                    change_command="brightnessctl set {0}%",
                    format="   {percent:2.0%}",
                    **decoration_group,
                ),
                widget.Spacer(length=7),
                # ex_widget.BrightnessControl(
                #     device="/sys/class/backlight/amdgpu_bl1",
                #     **decoration_group,
                # ),
                # widget.Spacer(length=7),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                ex_widget.Clock(
                    foreground="#fab387", format="󰥔  %H:%M:%S", **decoration_group
                ),
                widget.Spacer(length=7),
                # ex_widget.ScriptExit(
                #     default_text="[ 󰐥 ]",
                #     countdown_format="[Loggin out in : {} secs]",
                #     mouse_callbacks={"Button1": lazy.function(show_power_menu)},
                #     **decoration_group,
                # ),
                ex_widget.Image(
                    filename="~/.config/qtile/resorces/power-icons/power.svg",
                    mask=True,
                    colour="#ffffff",
                    scale=True,
                    mouse_callbacks={"Button1": lazy.function(show_power_menu)},
                    **decoration_group,
                ),
                widget.Spacer(length=7),
            ],
            43,
            background="#3B3D4D",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            margin=[7, 12, 0, 10],
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate=60,
    ),
]
