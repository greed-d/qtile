#!/bin/bash
#start nitrogen
nitrogen --restore

#Start polkit agent
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

picom --config /home/greed/.config/picom/picom.qtile.conf &
