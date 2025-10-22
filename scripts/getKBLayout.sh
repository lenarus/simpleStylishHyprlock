#!/bin/env bash

echo $(hyprctl devices | grep -B 6 "main: yes" | grep "active keymap: " | awk '{for (i = 3; i <= NF; i++)printf("%s ", $i);print " "}')