#!/usr/bin/env python
#
# Quick usage of "launchpad.py", LEDs and buttons.
# Works with all Launchpads: Mk1, Mk2, S/Mini, Pro, XL and LaunchKey
#
#
# FMMT666(ASkr) 7/2013..2/2018
# www.askrprojects.net
#

import sys

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")

import random
from pygame import time


def main():
    mode = None

    # create an instance
    lp = launchpad.Launchpad();

    # check what we have here and override lp if necessary
    if lp.Open():
        print("Launchpad Mk1/S/Mini")
        mode = "Mk1"

    if mode is None:
        print("Did not find any Launchpads, meh...")
        return

    # Clear the buffer because the Launchpad remembers everything :-)
    lp.ButtonFlush()

    while 1:
        if mode == "Mk1" or mode == "XL":
            lp.LedCtrlRaw(random.randint(0, 127), random.randint(0, 3), random.randint(0, 3))

        if mode == "XL" or mode == "LKM":
            but = lp.InputStateRaw()
        else:
            but = lp.ButtonStateRaw()

        if but != []:
            print(" event: ", but)

    # now quit...
    print("Quitting might raise a 'Bad Pointer' error (~almost~ nothing to worry about...:).\n\n")

    lp.Reset()  # turn all LEDs off
    lp.Close()  # close the Launchpad (will quit with an error due to a PyGame bug)


if __name__ == '__main__':
    main()
