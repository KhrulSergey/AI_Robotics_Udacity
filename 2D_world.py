import numpy as np


#colors=[['green', 'green', 'green'], ['green', 'red', 'green'], ['green', 'green', 'green']]
colors=[['red','green', 'green', 'red','red'],
        ['red','red', 'green', 'red','red'],
        ['red','red', 'green', 'green','red'],
        ['red', 'red', 'red', 'red', 'red']]
dimM = len(colors)
dimP = len(colors[0])
measurements = ['green', 'green', 'green', 'green', 'green']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p_sensor = 0.7
p_move = 0.8
sensor_wrong = 1.0 - p_sensor
p_stay = 1.0 - p_move

def sense(p, colors, measurements):
    #aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    dimRp = len(p)
    dimCp = len(p[0])
    aux = np.full((dimRp, dimCp), 0.0)
    s = 0.0
    for i in range(dimRp):
        for j in range (dimCp):
            hit = (measurements == colors[i][j])
            aux[i][j] = p[i][j]*(hit*p_sensor + (1-hit)*sensor_wrong)
            s += aux[i][j]

    for i in range (dimRp):
        for j in range (dimCp):
            aux[i][j] /= s
    return aux
def move (p, motion):
    dimRp = len(p)
    dimCp = len(p[0])
    aux = np.full((dimRp,dimCp), 0.0)
    for i in range (dimRp):
        for j in range (dimCp):
            k = (i-motion[0])%dimRp
            m = (j-motion[1])%dimCp
            aux[i][j] = p_move * p[k][m] + p_stay*p[i][j]
    return aux
def show (p):
    for i in range(len(p)):
        print(p[i])

if len(measurements) != len(motions):
    raise (ValueError, "error in size of measurements/motions array")

pinit = 1.0 / float(len(colors))/float(len(colors[0]))
p = np.full((dimM, dimP),pinit)
#p = [[pinit for row in range(colors[0])] for col on range(colors)]

for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, colors, measurements[k])
show (p)