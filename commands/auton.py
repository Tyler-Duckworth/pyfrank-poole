from wpilib.command.commandgroup import CommandGroup 

from wpilib.command.waitcommand import WaitCommand 
from commands.setspeed import SetSpeed

class Auton(CommandGroup):
    def __init__(self):
        super().__init__('Autonomous Program')

        self.addSequential(SetSpeed(power=0.7, time=2))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(SetSpeed(power=0.7, time=2))