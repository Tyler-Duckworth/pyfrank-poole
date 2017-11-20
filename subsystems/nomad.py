import wpilib

from wpilib.smartdashboard import SmartDashboard
from wpilib.command.subsystem import Subsystem
from wpilib.compressor import Compressor
from .solenoids import SolenoidHandler
from .motor import DriveMotor
from chandra import Chandra
from commands.nomaddrive import NomadDrive

class Nomad(Subsystem):
    DriveMotor l0, l1, r0, r1

    DriveMotor stir, intake, climb, shooter

    SolenoidHandler gate, mouth, gearBox

    Compressor comp

    def __init__(self):
        self.comp = new Compressor(0)
        self.comp.start()

        self.gate = new SolenoidHandler(Chandra.gearGateOpen, Chandra.gearGateClose, False, True)
        self.mouth = new SolenoidHandler(Chandra.gear_intakeTighten, Chandra.gear_intakeLower, False)
        self.gearBox = new SolenoidHandler(Chandra.gearboxLowGear, Chandra.gearboxHighGear, False)

        self.climb = new DriveMotor(Chandra.climbMotor)
        
        self.l0 = new DriveMotor(Chandra.L0Motor)
        self.l1 = new DriveMotor(Chandra.L1Motor)
        self.r0 = new DriveMotor(Chandra.R0Motor)
        self.r1 = new DriveMotor(Chandra.R1Motor)

        self.l0.setInverted(True)
        self.l1.setInverted(True)

        self.r0.setInverted(False)
        self.r1.setInverted(False)

    def __init__(self):
        self(False)

    def initDefaultCommand(self):
        setDefaultCommand(new NomadDrive())
    def stop(self):
        tank_power(0,0)
    def tank_power(self, lpow, rpow):
        l1.set(lpow)
        l0.set(lpow)

        r1.set(rpow)
        r0.set(rpow)
