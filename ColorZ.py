#Modify the code below so that the function sense, which
#takes p and Z as inputs, will output the NON-normalized
#probability distribution, q, after multiplying the entries
#in p by pHit or pMiss according to the color in the
#corresponding cell in world.

p=[0, 0.5, 0, 0, 0.5]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['green','red']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    dim = len(p)
    for i in range(dim):
        if Z==world[i]:
            q.append(p[i] * pHit)
        else:
            q.append(p[i] * pMiss)
    sumQ = sum(q)
    if (sumQ != 1):
        if (sumQ > 1):
            for i in range(dim):
                q[i] *= sumQ
        if (sumQ < 1):
            for i in range(dim):
                q[i] /= sumQ
    return q

def move (p, U):
    q=[]
    for i in range (len(p)):
        q.append(p[(i-U)%len(p)])
    return q

#for k in range(len(measurements)):
#    p=sense(p,measurements[k])


print (move (p, 2))