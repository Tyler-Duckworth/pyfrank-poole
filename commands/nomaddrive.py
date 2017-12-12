from chandra import Chandra

from centrifuge import Centrifuge
from wpilib.command import Command 
from wpilib import SmartDashboard 

from subsystems.conts import Conts
import subsystems

class NomadDrive(Command):

    #cont
    #systems

    isRestricted = True
    enabled = True
    inwards = False

    def __init__(self):
        super().__init__('NomadDrive')

        self.requires(subsystems.drive)
        self.cont = Conts()
    def execute(self):
        if self.isRestricted:
            self.restrictedOperation()
        else:
            self.normalOperation()
    def restrictedOperation(self):
        subsystems.drive.tank_power(self.cont.controller.getAxis(Chandra.STICK_LEFT_Y_AXIS), self.cont.controller.getAxis(Chandra.STICK_RIGHT_Y_AXIS))
        cpow = self.cont.controller.getAxis(Chandra.L_TRIGGER_AXIS) + 1
        if cpow != 1:
            subsystems.drive.climb.set(cpow)
        else:
            subsystems.drive.climb.set(0)

        if self.cont.controller.getButton(Chandra.rone):
            systems.drive.gearBox.enable()
        elif self.cont.controller.getButton(Chandra.lone):
            systems.drive.gearBox.disable()
        if self.cont.controller.getPOV(0) == 270:
            enabled = False
        if self.cont.controller.getPOV(0) == 0:
            enabled = True
            inwards = False
        if self.cont.controller.getPOV(0) == 180:
            enabled = True
            inwards = True
        cpower = self.cont.controller.getAxis(Chandra.L_TRIGGER_AXIS) + 1
        subsystems.drive.climb.set(cpower * cpower)
    def normalOperation(self):
        subsystems.drive.tank_power(self.cont.controller.getAxis(Chandra.STICK_LEFT_Y_AXIS), self.cont.controller.getAxis(Chandra.STICK_RIGHT_Y_AXIS))

        cpow = self.cont.controller.getAxis(Chandra.L_TRIGGER_AXIS) + 1
        if cpow != 1:
            subsystems.drive.climb.set(cpow)
        else:
            subsystems.drive.climb.set(0)

        if self.cont.controller.getButton(Chandra.rone):
            systems.drive.gearBox.enable()
        elif self.cont.controller.getButton(Chandra.lone):
            systems.drive.gearBox.disable()
        if cont.getPOV(0) == 270:
            enabled = False
        if cont.getPOV(0) == 0:
            enabled = True
            inwards = False
        if cont.getPOV(0) == 180:
            enabled = True
            inwards = True
        subsystems.drive.mouth.set(cont.controller.getButton(Chandra.SQUARE))
        subsystems.drive.gate.set(not cont.controller.getButton(Chandra.X))
    def end(self):
        subsystems.drive.stop()
