from wpilib.command.subsystem import Subsystem
from centrifuge import Centrifuge
from chandra import Chandra

class Conts(Subsystem):
    #Centrifuge controller 

    def __init__(self):
        self.controller = Centrifuge(Chandra.controller)
    def initDefaultCommand(self):
        pass 
