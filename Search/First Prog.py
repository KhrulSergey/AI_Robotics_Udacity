# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]] [init[1]] = 1
    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False
    isExpandable = False

    while not found and not isExpandable:
        if len(open) == 0:
            isExpandable = True
            print('Fail to search')
        else:
            open.sort()
            open.reverse()
            next = open.pop()

            x = next[1]
            y = next[2]
            g = next[0]
            if (x == goal[0] and y == goal[1]):
                found = True
                print(next)
                # print('### Search successful ###')
            else:
                for i in range (len(delta)):
                    currentX = x + delta[i][0]
                    currentY = y + delta[i][1]
                    if (0 <= currentX < len(grid) and 0 <= currentY < len(grid[0])):
                        if (closed[currentX][currentY] == 0 and grid[currentX][currentY] == 0):
                            g2 = g + cost
                            open.append([g2, currentX, currentY])
                            # print('append list item')
                            # print('[%f, %f, %f]', % {g2, x2, y2})
                            closed[currentX][currentY] = 1
    # print('New Grid with Path in Zero:')
    # for i in range(len(grid)):
    #     print('  ', grid[i])

search()
