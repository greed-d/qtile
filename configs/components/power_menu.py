from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText
from libqtile.lazy import lazy


def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="/home/greed/.config/qtile/resorces/power-icons/lock.svg",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mask=True,
            colour="#cdd6f4",
            mouse_callbacks={"Button1": lazy.spawn("betterlockscreen -l")},
        ),
        PopupImage(
            filename="/home/greed/.config/qtile/resorces/power-icons/moon.svg",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mask=True,
            colour="#cdd6f4",
            mouse_callbacks={
                "Button1": lazy.spawn("/home/greed/.config/qtile/scripts/check.sh")
            },
        ),
        PopupImage(
            filename="/home/greed/.config/qtile/resorces/power-icons/power.svg",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mask=True,
            colour="#cdd6f4",
            mouse_callbacks={"Button1": lazy.shutdown()},
        ),
        PopupText(
            text="Lock", pos_x=0.1, pos_y=0.7, width=0.2, height=0.2, h_align="center"
        ),
        PopupText(
            text="Sleep", pos_x=0.4, pos_y=0.7, width=0.2, height=0.2, h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center",
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)
