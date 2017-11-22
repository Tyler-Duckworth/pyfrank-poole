import wpilib

class SolenoidHandler():

    def __init__(self, port1, port2, _toget, _invert):
        self.sol1 = wpilib.Solenoid(port1)
        self.sol2 = wpilib.Solenoid(port2)
        self.toget = _toget
        self.invert = _invert
        self.deff = not _invert
        self.last = False
        self.sets(not self.deff)
    
    def enable(self):
        last = True
        self.sol1.set(self.deff)
        self.sol2.set(self.deff ^ (not self.toget))


    def disable(self):
        last = False
        self.sol1.set(self.deff)
        self.sol2.set(self.deff)


    def get(self):
        return last
    
    def sets(self, on):
        if on is True:
            self.enable()
        else:
            self.disable()
            
    def toggle(self):
        sets(last)
