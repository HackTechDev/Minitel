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

    m.resetzones()
    m.home()
    m.cursor(False)
    m.pos(0, 1)
    m.flash()
    m._print('Recherche... ')

    m.drawscreen('ecrans/ilard.vtd')

if __name__ == '__main__':
    main()
