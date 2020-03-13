#!/usr/bin/python3

import serial

with serial.Serial('/dev/ttyUSB0', 4800, parity=serial.PARITY_EVEN, bytesize=7, timeout=5) as ser:
    ser.write(b'Hello Minitel World !')
    s = ser.read(2)
    print(s)
