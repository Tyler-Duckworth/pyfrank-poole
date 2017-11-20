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
        self.comp = new Compressor(0)
        self.comp.start()

        self.gate = new SolenoidHandler(Chandra.gearGateOpen, Chandra.gearGateClose, False, True)
        self.mouth = new SolenoidHandler(Chandra.gear_intakeTighten, Chandra.gear_intakeLower, False)
        self.gearBox = new SolenoidHandler(Chandra.gearboxLowGear, Chandra.gearboxHighGear, False)

        self.climb = new DriveMotor(Chandra.climbMotor)
        
        self.lz = new DriveMotor(Chandra.L0Motor)
        self.lo = new DriveMotor(Chandra.L1Motor)
        self.rz = new DriveMotor(Chandra.R0Motor)
        self.ro = new DriveMotor(Chandra.R1Motor)

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
