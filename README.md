# PiRight

PiRight is a project to build a Raspberry-Pi based game to assist those with Attention-Defecit Disorders

It is intended as an entry to the [PA Pi Competition](http://www.paconsulting.com/events/raspberry-pi-competition), as well as a learning experience with the use of Pygame for a GUI

## Requirements
* Python3 - `apt-get install python3`
* Pygame - [instructions for installation](http://askubuntu.com/questions/401342/how-to-download-pygame-in-python3-3)
* Tkinter - `apt-get install python3-tk`
* usbmount (handles importing of data from USB drives) - `apt-get install usbmount`

This has only been tested on Raspbian, but may also work on other distributions

## To set up
 `git clone https://github.com/danielchriscarter/PiRight`

 `python3 home.py`

## Used Libraries
* Pygame(LGPL)
* Raspberry Pi GPIO module (MIT licence)
* [VKeyboard](https://github.com/wbphelps/VKeyboard) (GPL)