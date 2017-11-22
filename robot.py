import wpilib

from commandbased import CommandBasedRobot
import subsystems
import subsystems.oi
import commands
import commands.nomaddrive

global subs
class WoprJR(CommandBasedRobot):

    def robotInit(self):
        subs = subsystems
        subsystems.init()
        subsystems.oi.init()
        self.teleopProgram = commands.nomaddrive.NomadDrive()
    def teleopInit(self):
        self.teleopProgram.start()

if __name__ == "__main__":
    wpilib.run(WoprJR)
