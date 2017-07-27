# J.J. Strnad, Physics 130B
# Car Crash Simulator
# Fall 2012

from visual import *
import time

scene = display(title='Car Crash', width=1200, height=300, background = ((112/255), (128/255), (144/255)))


print("\nThis is a simulator for a 1-D car collision.\nCar A starts on the left and Car B starts on the right.\
The two cars start out 100 meters away from each other.These two cars will collide head-on.\
Try to guess which car will have the largest magnitude of momentum upon impact, which car \
will have the most kinetic energy when they collide, and how long it will take \
for the collision to take place based upon the attributes you assign to each car.\n\n")

posA = -50
posB = 50

#Set up the cars
box(pos = (0, -5, 0), length = 120, height = 10, width = 2, color= (1,1,1))
box(pos = (0, -5, 1.001), length = 1, height = 10, width = 0, color = color.red)

FrameB =box(pos = (posB+5, 3, 0), length = 6, height = 4, width = 1, color=color.red)
FrontB = box(pos = (posB+1, 2, 0), length = 2, height = 2, width = 1, color=color.red)
Wheel1B = sphere(pos = (posB+2, .5, 0), radius = .5, color=color.red) 
Wheel2B = sphere(pos = (posB+6, .5, 0), radius = .5, color=color.red)
LabelB = label(pos = (posB+5, -5, 0), text = 'B', color=color.red)

FrameA = box(pos = (posA-5, 3, 0), length = 6, height = 4, width = 1, color=color.blue)
FrontA = box(pos = (posA-1, 2, 0), length = 2, height = 2, width = 1, color=color.blue)
Wheel1A = sphere(pos = (posA-2, .5, 0), radius = .5, color=color.blue) 
Wheel2A = sphere(pos = (posA-6, .5, 0), radius = .5, color=color.blue)
LabelA = label(pos = (posA-5, -5, 0), text = 'A', color=color.blue)


# Establish initial conditions based on user input
massA = eval(input("What should the mass (in kg) of car A be?: "))
velA = eval(input("What should the initial speed (in m/s) of car A be?: "))
accelA = eval(input("What should the acceleration (in m/s^2) of car A be?: "))
massB = eval(input("\nWhat should the mass (in kg) of car B be?: "))
velB = eval(input("What should the initial speed (in m/s) of car B be?: "))
accelB = eval(input("What should the acceleration (in m/s^2) of car B be?: "))
# Obtain guesses
momQ = input("\nWhich car do you think will have the largest magnitude of momentum upon impact? Type 'a' for car A, 'b' for car B, '=' for equal: ")
KEq = input("Which car do you think will have the most kinetic energy upon impact? Type 'a' for car A, 'b' for car B, '=' for equal: ")
timeQ = eval(input("How long (in seconds) do you think it will take for the two cars to collide?: "))


#Main while loop
t = 0
dt = .01
while (FrontA.pos.x + 1) < (FrontB.pos.x - 1):
    rate(100)
    # Change velocities
    velA = velA + (accelA * dt)
    velB = velB + (accelB * dt)
    # Change positions
    FrameA.pos.x = FrameA.pos.x + (velA * dt)
    FrontA.pos.x = FrontA.pos.x + (velA * dt)
    Wheel1A.pos.x = Wheel1A.pos.x + (velA * dt)
    Wheel2A.pos.x = Wheel2A.pos.x + (velA * dt)
    
    FrameB.pos.x = FrameB.pos.x - (velB * dt)
    FrontB.pos.x = FrontB.pos.x - (velB * dt)
    Wheel1B.pos.x = Wheel1B.pos.x - (velB * dt)
    Wheel2B.pos.x = Wheel2B.pos.x - (velB * dt)   
    # Update time
    t = t + dt    

 
#Record values obtained from the while loop
momAfinal = massA * velA
kAfinal = .5 * massA * (velA ** 2)

momBfinal = massB * velB
kBfinal = .5 * massB * (velB ** 2)
# Get the actual answers to the momentum and kinetic energy questions
if kBfinal > kAfinal:
    KEanswer = 'b'
elif kBfinal < kAfinal:
    KEanswer = 'a'
else: KEanswer = '='
        
if momBfinal > momAfinal:
    momA = 'b'
elif momBfinal < momAfinal:
    momA = 'a'
else: momA = '='
        
            
if momQ == momA: # If the users guess about momentum was correct
    if momA == 'b':
        print("\n\nYou were correct about momentum. Car B's momentum is {0:.2f} kgm/s greater than Car A's upon impact.".format(momBfinal - momAfinal))
    elif momA == 'a':
        print("\n\nYou were correct about momentum. Car A's momentum is {0:.2f} kgm/s greater than Car B's upon impact.".format(momAfinal - momBfinal))
    else: print("\n\nYou were correct about momentum. Car A and Car B both have momentum {0:.2f} kgm/s upon impact.".format(momAfinal))
else: # if it was wrong
    if momA == 'b':
        print("\n\nYou were incorrect about momentum. Car B's momentum is {0:.2f} kgm/s greater than Car A's upon impact.".format(momBfinal - momAfinal))
    elif momA == 'a':
        print("\n\nYou were incorrect about momentum. Car A's momentum is {0:.2f} kgm/s greater than Car B's upon impact.".format(momAfinal - momBfinal))
    elif momQ == '=':
        print("\n\nYou were incorrect about momentum. Car A has momentum {0:.2f} and Car B has momentum {1:.2f} kgm/s upon impact.".format(momAfinal, momBfinal))
    else: print("\n\nYou were incorrect about momentum. Car A and Car B both have momentum {0:.2f} kgm/s upon impact.".format(momAfinal))

if KEq == KEanswer: # If the users guess about kinetic energy was correct
    if KEanswer == 'b':
        print("\nYou were correct about kinetic energy. Car B's kinetic energy is {0:.2f} Joules greater than Car A's upon impact.".format(kBfinal - kAfinal))
    elif KEanswer == 'a':
        print("\nYou were correct about kinetic energy. Car A's kinetic energy is {0:.2f} Joules greater than Car B's upon impact.".format(kAfinal - kBfinal))
    else:
        print("\nYou were correct about kinetic energy. Car A and Car B both have kinetic energies of {0:.2f} Joules upon impact.".format(kAfinal))
else: # if it was wrong
    if KEanswer == 'b':
        print("\nYou were incorrect about kinetic energy. Car B's kinetic energy is {0:.2f} Joules greater than Car A's upon impact.".format(kBfinal - kAfinal))
    elif KEanswer == 'a':
        print("\nYou were incorrect about kinetic energy. Car A's kinetic energy is {0:.2f} Joules great than Car B's upon impact.".format(kAfinal - kBfinal))
    elif KEq == '=':
        print("\nYou were incorrect about kinetic energy. Car A has kinetic energy {0:.2f} and Car B has kinetic energy {1:.2f} upon impact.".format(kAfinal, kBfinal))
    else:
        print("\nYou were incorrect about kinetic energy. Car A and Car B both have kinetic energies of {0:.2f} Joules upon impact.".format(kAfinal))

if round(timeQ, 5) == round(t, 5): # Time needs to be rounded otherwise the inexact float value for time that is stored in the computer would throw make a correct guess seem incorrect to the computer.
    print("\nYour time collision estimate was correct. The cars take {0:.3f} seconds to collide.\n".format(t))
elif timeQ > t:
    print("\nYour time until collision estimate was too high. You were off by {0:.3f} seconds.\n".format(timeQ - t))
else: print("\nYour time until collision estimate was too low. You were off by {0:.3f} seconds.\n".format(t - timeQ))
       
