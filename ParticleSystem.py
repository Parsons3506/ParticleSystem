
import rhinoscriptsyntax as rs
from Particle import Particle
from Attractor import Attractor
import random
import Rhino


def main():
    #boxs = rs.ObjectsByName("box")
    #min = rs.ObjectsByName("min")
    #max = rs.ObjectsByName("max")
    
    box = rs.GetBox(prompt1="select box")
    
    minPoint = box[0]
    maxPoint = box[6]
    
    size = 5.0
    location = [0,0,0]
    vel = [0,0,0]
    acc = [0,0,0]
    
    attrPointIn = rs.GetObjects("select attractor", 1)
    point = rs.coerce3dpoint(point, raise_on_error=false)
    Attractor = Attractor(point,3,50)
    
    particles = []
    boundingBox = Rhino.Geometry.BoundingBox(minPoint,maxPoint)
    for i in range(0,10):
        x = random.uniform(minPoint[0],maxPoint[0])
        y = random.uniform(minPoint[1],maxPoint[1])
        z = random.uniform(minPoint[2],maxPoint[2])
        
        acc = random.uniform(-.01,-.5)
        size = random.uniform(.1,2)
        tempParticle = Particle(size, [x,y,z], vel, [0,0,acc])
        tempParticle.setBoundingBox(boundingBox)
        particles.append(tempParticle)
    
    for i in range(0,10):
        loop(particles)
    
    print"finished"
    
def applyAttractor(particles, Attractor):
    for particle in particles:
        
    

def loop(particles, Attractor):
    rs.EnableRedraw(False)
    drawPoints = []
    for particle in particles:
        applyRepel(particle,Attractor)
        particle.update()
        tempPoint = particle.draw()
        if tempPoint:
            drawPoints.append(tempPoint)
    rs.EnableRedraw(True)
    rs.EnableRedraw(False)
    rs.DeleteObjects(drawPoints)

if(__name__ == "__main__"):
    main()

