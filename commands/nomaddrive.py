from chandra import Chandra

from centrifuge import Centrifuge
from wpilib.command import Command 
from wpilib import SmartDashboard 

from subsystems.conts import Conts
import subsystems

class NomadDrive(Command):

    #cont
    #systems

    isRestricted = True
    enabled = True
    inwards = False

    def __init__(self):
        super().__init__('NomadDrive')

        self.requires(subsystems.drive)
        self.cont = Conts()
    def execute(self):
        subsystems.drive.tank_power(self.cont.controller.getAxis(Chandra.STICK_LEFT_Y_AXIS), self.cont.controller.getAxis(Chandra.STICK_RIGHT_Y_AXIS))
    def end(self):
        subsystems.drive.stop()
