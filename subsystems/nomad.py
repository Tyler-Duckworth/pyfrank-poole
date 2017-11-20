import wpilib

from wpilib.smartdashboard import SmartDashboard
from wpilib.command.subsystem import Subsystem
from wpilib.compressor import Compressor
from .solenoids import SolenoidHandler
from .motor import DriveMotor
from chandra import Chandra
from commands.nomaddrive import NomadDrive

class Nomad(Subsystem):

    def __init__(self):
        self.comp = Compressor()
        self.comp.start()

        self.gate = SolenoidHandler(Chandra.gearGateOpen, Chandra.gearGateClose, False, True)
        self.mouth = SolenoidHandler(Chandra.gear_intakeTighten, Chandra.gear_intakeLower, False)
        self.gearBox = SolenoidHandler(Chandra.gearboxLowGear, Chandra.gearboxHighGear, False)

        self.climb = DriveMotor(Chandra.climbMotor)
        
        self.lz = DriveMotor(Chandra.L0Motor)
        self.lo = DriveMotor(Chandra.L1Motor)
        self.rz = DriveMotor(Chandra.R0Motor)
        self.ro = DriveMotor(Chandra.R1Motor)

        self.lz.setInverted(True)
        self.lo.setInverted(True)

        self.rz.setInverted(False)
        self.ro.setInverted(False)

    def __init__(self):
        self(False)

    def initDefaultCommand(self):
        setDefaultCommand(new NomadDrive())
    def stop(self):
        tank_power(0,0)
    def tank_power(self, lpow, rpow):
        lz.set(lpow)
        lo.set(lpow)

        rz.set(rpow)
        ro.set(rpow)
