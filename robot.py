import wpilib

from commandbased import CommandBasedRobot
import subsystems
import subsystems.oi
import commands
import commands.nomaddrive


class WoprJR(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()
        subsystems.oi.init()
        self.teleopProgram = commands.nomaddrive.NomadDrive()
    def teleopInit(self):
        self.teleopProgram.start()

if __name__ == "__main__":
    wpilib.run(WoprJR)
