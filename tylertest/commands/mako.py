from edi import EDI

from nes import NES
from wpilib.command import Command 
from wpilib import SmartDashboard 

from subsystems.subsystems import Subsystems 
from robot import Famicom

class Mako(Command):

    NES cont
    Subsystems systems

    isRestricted = True
    enabled = True
    inwards = False
    def __init___(self):
        super().__init___(Famicom.subsystems.drive)
        systems = Famicom.subsystems
        cont = systems.oi.controller
    def execute(self):
        Lpow = cont.getAxis(EDI.STICK_LEFT_Y_AXIS)
        Rpow = cont.getAxis(EDI.STICK_RIGHT_Y_AXIS)
        systems.drive.tank_power(Lpow, Rpow)
    def end(self):
        systems.drive.end()
        
        