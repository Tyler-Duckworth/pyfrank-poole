import wpilib

from commandbased import CommandBasedRobot
import subsystems.subsystems
import subsystems.oi
from commands.nomaddrive import NomadDrive


class WoprJR(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        oi.init()
        self.teleopProgram = NomadDrive()
    def teleopInit(self):
        self.teleopProgram.start()

if __name__ == "__main__":
    wpilib.run(WoprJR)
