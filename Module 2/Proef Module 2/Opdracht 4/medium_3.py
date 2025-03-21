from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:

color = 'white'
empty = robotArm.stackEmpty()

for i in range(9):
    robotArm.moveRight()

for i in range(9):
    if not empty:
        robotArm.moveLeft()
        robotArm.grab()
        colorScan = robotArm.scan()
        if colorScan == color:
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveLeft()
        else:
            robotArm.drop()

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

