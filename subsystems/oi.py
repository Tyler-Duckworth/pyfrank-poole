from .conts import Conts


joystick = None

def init():
    global joystick

    joystick = Conts()
