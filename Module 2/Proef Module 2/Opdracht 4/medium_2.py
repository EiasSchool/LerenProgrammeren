from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:

# Start checking positions
position = robotArm.stackIndex()

while position < 9:
    empty = robotArm.stackEmpty()
    if not empty:
        while not empty:
            robotArm.grab()
            robotArm.moveLeft()
            robotArm.drop()
            robotArm.moveRight()
            empty = robotArm.stackEmpty()
    position = robotArm.stackIndex()
    robotArm.moveRight()

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
robotArm.showSolution()
robotArm.wait()