from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:

empty = robotArm.stackEmpty()
robotArm.grab()

BluePos = 9
GreenPos = 8
RedPos = 7

while True:
    color = robotArm.scan()
    position = robotArm.stackIndex()

    if not empty:
        if color == 'blue':
            for i in range(position, BluePos):
                robotArm.moveRight()
            robotArm.drop()
            for i in range((BluePos - 1) - position):
                robotArm.moveLeft()
                empty = robotArm.stackEmpty()
            if not empty:
                robotArm.grab()
        elif color == 'green':
            for i in range(position, GreenPos):
                robotArm.moveRight()
            robotArm.drop()
            for i in range((GreenPos - 1) - position):
                robotArm.moveLeft()
                empty = robotArm.stackEmpty()
            if not empty:
                robotArm.grab()
        elif color == 'red':
            for i in range(position, RedPos):
                robotArm.moveRight()
            robotArm.drop()
            for i in range((RedPos - 1) - position):
                robotArm.moveLeft()
                empty = robotArm.stackEmpty()
            if not empty:
                robotArm.grab()
    else:
        break
        
# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

