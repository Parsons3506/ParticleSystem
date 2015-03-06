import rhinoscriptsyntax as rs
from Particle import Particle
from Particle import Attractor

import random
import Rhino

def main():
    #boxs = rs.ObjectsByName("box")
    #min = rs.ObjectsByName("min")
    #max = rs.ObjectsByName("max")
    
    box = rs.GetBox(prompt1="select box")
    
    attrPointIn = rs.GetObject("select attractor",1)
    point = rs.coerce3dpoint(attrPointIn)
    attr = Attractor(point, 100, 50)
    
    minPoint = box[0]
    maxPoint = box[6]
    
    size = 5.0
    location = [0,0,0]
    vel = [0,0,0]
    acc = [0,0,0]
    
    particles = []
    boundingBox = Rhino.Geometry.BoundingBox(minPoint,maxPoint)
    for i in range(0,200):
        x = random.uniform(minPoint[0],maxPoint[0])
        y = random.uniform(minPoint[1],maxPoint[1])
        z = random.uniform(minPoint[2],maxPoint[2])
        
        acc = random.uniform(-.01,-0.2)
        size = random.uniform(.008,0.4)
        tempParticle = Particle(size, [x,y,z], vel, [0,0,acc])
        tempParticle.setBoundingBox(boundingBox)
        particles.append(tempParticle)
    
    for i in range(0,100):
            loop(particles, attr)
    
    
    print"finished"



def loop(particles, attractor):
    rs.EnableRedraw(False)
    drawPoints = []
    for particle in particles:
        applyRepel(particle,attractor)
        particle.update()
        tempPoint = particle.draw()
        if tempPoint:
            drawPoints.append(tempPoint)
    rs.EnableRedraw(True)
    rs.EnableRedraw(False)
    rs.DeleteObjects(drawPoints)


def applyRepel(particle, attractor):
    attrVector = attractor.attract(particle)
    particle.applyForce(attrVector)
        

def drawSphere(particles):
    for particle in particles:
        tempPoint = particle.draw()
        if tempPoint:
            rs.AddSphere(rs.coerce3dpoint(tempPoint),particle._size)

if(__name__ == "__main__"):
    main()

