import rhinoscriptsyntax as rs
import Rhino


class Attractor:
    
    def __init__(self, location, force, radius):
        self._loc = location
        self._force = force
        self._radius = radius
        
    def applyForce(self, force):
        newForce = rs.VectorDivide(force, self._size)
        self._acc = rs.VectorAdd(self._acc, newForce)
    
    def attract(self, particle):
        dir = rs.VectorCreate(self._loc, particle._loc)
        mag = rs.VectorLength(dir)
        if mag > self._radius:
            mag = self._radius
        dir = rs.VectorUnitize(dir)
        
        force = self._force * (mag/self._radius)
        return rs.VectorScale(dir, force)
        
        
