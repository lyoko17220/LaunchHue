# Nicolas SAGOT Script
import time
from random import random

import launchpad_py as launchpad
from phue import Bridge

b = Bridge('192.168.1.15')

b.connect()

# create an instance
lp = launchpad.Launchpad()

class PadButtonFunctions:
    @staticmethod
    def short_press_0():
        color = [random(), random()]
        command = {'transitiontime': 0, 'on': True, 'bri': 100, 'xy': color}
        b.set_light([2,3], command)
        command = {'transitiontime': 0, 'on': True, 'bri': 1, 'xy': color}
        b.set_light([2, 3], command)
        print("Changing", command['xy'])

    def short_press_1():
        color = [random(), random()]
        command = {'transitiontime': 0, 'on': True, 'bri': 100, 'xy': color}
        b.set_light([2], command)
        time.sleep(0.1)
        b.set_light([3], command)
        command = {'transitiontime': 0, 'on': True, 'bri': 1, 'xy': color}
        b.set_light([3], command)
        time.sleep(0.1)
        b.set_light([2], command)
        print("Changing", command['xy'])

    def short_press_7():
        color = [random(), random()]
        command = {'transitiontime': 0, 'on': True, 'bri': 100, 'xy': color}
        b.set_light([2,3], command)
        command = {'transitiontime': 10 , 'on': True, 'bri': 1, 'xy': color}
        b.set_light([2, 3], command)
        print("Changing", command['xy'])


    def short_press_68():
        color = [0.2, 0.4]
        command = {'transitiontime': 0, 'on': True, 'bri': 100, 'xy': color}
        b.set_light([2, 3], command)
        command = {'transitiontime': 3, 'on': True, 'bri': 1, 'xy': color}
        b.set_light([2, 3], command)
        print("Changing", command['xy'])

    def short_press_69():
        color = [0.6, 0.3]
        command = {'transitiontime': 1, 'on': True, 'bri': 100, 'xy': color}
        b.set_light([2, 3], command)
        command = {'transitiontime': 3, 'on': True, 'bri': 1, 'xy': color}
        b.set_light([2, 3], command)
        print("Changing", command['xy'])

    @staticmethod
    def long_press_true_112():
        command = {'transitiontime': 0, 'on': True, 'bri': 100, 'xy': [0.33,0.33]}
        b.set_light([2,3], command)
        print("Changing", command['xy'])

    @staticmethod
    def long_press_false_112():
        command = {'transitiontime': 0, 'on': True, 'bri': 1, 'xy': [0.33,0.33]}
        b.set_light([2,3], command)
        print("Changing", command['xy'])

class PadButton:

    @staticmethod
    def get(action):
        touch = str(action[0])

        if action[1]:
            func_name = 'short_press_' + str(touch)
            if hasattr(PadButtonFunctions, func_name):
                func = getattr(PadButtonFunctions, func_name)
                func()  # <-- this should work!

            func_name = 'long_press_true_' + str(touch)
            if hasattr(PadButtonFunctions, func_name):
                func = getattr(PadButtonFunctions, func_name)
                func()  # <-- this should work!
        else:
            func_name = 'long_press_false_' + str(touch)
            if hasattr(PadButtonFunctions, func_name):
                func = getattr(PadButtonFunctions, func_name)
                func()  # <-- this should work!

    @staticmethod
    def color_only_binded():
        lp.LedAllOn(0)
        for i in range(0, 200):
            if hasattr(PadButtonFunctions, 'short_press_' + str(i)):
                lp.LedCtrlRaw(i, 0, 3)
            if hasattr(PadButtonFunctions, 'long_press_true_' + str(i)) or hasattr(PadButtonFunctions, 'long_press_false_' + str(i)):
                lp.LedCtrlRaw(i, 3, 2)
        lp.LedCtrlRaw(25, 3, 2)


def main():
    mode = None

    # check what we have here and override lp if necessary
    if lp.Open():
        print("Launchpad Mk1/S/Mini")
        mode = "Mk1"

    if mode is None:
        print("Did not find any Launchpads, meh...")
        return

    # Clear the buffer because the Launchpad remembers everything :-)
    lp.ButtonFlush()

    # Prepare Light
    b.set_light(3, 'on', False)

    PadButton.color_only_binded()

    while 1:
        but = lp.ButtonStateRaw()
        #time.sleep(.05)
        if but.__len__() == 2:
            #print(but)
            PadButton.get(but)
            # color = [random(), random()]
            # command = {'transitiontime': 1, 'on': True, 'bri': 100, 'xy': color}
            # b.set_light([2,3], command)
            # command = {'transitiontime': 1, 'on': True, 'bri': 1, 'xy': color}
            # b.set_light([2, 3], command)
            # print("Changing", command['xy'])


if __name__ == '__main__':
    main()
