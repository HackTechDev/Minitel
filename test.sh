#!/bin/sh

stty -F /dev/ttyUSB0 4800 istrip cs7 parenb -parodd brkint ignpar icrnl ixon ixany opost onlcr cread hupcl isig icanon echo echoe echok
sleep 2
echo 'Hello World' > /dev/ttyUSB0
