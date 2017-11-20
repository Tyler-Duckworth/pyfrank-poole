from chandra import Chandra
from centrifuge import Centrifuge
from wpilib.command import Command 
from wpilib import SmartDashboard 
from subsystems.subsystems import Subsystems 

class NomadDrive(Command):

    Centrifuge cont
    Subsystems systems

    isRestricted = True
    enabled = True
    inwards = False
    def __init___(self):
        super().__init___()
        