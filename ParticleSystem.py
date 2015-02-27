import rhinoscriptsyntax as rs
from Particle import Particle
import random



def main():
    
    box = rs.GetBox(prompt1="select box")
    
    minPoint = box[0]
    maxPoint = box[6]
    
    size = 5.0
    location = [0,0,0]
    vel = [0,0,0]
    acc = [0,0,0]
    
    particles = []
    
    for i in range(0,1000):
        x = random.uniform(minPoint[0],maxPoint[0])
        y = random.uniform(minPoint[1],maxPoint[1])
        z = random.uniform(minPoint[2],maxPoint[2])
        
        
        
        particles.append(Particle(size, [x,y,z], vel, acc))
    
    for particle in particles:
        particle.draw()
    
    print"hello"


if(__name__ == "__main__"):
    main()

