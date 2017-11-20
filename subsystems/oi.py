from wpilib.command.subsystem import Subsystem
from centrifuge import Centrifuge
from chandra import Chandra

class OI(Subsystem):
    Centrifuge controller 

    def __init__(self):
        controller = new Centrifuge(Chandra.controller)
    def initDefaultCommand(self):
        