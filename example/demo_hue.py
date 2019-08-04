#!/usr/bin/python
from random import random

from phue import Bridge

b = Bridge('192.168.1.15')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Prints if light 1 is on or not

while 1:
    command = {'transitiontime' : 1, 'on' : True, 'bri' : 100, 'xy': [random(), random()]}
    b.set_light(3, command)