from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:

empty = robotArm.stackEmpty()

while not empty:
    position = robotArm.stackIndex()
    robotArm.grab()

    color = robotArm.scan()

    if color == 'red':
        for i in range(9 - position):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(9 - position):
            robotArm.moveLeft()
        if robotArm.stackEmpty():
            robotArm.moveRight()
    else:
        robotArm.drop()
        if position < 8:
            robotArm.moveRight()
        else:
            break

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

