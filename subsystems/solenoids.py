import wpilib

class SolenoidHandler():

    def __init__(self, port1, port2, _toget, _invert):
        self.sol1 = wpilib.Solenoid(port1)
        self.sol2 = wpilib.Solenoid(port2)
        self.toget = _toget
        self.invert = _invert
        self.deff = !self.invert
        self.last = False
        set(!deff)
    
    def enable(self):
        last = True
        sol1.set(deff)
        sol2.set(deff ^ !toget)


    def disable(self):
        last = False
        sol1.set(deff)
        sol2.set(deff)


    def get(self):
        return last
    
    def set(self, on):
        if self.on = True:
            enable()
        else:
            disable()
            
    def toggle(self):
        set(last)