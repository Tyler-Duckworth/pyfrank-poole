from wpilib.joystick import Joystick
"""This Module """

class NES(Joystick):
    def __init__(self, port):
        super().__init__(port)
    def pow_scale(self, val, pow):
        _abs_v = abs(val)
        _sgn_v = sgn(val)
        return _sgn_v * (_abs_v**pow)

    def sgn(vale):
        if vale > 0:
            return 1
        elif vale < 0:
            return -1
        else:
            return 0

    def _pow_scale(self, val):
        return self.pow_scale(val, 2.0)


    def getButton(self, port):
        return self.getRawButton(port)


    def getAxis(self, port):
        return self._pow_scale(self.getRawAxis(port))