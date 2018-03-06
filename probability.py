#Modify the code below so that the function sense, which
#takes p and Z as inputs, will output the NON-normalized
#probability distribution, q, after multiplying the entries
#in p by pHit or pMiss according to the color in the
#corresponding cell in world.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red','red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

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
        s = pExact * p[(i - U) % len(p)]
        s = s + pOvershoot * p[(i - U - 1) % len(p)]
        s = s + pUndershoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q

#for k in range(len(measurements)):
#    p=sense(p,measurements[k])

for i in range(len(motions)):
    p = sense(p, measurements[i])
    p=move (p, motions[i])


print (p)