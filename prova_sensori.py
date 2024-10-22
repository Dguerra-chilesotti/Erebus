from controller import Robot

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
wheel1 = robot.getDevice("wheel1")   # Create an object to control the left wheel
wheel2 = robot.getDevice("wheel2") # Create an object to control the right wheel

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

def go_to(direction):
    if direction == 'foward':
        speed1 = max_velocity
        speed2 = max_velocity
    elif direction == 'backward':
        speed1 = -max_velocity
        speed2 = -max_velocity
    
    wheel1.setVelocity(speed1)              
    wheel2.setVelocity(speed2)



start = robot.getTime()
while robot.step(timeStep) != -1:
    # Display distance values of the sensors
    # For any sensor its readings are obtained via the .getValue() funciton. 
    print(numToBlock(s1.getValue()),numToBlock(s2.getValue()),numToBlock(s3.getValue()),numToBlock(s4.getValue()))
    #vr0001 of trying making movement in the maze and making simple function that help movement as go(position) ect
    

    
