from chandra import Chandra

from centrifuge import Centrifuge
from wpilib.command import Command 
from wpilib import SmartDashboard 

from subsystems.nomad import Nomad
from subsystems.subsystems import Subsystems
from subsystems.conts import Conts
from robot import WoprJR

class NomadDrive(Command):

    #cont
    #systems

    isRestricted = True
    enabled = True
    inwards = False

    def __init__(self):
        super().__init__(Nomad)

        self.sub = Subsystems()
        self.cont = Conts()
    def execute(self):
        self.Lpow = self.cont.controller.getAxis(Chandra.STICK_LEFT_Y_AXIS)
        self.Rpow = self.cont.controller.getAxis(Chandra.STICK_RIGHT_Y_AXIS)
        self.sub.drive.tank_power(self.Lpow,self.Rpow)
    def end(self):
        self.nomads.end()
        
        
