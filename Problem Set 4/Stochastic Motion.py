# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']  # Use these when creating your policy grid.


# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid, goal, cost_step, collision_cost, success_prob):
    failure_prob = (1.0 - success_prob) / 2.0  # Probability(stepping left) = prob(stepping right) = failure_prob
    valueMatrix = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    isExpandable = True

    while isExpandable:
        isExpandable = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if valueMatrix[x][y] > 0:
                        valueMatrix[x][y] = 0
                        isExpandable = True
                        policy[x][y] = '*'
                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        currentV = cost_step
                        #calculate different direction values
                        for i in range (-1,2):
                            currentAction = (a + i) % len(delta)
                            currentX = x + delta[currentAction][0]
                            currentY = y + delta[currentAction][1]
                            if a == currentAction:
                                p2 = success_prob
                            else:
                                p2 = failure_prob

                            if (0 <= currentX < len(grid) and 0 <= currentY < len(grid[0])
                                and grid[currentX][currentY] == 0):
                                currentV += p2 * valueMatrix[currentX][currentY]
                            else:
                                currentV += p2 * collision_cost

                        if currentV < valueMatrix[x][y]:
                            isExpandable = True
                            valueMatrix[x][y] = currentV
                            policy[x][y] = delta_name[a]

    return (valueMatrix, policy)

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------- -----------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0]) - 1]  # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.5

(value, policy) = stochastic_value(grid, goal, cost_step, collision_cost, success_prob)
for row in value:
    print (row)
for row in policy:
    print (row)

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
