from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:

empty = robotArm.stackEmpty()
position = robotArm.stackIndex()

while position < 2:
    if not empty:
        robotArm.grab()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
        empty = robotArm.stackEmpty()
    else:
         break

robotArm.moveRight()
position = robotArm.stackIndex()

while position == 1:
    robotArm.moveRight()
    empty = robotArm.stackEmpty()
    
    if not empty:
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    else:
        break 

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

