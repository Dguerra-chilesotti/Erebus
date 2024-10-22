from controller import Robot
import math
import time
python_pi = math.pi

timeStep = 32            # Set the time step for the simulation
max_velocity = 6.28      # Set a maximum velocity time constant

# Make robot controller instance
robot = Robot()

'''
Every component on the robot is initialised through robot.getDevice("name") 
If the "name" does not register well, check the custom_robot.proto file in the /games/protos folder
There you will find the configuration for the robot including each component name
'''

# Define the wheels 
wheel1 = robot.getDevice("wheel1 motor")   # Create an object to control the left wheel
wheel2 = robot.getDevice("wheel2 motor") # Create an object to control the right wheel



# Set the wheels to have infinite rotation 
wheel1.setPosition(float("inf"))       
wheel2.setPosition(float("inf"))

# Define distance sensors
s1 = robot.getDevice("distance sensor1")
s2 = robot.getDevice("distance sensor2")
s3 = robot.getDevice("distance sensor3")
s4 = robot.getDevice("distance sensor4")


'''
The names ps0, ps2, etc corresponds to the distance sensors located on the e-puck robot. 
When you create your custom robot the names should change to "distance sensor1", "distance sensor2", etc
The custom_robot.proto file should be refered for any such differences. 
'''

# Enable distance sensors N.B.: This needs to be done for every sensor
s1.enable(timeStep)
s2.enable(timeStep)
s3.enable(timeStep)
s4.enable(timeStep)

#Define the Gyro and enable it
gyro = robot.getDevice("gyro")
gyro.enable(timeStep)

 # pre-set each wheel velocity
speed1 = max_velocity
speed2 = max_velocity

# Mini visualiser for the distance sensors on the console
def numToBlock(num):
    if num > 0.7:
        return '▁'
    elif num > 0.6:
        return '▂'
    elif num > 0.5:
        return '▃'
    elif num > 0.4:
        return '▄'
    elif num > 0.3:
        return '▅'
    elif num > 0.2:
        return '▆'
    elif num > 0.1:
        return '▇'
    elif num > 0:
        return '█'

def go_to(direction):#funzione che come argomento ha la direzione del robot
    speed1 = max_velocity   
    speed2 = max_velocity
    sum = 0
    Degree = 90
    if direction == 'foward':
        speed1 = max_velocity
        speed2 = max_velocity
        print('foward :)')

    if direction == 'backward':
        speed1 = -max_velocity
        speed2 = -max_velocity
    
    if direction == 'right':
        while sum < Degree*1/0.0005:
            sum += radToDegreepersecond(0)
            speed1 = max_velocity
            speed2 = -max_velocity
        
    
    if direction == 'left':
        while sum < Degree*1/0.0005:
            sum += radToDegreepersecond(0)
            speed1 = -max_velocity
            speed2 = max_velocity
        
    
    if direction == 'rotate':
            speed1 = max_velocity
            speed2 = -max_velocity
    
    wheel1.setVelocity(speed1)              
    wheel2.setVelocity(speed2)
    
    
def radToDegreepersecond(dir) :
    axis = gyro.getValues()
    return ((axis[dir])*180)/python_pi

start = robot.getTime()
while robot.step(timeStep) != -1:
    # Display distance values of the sensors
    # For any sensor its readings are obtained via the .getValue() funciton. 
    print(numToBlock(s1.getValue()),numToBlock(s2.getValue()),numToBlock(s3.getValue()),numToBlock(s4.getValue()))
    print(radToDegreepersecond(0),radToDegreepersecond(1),radToDegreepersecond(2))
   
    #go_to('foward')
    go_to('left')
    
  
    
    #vr0001 of trying making movement in the maze and making simple function that help movement as go(position) ect
if(robot.step(timeStep)== -1):   
    print("errrore madornale :)")
    
