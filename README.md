# i3
Configuration files for i3

# Requirements

## Startup
* pulseaudio - Audio
* xscreensaver - Screensaver
* xcompmgr - Composition manager (disabled)
* compton - Composition manager
* udiskie - Auto mounting
* nitrogen - Wallpaper

## General usage
* rofi - launcher
* scrot - Screenshots
* dunst - Notifications
* pamixer - Volume handler
* terminator - Terminal emulator

# Keybinds

* Super+(WASD or arrow keys) => Move focus
* Super+Shift+(WASD or arrow keys) => Move window

* Super+0-9 => Go to workspace
* Super+Shift+0-9 => Move window to workspace

* Super+R => Resize mode (use WASD or arrow keys to resize, escape to exit mode)

* Super+Space => rofi launched

* Super+Alt+(1-4) => Take screenshot using scrot

* Super+(h|v) => Split horizontal/vertical
* Super+c => Toggle split

* Super+Alt+Space => Floating mode toggle

* Super+(z|x|c) => Layout (stacking|tabbed)

* Control+Super+r => Reload configuration
* Control+Super+Shift+r => Restart i3

# Appearance
Can be modified in the config/gaps files, will send the variables to rofi, dunst and blocks/status so they follow the theme as well, which is real nice.

Naming of workspaces can also be changed easily by editing their variables.

# Notes

Bottom of gaps/config file contains window specific rules. Steam, skype, spotify, terminals are sitting on their own workspaces by default but can easily be removed/added to.
