import wpilib

from commandbased import CommandBasedRobot
import subsystems
import subsystems.oi
import commands
from commands.nomaddrive import NomadDrive
from commands.auton import Auton

global subs
class WoprJR(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        subsystems.oi.init()

        self.teleopProgram = NomadDrive()
        self.autonomousProgram = Auton()

    def autonomousInit(self):
        self.autonomousProgram.start()
        
    def teleopInit(self):
        self.teleopProgram.start()
    

if __name__ == "__main__":
    wpilib.run(WoprJR)
