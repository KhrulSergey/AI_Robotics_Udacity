# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):

    valueMatrix = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    isExpandable = True

    while isExpandable:
       isExpandable = False
       for x in range(len(grid)):
           for y in range(len(grid[0])):
               if goal[0] == x and goal[1] == y:
                   if valueMatrix[x][y] > 0:
                       valueMatrix[x][y] = 0
                       isExpandable = True
               elif grid[x][y] == 0:
                   for k in range(len(delta)):
                       currentX = x + delta[k][0]
                       currentY = y + delta[k][1]
                       if (0 <= currentX < len(grid) and 0 <= currentY < len(grid[0])
                           and grid[currentX][currentY] == 0):
                           currentV = valueMatrix[currentX][currentY] + cost
                           if currentV < valueMatrix[x][y]:
                               isExpandable = True
                               valueMatrix[x][y] = currentV
    return (valueMatrix)



valueMatrix = compute_value(grid, goal, cost)

for i in range(len(valueMatrix)):
    print(valueMatrix[i])