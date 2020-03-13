#!/usr/bin/env python3

import serial
import pynitel
from bs4 import BeautifulSoup
import requests
import sys
import json


m = None

def init():
    "Initialisation du serveur vidéotex"
    global m
    m = pynitel.Pynitel(serial.Serial('/dev/ttyUSB0', 4800,
                                      parity=serial.PARITY_EVEN, bytesize=7,
                                      timeout=2))


def main():
    global m
    init()

    m.home()
    m.pos(1)
    m._print('ILARD')

    m.color(m.vert)
    m.locate(2, 5)
    m._print('HACKLAB08')

if __name__ == '__main__':
    main()
