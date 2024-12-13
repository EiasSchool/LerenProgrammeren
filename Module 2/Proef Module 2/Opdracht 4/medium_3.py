from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:

position = robotArm.stackIndex()

while position < 9:
    empty = robotArm.stackEmpty()

    if not empty:
        robotArm.grab()
        color = robotArm.scan()
        if color == 'white':
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveRight()
        else:
            robotArm.drop()
            robotArm.moveRight()
    else:
        robotArm.moveRight()
    position = robotArm.stackIndex()

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

