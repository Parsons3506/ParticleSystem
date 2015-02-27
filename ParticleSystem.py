import rhinoscriptsyntax as rs
from Particle import Particle
import random
import Rhino


def main():
    #boxs = rs.ObjectsByName("box")
    min = rs.ObjectsByName("min")
    max = rs.ObjectsByName("max")
    
    #box = rs.GetBox(prompt1="select box")
    
    minPoint = rs.coerce3dpoint(min[0])
    maxPoint = rs.coerce3dpoint(max[0])
    
    size = 5.0
    location = [0,0,0]
    vel = [0,0,0]
    acc = [0,0,0]
    
    particles = []
    boundingBox = Rhino.Geometry.BoundingBox(minPoint,maxPoint)
    for i in range(0,1000):
        x = random.uniform(minPoint[0],maxPoint[0])
        y = random.uniform(minPoint[1],maxPoint[1])
        z = random.uniform(minPoint[2],maxPoint[2])
        
        acc = random.uniform(-.01,-10)
        
        tempParticle = Particle(size, [x,y,z], vel, [0,0,acc])
        tempParticle.setBoundingBox(boundingBox)
        particles.append(tempParticle)
    
    for i in range(0,24):
        loop(particles)
    
    
    print"finished"

def loop(particles):
    rs.EnableRedraw(False)
    drawPoints = []
    for particle in particles:
        particle.update()
        tempPoint = particle.draw()
        if tempPoint:
            drawPoints.append(tempPoint)
    rs.EnableRedraw(True)
    rs.EnableRedraw(False)
    rs.DeleteObjects(drawPoints)

if(__name__ == "__main__"):
    main()

