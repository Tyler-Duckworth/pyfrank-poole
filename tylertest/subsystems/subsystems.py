from wpilib.drivestation import DriverStation
from wpilib import SmartDashboard 
from networktables import NetworkTables

from nomad import Nomad
from oi import OI
from sensors import Sensors

class Subsystems():
    NetworkTables infont 
    DriverStation ds
    Nomad drive
    OI oi
    Sensors sensors

    isEnabled = True

    def __init__(self):
        self.drive = new Nomad()
        self.oi = new OI()
        self.ds = DriverStation.getInstance()

        self.infont = NetworkTables.getTable('info')
        self.sensors = new Sensors()
    
    def dumpInfo(self):
        if isEnabled:
            SmartDashboard.putNumber("Yaw: ", Sensors.__init__.NavX.getYaw())
            SmartDashboard.putNumber("Pitch: ", Sensors.__init__.NavX.getPitch())

            self.infont.putNumber("BatteryVoltage", self.ds.getBatteryVoltage())
            DriverStation.Alliance color = self.ds.getAlliance()
            self.infont.putNumber("color", color.ordinal())