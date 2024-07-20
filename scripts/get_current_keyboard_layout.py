import sys


def main():
    text = []
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "yes":
            break
        text.append(sys.argv[i])
    print(text[len(text) - text[::-1].index("keymap:")])

if __name__ == "__main__":
    main()