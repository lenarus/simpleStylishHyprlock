#!/bin/bash
LAYOUT_TEXT=$(hyprctl devices)
python $HOME/.scripts/python_scripts/get_current_keyboard_layout.py $LAYOUT_TEXT
