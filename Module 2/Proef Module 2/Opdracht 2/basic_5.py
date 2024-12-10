from RobotArm import RobotArm

# Import the challenges (in this case challenges/basic.py)
from challenges.basic import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:

robotArm.moveRight()
robotArm.grab()

color = robotArm.scan()

if color == 'red':
    robotArm.moveLeft()
elif color == 'yellow':
    robotArm.moveRight()

# your code ends here

robotArm.drop()

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()