from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:

colors = {}
empty = robotArm.stackEmpty()

for scanColors in range(1, 10):
    robotArm.moveRight()
    robotArm.grab()
    colorFound = robotArm.scan()
    if colorFound in colors:
        colors[colorFound] += 1
    else:
        colors[colorFound] = 1
    robotArm.drop()

highest_color = max(colors, key=colors.get)

print(colors)
print(f'The most frequent color is {highest_color}')

for moveLeft in range(9):
    robotArm.moveLeft()

for moveHighestColorToStart in range(1, 10):
    robotArm.moveRight()
    robotArm.grab()
    current_color = robotArm.scan()
    if current_color == highest_color:
        current_position = moveHighestColorToStart
        for moveLeft in range(current_position):
            robotArm.moveLeft()
        robotArm.drop()
        for moveRight in range(current_position):
            robotArm.moveRight() 
    else:
        robotArm.drop()

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

