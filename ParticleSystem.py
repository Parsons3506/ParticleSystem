
import rhinoscriptsyntax as rs
from Particle import Particle
<<<<<<< HEAD
from Attractor import Attractor
=======
from Particle import Attractor

>>>>>>> origin/master
import random
import Rhino

def main():
    #boxs = rs.ObjectsByName("box")
    #min = rs.ObjectsByName("min")
    #max = rs.ObjectsByName("max")
    
    box = rs.GetBox(prompt1="select box")
    
    attrPointIn = rs.GetObjects("select attractors",1)
    attrs = []
    for a in attrPointIn:
        point = rs.coerce3dpoint(a)
        attrs.append(Attractor(point, -1, 50))
    
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
<<<<<<< HEAD
    for i in range(0,10):
=======
    for i in range(0,200):
>>>>>>> origin/master
        x = random.uniform(minPoint[0],maxPoint[0])
        y = random.uniform(minPoint[1],maxPoint[1])
        z = random.uniform(minPoint[2],maxPoint[2])
        
        acc = random.uniform(-.01,-0.2)
        size = random.uniform(.008,0.4)
        tempParticle = Particle(size, [x,y,z], vel, [0,0,acc])
        tempParticle.setBoundingBox(boundingBox)
        particles.append(tempParticle)
    
<<<<<<< HEAD
    for i in range(0,10):
        loop(particles)
=======
    for i in range(0,100):
            loop(particles, attrs)
    
>>>>>>> origin/master
    
    for particle in particles:
        particle.drawCurve()
    
    print"finished"
    
def applyAttractor(particles, Attractor):
    for particle in particles:
        
    

<<<<<<< HEAD
def loop(particles, Attractor):
    rs.EnableRedraw(False)
    drawPoints = []
    for particle in particles:
        applyRepel(particle,Attractor)
=======


def loop(particles, attractor):
    rs.EnableRedraw(False)
    drawPoints = []
    for particle in particles:
        applyRepel(particle,attractor)
>>>>>>> origin/master
        particle.update()
        tempPoint = particle.draw()
        if tempPoint:
            drawPoints.append(tempPoint)
    rs.EnableRedraw(True)
    rs.EnableRedraw(False)
    rs.DeleteObjects(drawPoints)

<<<<<<< HEAD
=======

def applyRepel(particle, attractors):
    for attr in attractors:
        attrVector = attr.attract(particle)
        particle.applyForce(attrVector)
        

def drawSphere(particles):
    for particle in particles:
        tempPoint = particle.draw()
        if tempPoint:
            rs.AddSphere(rs.coerce3dpoint(tempPoint),particle._size)

>>>>>>> origin/master
if(__name__ == "__main__"):
    main()

