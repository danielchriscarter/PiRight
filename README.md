# PyRight

PyRight is a project to build a Raspberry-Pi based game to assist those with Attention-Defecit Disorders

It is intended as an entry to the [PA Pi Competition](http://www.paconsulting.com/events/raspberry-pi-competition), as well as a learning experience with the use of Pygame for a GUI

## Requirements
* Python3 - `apt-get install python3`
* Pygame - [instructions for installation](http://askubuntu.com/questions/401342/how-to-download-pygame-in-python3-3)
* usbmount (handles importing of data from USB drives) - `apt-get install usbmount`
* Florence (on-screen keyboard for touchscreen) - `apt-get install florence`
* at-spi2-core (library required for Florence keyboard) - `apt-get install at-spi2-core`

This has only been tested on Raspbian, but may also work on other distributions

## To set up
 `git clone https://github.com/danielchriscarter/PiRight`

 `sudo python3 main_code.py`

## Used Libraries
* Pygame(LGPL)
* Raspberry Pi GPIO module (MIT licence)