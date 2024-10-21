from libqtile import hook
from qtile_extras import widget as ex_widget
from qtile_extras.widget.decorations import RectDecoration


class CustomWindowName(ex_widget.TextBox):
    def __init__(self, **config):
        super().__init__(**config)
        self.text = "None"  # Default text when no mapped window is active
        hook.subscribe.client_focus(
            self.update_window
        )  # Hook into client focus changes

        # Mapping: window class -> [icon, custom name]
        self.window_map = {
            "kitty": ["󰄛", "Kitty Terminal"],
            "firefox": ["󰈹", "Firefox"],
            "microsoft-edge": ["󰇩", "Edge"],
            "discord": ["", "Discord"],
            "vesktop": ["", "Vesktop"],
            "armcord": [" ", "Armcord"],
            "org.kde.dolphin": ["", "Dolphin"],
            "plex": ["󰚺", "Plex"],
            "steam": ["", "Steam"],
            "spotify": ["󰓇", "Spotify"],
            "ristretto": ["󰋩", "Ristretto"],
            "obsidian": ["󱓧", "Obsidian"],
            # Browsers
            "google-chrome": ["", "Google Chrome"],
            "zen-alpha": ["󰰶", "Zen Browser"],
            "Navigator": ["󰰶", "Zen Browser"],
            "brave-browser": ["󰖟", "Brave Browser"],
            "chromium": ["", "Chromium"],
            "opera": ["", "Opera"],
            "vivaldi": ["󰖟", "Vivaldi"],
            "waterfox": ["󰖟", "Waterfox"],
            "thorium": ["󰖟", "Waterfox"],
            "tor-browser": ["", "Tor Browser"],
            "floorp": ["󰈹", "Floorp"],
            # Terminals
            "gnome-terminal": ["", "GNOME Terminal"],
            "konsole": ["", "Konsole"],
            "alacritty": ["", "Alacritty"],
            "wezterm": ["", "Wezterm"],
            "foot": ["󰽒", "Foot Terminal"],
            "tilix": ["", "Tilix"],
            "xterm": ["", "XTerm"],
            "urxvt": ["", "URxvt"],
            "st": ["", "st Terminal"],
            # IDE/Text editors
            "code": ["󰨞", "Visual Studio Code"],
            "vscode": ["󰨞", "VS Code"],
            "sublime-text": ["", "Sublime Text"],
            "atom": ["", "Atom"],
            "android-studio": ["󰀴", "Android Studio"],
            "intellij-idea": ["", "IntelliJ IDEA"],
            "pycharm": ["󱃖", "PyCharm"],
            "webstorm": ["󱃖", "WebStorm"],
            "phpstorm": ["󱃖", "PhpStorm"],
            "eclipse": ["", "Eclipse"],
            "netbeans": ["", "NetBeans"],
            "docker": ["", "Docker"],
            "vim": ["", "Vim"],
            "neovim": ["", "Neovim"],
            "neovide": ["", "Neovide"],
            "emacs": ["", "Emacs"],
            # Social Apps
            "slack": ["󰒱", "Slack"],
            "telegram-desktop": ["", "Telegram"],
            "org.telegram.desktop": ["", "Telegram"],
            "whatsapp": ["󰖣", "WhatsApp"],
            "teams": ["󰊻", "Microsoft Teams"],
            "skype": ["󰒯", "Skype"],
            "thunderbird": ["", "Thunderbird"],
            # File Managers
            "nautilus": ["󰝰", "Files (Nautilus)"],
            "thunar": ["󰝰", "Thunar"],
            "pcmanfm": ["󰝰", "PCManFM"],
            "nemo": ["󰝰", "Nemo"],
            "ranger": ["󰝰", "Ranger"],
            "doublecmd": ["󰝰", "Double Commander"],
            "krusader": ["󰝰", "Krusader"],
            "vlc": ["󰕼", "VLC Media Player"],
            "mpv": ["", "MPV"],
            "rhythmbox": ["󰓃", "Rhythmbox"],
            "gimp": ["", "GIMP"],
            "inkscape": ["", "Inkscape"],
            "krita": ["", "Krita"],
            "blender": ["󰂫", "Blender"],
            "kdenlive": ["", "Kdenlive"],
            "lutris": ["󰺵", "Lutris"],
            "heroic": ["󰺵", "Heroic Games Launcher"],
            "minecraft": ["󰍳", "Minecraft"],
            "csgo": ["󰺵", "CS:GO"],
            "dota2": ["󰺵", "Dota 2"],
            "evernote": ["", "Evernote"],
            "sioyek": ["", "Sioyek"],
            "dropbox": ["󰇣", "Dropbox"],
            "^$": ["󰇄", "Desktop"],
            # Add other mappings as needed
        }

    def update_window(self, window=None):
        # Get the current active window
        active_window = self.qtile.current_window
        if active_window:
            window_class = active_window.window.get_wm_class()[
                0
            ]  # Get the window class name

            # Check if the window class is in the window_map
            if window_class in self.window_map:
                icon, name = self.window_map[window_class]
                self.update(f"{icon}  {name}")  # Display icon and name
            else:
                self.update(
                    active_window.name
                )  # Display the actual window title if no match
        else:
            self.update("None")  # Default when no window is active
