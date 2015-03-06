import rhinoscriptsyntax as rs
import Rhino


class Particle:
    
    def __init__(self, size, location, vel, acc):
        self._size = size
        self._loc = location
        self._vel = vel
        self._acc = acc
        self._bBox = None
        self._alive = True
    
    def applyForce(self,force):
        newForce = rs.VectorDivide(force,self._size)
        self._acc = rs.VectorAdd(self._acc,newForce)
    
    def setBoundingBox(self,boundingBox):
        self._bBox = boundingBox
        
    def update(self):
        self._vel = rs.VectorAdd(self._vel,self._acc)
        self._loc = rs.VectorAdd(self._loc, self._vel)
        if(self._bBox and not self._bBox.Contains(Rhino.Geometry.Point3d(self._loc))):
            self._alive = False
    
    def draw(self):
        if(self._alive):
            return rs.AddPoint(self._loc)
        else:
            return False
            
            
class Attractor:
    
    def __init__(self, location, force, rad):
        self._loc = location
        self._force = force
        self._rad = rad
        
    def attract(self, particle):
        dir = rs.VectorCreate(self._loc,particle._loc)
        mag = rs.VectorLength(dir)
        if(mag > self._rad):
            mag = self._rad
        dir = rs.VectorUnitize(dir)
        
        force = self._force * (mag/self._rad)
        return rs.VectorScale(dir,force)
        
