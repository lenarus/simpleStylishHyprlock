import sys
import os


def main():
    layout_text = os.popen("hyprctl devices").read().split()
    text = []
    for i in range(1, len(layout_text)):
        if layout_text[i] == "yes":
            break
        text.append(layout_text[i])
    print(text[len(text) - text[::-1].index("keymap:")])


if __name__ == "__main__":
    main()
