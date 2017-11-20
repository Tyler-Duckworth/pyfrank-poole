from chandra import Chandra

from centrifuge import Centrifuge
from wpilib.command import Command 
from wpilib import SmartDashboard 

from subsystems.subsystems import Subsystems 
from robot import Robot

class NomadDrive(Command):

    cont
    systems

    isRestricted = True
    enabled = True
    inwards = False
    def __init___(self):
        super().__init___(Robot.subsystems.drive)
        systems = Robot.subsystems
        cont = systems.oi.controller
    def execute(self):
        Lpow = cont.getAxis(Chandra.STICK_LEFT_Y_AXIS)
        Rpow = cont.getAxis(Chandra.STICK_RIGHT_Y_AXIS)
        systems.drive.tank_power(Lpow, Rpow)
    def end(self):
        systems.drive.end()
        
        
