# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [1, 1, 1, 0, 0, 0]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

# cost has 3 values, corresponding to making
#  a right turn, no turn, and a left turn
cost_move = [0, 1, 20]

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

def optimum_policy2D(grid, init, goal, cost):

    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    policy = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(len(forward)):
                    if goal[0] == x and goal[1] == y:
                        if value[orientation][x][y] > 0:
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                            change = True

                    elif grid[x][y] == 0:
                        #find 3 ways to move(act)
                        for a in range(len(action)):
                            currentOrient = (orientation + action[a])%4
                            currentX = x + forward[currentOrient][0]
                            currentY = y + forward[currentOrient][1]

                            if (0 <= currentX < len(grid) and 0 <= currentY < len(grid[0])
                                and grid[currentX][currentY] == 0):
                                currentV = value[currentOrient][currentX][currentY] + cost[a]
                                if currentV < value[orientation][x][y]:
                                    change = True
                                    value[orientation][x][y] = currentV
                                    policy[orientation][x][y] = action_name[a]
    x = init[0]
    y = init[1]
    orientation = init[2]
    policy2D[x][y] = policy[orientation][x][y]
    while policy[orientation][x][y] != '*':
        if policy[orientation][x][y] == '#':
            currentOrient = orientation
        elif policy[orientation][x][y] == 'L':
            currentOrient = (orientation + 1)%4
        elif policy[orientation][x][y] == 'R':
            currentOrient = (orientation - 1)%4
        x = x + forward[currentOrient][0]
        y = y + forward[currentOrient][1]
        orientation = currentOrient
        policy2D[x][y] = policy[orientation][x][y]
    return policy2D

policy = optimum_policy2D(grid, init, goal, cost_move)
for i in range(len(policy)):
    print (policy[i])
