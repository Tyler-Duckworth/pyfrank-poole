import wpilib
from wpilib.command.subsystem import Subsystem

from robotpy_ext.common_drivers import navx

class Sensors(Subsystem):
    navx NavX
    def __init__(self):
        self.NavX = navx.AHRS.create_spi()
    
    def initDefaultCommand(self):
        