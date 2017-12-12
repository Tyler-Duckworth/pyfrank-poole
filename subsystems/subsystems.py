from wpilib.driverstation import DriverStation
from wpilib import SmartDashboard
from wpilib.command.subsystem import Subsystem 
from networktables import NetworkTables

import subsystems
#from .nomad import Nomad
from .conts import Conts
from .sensors import Sensors

class Subsystems(Subsystem):
    isEnabled = True
    def __init__(self):
        self.oi = Conts()
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
    def initDefaultCommand(self):
       pass 
