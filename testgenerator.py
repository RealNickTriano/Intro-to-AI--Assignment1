import os
import shutil
import random

# Constants
folderName = "./tests/"
gridSize_x = 100
gridSize_y = 50
blockedRatio = .1
numberOfTests = 50

# Checks if point is free/not blocked
def pointFree(p, nodes):
    startX = p[0]
    startY = p[1]

    # If the point blocked then:
    if nodes[(startX, startY)] == False:
        # Check above point
        if startY > 0 and nodes[(startX, startY - 1)]:
            return True
        # Check left point
        if startX > 0 and nodes[(startX - 1, startY)]:
            return True
        # Check top left point
        if startX > 0 and startY > 0 and nodes[(startX - 1, startY - 1)]:
            return True
        return False
    return True

def goal(nodes):

    # Starting point
    while True:
        startX = random.randrange(gridSize_x)
        startY = random.randrange(gridSize_y)
        start = (startX, startY)
        if pointFree(start, nodes):
            break

    # Goal/finishing point
    while True:
        goalX = random.randrange(gridSize_x)
        goalY = random.randrange(gridSize_y)
        goal = (goalX, goalY)
        if goal != start and pointFree(goal, nodes):
            break

    return (start, goal)


# Generate open and blocked cells
def graphGenerator(nodes):
    for x in range(gridSize_x):
        for y in range(gridSize_y):
            nodes[(x,y)] = True

    currentBlockedRatio = float(0)
    blockedCells = 0
    while currentBlockedRatio < blockedRatio:
        randomX = random.randrange(gridSize_x)
        randomY = random.randrange(gridSize_y)
        if nodes[(randomX, randomY)] == True:
            nodes[(randomX, randomY)] = False
            blockedCells += 1
            # total blocked / grid size
            currentBlockedRatio = float(blockedCells / (gridSize_x * gridSize_y))

directory = os.path.join(os.getcwd(), folderName)

# Delete existing directory to avoid file exists error
if os.path.exists(directory):
    shutil.rmtree(directory)

# Create the graphs directory
os.mkdir(directory)

# Generate test files
for i in range(numberOfTests):
    nodes = dict()
    graphGenerator(nodes)
    goalPoints = goal(nodes)
    filename = directory + "test_" + str(i + 1).zfill(2) + ".txt"
    with open(filename, 'w') as f:
        f.write(str(goalPoints[0][0] + 1) + " " + str(goalPoints[0][1] + 1) + "\n")
        f.write(str(goalPoints[1][0] + 1) + " " + str(goalPoints[1][1] + 1) + "\n")
        f.write(str(gridSize_x) + " " + str(gridSize_y) + "\n")
        for x in range(gridSize_x):
            for y in range(gridSize_y):
                blocked = 0
                if not nodes[(x,y)]:
                    blocked = 1
                f.write(str(x + 1) + " " + str(y + 1) + " " + str(blocked) + "\n")
