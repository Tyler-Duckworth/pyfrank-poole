from wpilib.joystick import Joystick
"""This Module """

class Centrifuge(Joystick):
    def __init__(self, port):
        super().__init__(port)
    def pow_scale(self, val, pow):
        _abs_v = abs(val)
        _sgn_v = self.sign(val)
        return _sgn_v * (_abs_v**pow)


    def _pow_scale(self, val):
        return self.pow_scale(val, 2.0)


    def getButton(self, port):
        return self.getRawButton(port)


    def getAxis(self, port):
        return self._pow_scale(self.getRawAxis(port))
    def sign(self, value):
        if value == 0:
            return 0
        elif value < 0:
            return -1.0
        else:
            return 1.0