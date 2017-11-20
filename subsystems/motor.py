from wpilib.spark import Spark

class DriveMotor(Spark):
    def __init__(self, port):
        super().__init__(port)