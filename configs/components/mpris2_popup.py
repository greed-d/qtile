from pathlib import Path

from qtile_extras.popup.toolkit import (
    PopupCircularProgress,
    PopupImage,
    PopupRelativeLayout,
    PopupSlider,
    PopupText,
)


# IMAGES_FOLDER = "~/.config/qtile/resorces/media-icons"
DEFAULT_IMAGE = "~/.config/qtile/resorces/media-icons/default.png"

DEFAULT_LAYOUT = PopupRelativeLayout(
    None,
    width=400,
    background="1e1e2e",
    height=250,
    controls=[
        PopupText(
            "",
            name="player",
            pos_x=0.5,
            pos_y=0.1,
            width=0.55,
            height=0.14,
            h_align="left",
            v_align="top",
        ),
        PopupText(
            "",
            name="title",
            pos_x=0.5,
            pos_y=0.21,
            width=0.55,
            height=0.14,
            h_align="left",
            v_align="middle",
        ),
        PopupText(
            "",
            name="artist",
            pos_x=0.5,
            pos_y=0.34,
            width=0.55,
            height=0.14,
            h_align="left",
            v_align="middle",
        ),
        PopupText(
            "",
            name="album",
            pos_x=0.5,
            pos_y=0.45,
            width=0.55,
            height=0.14,
            h_align="left",
            v_align="bottom",
        ),
        PopupImage(
            name="artwork",
            filename=DEFAULT_IMAGE,
            pos_x=0.1,
            pos_y=0.03,
            width=0.35,
            height=0.63,
        ),
        PopupSlider(
            name="progress", pos_x=0.1, pos_y=0.6, width=0.8, height=0.2, marker_size=0
        ),
        PopupImage(
            name="previous",
            filename="~/.config/qtile/resorces/media-icons/previous.svg",
            # .resolve()
            # .as_posix(),
            mask=True,
            pos_x=0.125,
            pos_y=0.8,
            width=0.15,
            height=0.1,
        ),
        PopupImage(
            name="play_pause",
            filename="~/.config/qtile/resorces/media-icons/play_pause.svg",
            # .resolve()
            # .as_posix(),
            mask=True,
            pos_x=0.325,
            pos_y=0.8,
            width=0.15,
            height=0.1,
        ),
        PopupImage(
            name="stop",
            filename="~/.config/qtile/resorces/media-icons/stop.svg",
            # .resolve()
            # .as_posix(),
            mask=True,
            pos_x=0.525,
            pos_y=0.8,
            width=0.15,
            height=0.1,
        ),
        PopupImage(
            name="next",
            filename=("~/.config/qtile/resorces/media-icons/next.svg"),
            # .resolve()
            # .as_posix(),
            mask=True,
            pos_x=0.725,
            pos_y=0.8,
            width=0.15,
            height=0.1,
        ),
    ],
    close_on_click=True,
)
