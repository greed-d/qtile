from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupText, PopupSlider

VOLUME_NOTIFICATION = PopupRelativeLayout(
    width=200,
    height=50,
    controls=[
        PopupText(
            text="Volume:",
            name="text",
            pos_x=0.1,
            pos_y=0.1,
            height=0.2,
            width=0.8,
            v_align="middle",
            h_align="center",
        ),
        PopupSlider(
            name="volume",
            pos_x=0.1,
            pos_y=0.3,
            width=0.8,
            height=0.8,
            colour_below="00ffff",
            bar_border_size=2,
            bar_border_margin=1,
            bar_size=6,
            marker_size=0,
            end_margin=0,
        ),
    ],
)
