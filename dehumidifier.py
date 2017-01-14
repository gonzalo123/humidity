#!/usr/bin/env python

from ouimeaux.environment import Environment
from subprocess import check_output
import sys
import os

threshold = 3

def action(switch):
    humidity = int(check_output(["%s/reader.js" % os.path.dirname(sys.argv[0]), sensorMac]))
    if "Switch1" == switch.name:
        botton = expected - threshold
        isOn = False if switch.get_state() == 0 else True
        log = ""

        if isOn and humidity < botton:
            switch.basicevent.SetBinaryState(BinaryState=0)
            log = "humidity < %s Switch to OFF" % botton
        elif not isOn and humidity > expected:
            switch.basicevent.SetBinaryState(BinaryState=1)
            log = "humidity > %s Switch to ON" % expected

        print "Humidity: %s Switch is OK (%s) %s" % (humidity, 'On' if isOn else 'Off', log)

if __name__ == '__main__':
    try:
        sensorMac = sys.argv[1]
        mySwitch = sys.argv[2]
        expected = int(sys.argv[3])
    except:
        print 'Usage "./dehumidifier.py <sensorMac> <switch name> <expected humidity>"'
        sys.exit()

    env = Environment(action)
    env.start()
    env.discover(seconds=3)
