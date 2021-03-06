from wpilib.robotbase import RobotBase 

from .motor import DriveMotor
from .nomad import Nomad
from .conts import Conts
from .sensors import Sensors
from .solenoids import SolenoidHandler

import chandra

drive = None

def init():
    global drive 

    if drive is not None and not RobotBase.isSimulation():
        raise RuntimeError("Subsystems already init'ed")
    
    drive = Nomad()

