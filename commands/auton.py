from wpilib.command.commandgroup import CommandGroup 

from wpilib.command.waitcommand import WaitCommand 
from commands.tanktimed import TankDriveTimed

class Auton(CommandGroup):
    def __init__(self):
        super().__init__('Autonomous Program')

        self.addSequential(TankDriveTimed(1, .5, .5))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(TankDriveTimed(1, -.5, .5))