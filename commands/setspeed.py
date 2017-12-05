from wpilib.command import TimedCommand

import subsystems

class SetSpeed(TimedCommand):
    def __init__(self, power, time):
        super().__init__('Set Speed %d' % power, time)

        self.power = power
        self.requires(subsystems.drive)

    def initalize(self):
        subsystems.drive.tank_power(self.power, self.power)

    def end(self):
        subsystems.drive.tank_power(0,0)