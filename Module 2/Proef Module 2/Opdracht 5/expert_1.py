from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:
empty = robotArm.stackEmpty()

robotArm.grab()
for i in range(5):
    robotArm.moveRight()
robotArm.drop()

for i in range(4):
    robotArm.moveLeft()

while True:
    empty = robotArm.stackEmpty()
    if not empty:
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    else: 
        break

robotArm.moveRight()

while True:
    empty = robotArm.stackEmpty()
    if not empty:
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    else:
        break

robotArm.moveRight()

while True:
    empty = robotArm.stackEmpty()
    if not empty:
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    else:
        break

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

