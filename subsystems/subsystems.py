from wpilib.driverstation import DriverStation
from wpilib import SmartDashboard 
from networktables import NetworkTables

import nomad
from oi import OI
from sensors import Sensors

class Subsystems():
    infont 
    ds
    drive
    oi
    sensors

    isEnabled = True

    def __init__(self):
        self.drive = nomad.Nomad()
        self.oi = OI()
        self.ds = DriverStation.getInstance()

        self.infont = NetworkTables.getTable('info')
        self.sensors = Sensors()
    
    def dumpInfo(self):
        if isEnabled:
            SmartDashboard.putNumber("Yaw: ", Sensors.__init__.NavX.getYaw())
            SmartDashboard.putNumber("Pitch: ", Sensors.__init__.NavX.getPitch())

            self.infont.putNumber("BatteryVoltage", self.ds.getBatteryVoltage())
            color = self.ds.getAlliance()
            self.infont.putNumber("color", color.ordinal())
