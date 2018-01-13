import wpilib

from wpilib.smartdashboard import SmartDashboard
from wpilib.command.subsystem import Subsystem
from wpilib.compressor import Compressor
from wpilib.spark import Spark

from edi import EDI
from commands.mako import Mako

class Nomad(Subsystem):

    def __init__(self):        
        self.lz = new Spark(EDI.L0Motor)
        self.lo = new Spark(EDI.L1Motor)
        self.rz = new Spark(EDI.R0Motor)
        self.ro = new Spark(EDI.R1Motor)

        self.lz.setInverted(True)
        self.lo.setInverted(True)

        self.rz.setInverted(False)
        self.ro.setInverted(False)

    def __init__(self):
        self(False)

    def initDefaultCommand(self):
        setDefaultCommand(new Mako())

    def stop(self):
        tank_power(0,0)

    def tank_power(self, lpow, rpow):
        lz.set(lpow)
        lo.set(lpow)

        rz.set(rpow)
        ro.set(rpow)
