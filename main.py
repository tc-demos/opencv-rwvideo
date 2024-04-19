from fn import *

def main():
    lfuncs = [{"title": "Exit", "func": None},
        {"title": "Copy video file", "fn": copyVideo_Method1},
        {"title": "Capture video segment", "fn": capture},
       # {"title": "Display a live image", "fn": displayLiveImage},
    ]

    while True:
        print(f"\n{'-' * 15}Action Menu{'-' * 15}")
        for i in range(len(lfuncs)):
            print(i, lfuncs[i]["title"])
        print()

        choice = -1

        while choice < 0 or choice >= len(lfuncs):
            msg = f"Enter your choice (0-{str(len(lfuncs) - 1)}): "
            choice = int(input(msg))

        print()

        if choice != 0:
            lfuncs[choice]["fn"]()
        else:
            break


if __name__ == '__main__':
    main()