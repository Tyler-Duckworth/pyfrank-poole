from wpilib.command import TimedCommand

import subsystems

class TankDriveTimed(TimedCommand):

    def __init__(self, time, lpow, rpow):
        super().__init__('Tank Drive Timed %s, %s' % (lpow, rpow), time)

        self.lpow = lpow
        self.rpow = rpow
        self.requires(subsystems.nomad)

    def initalize(self):
        subsystems.subsystems.Subsystems.drive.set(self.lpow, self.rpow)
    def end(self):
        subsystems.subsystems.Subsystems.drive.set(0, 0)