#! /bin/bash

if  [[ $EUID != 0 ]]; then
    echo "This file must be run as root"
    echo "Please use sudo ./installDependancies.sh"
    exit 1
fi

apt-get update
apt-get install python3 python3-tk usbmount mercurial

hg clone https://bitbucket.org/pygame/pygame
cd pygame

apt-get install python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev python3-setuptools

python3 setup.py build
python3 setup.py install
