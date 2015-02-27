import rhinoscriptsyntax as rs



class Particle:
    
    def __init__(self, size, location, vel, acc):
        self._size = size
        self._loc = location
        self._vel = vel
        self._acc = acc
    
    def draw(self):
        rs.AddSphere(self._loc,self._size)
