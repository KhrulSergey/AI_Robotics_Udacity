from math import *
x = 8
mU = 10
sigmaX2 = 4

def gausFunc (x, mU, sigmaX2):
    normalizer = 1 / sqrt(2*pi*sigmaX2)
    f = normalizer * exp(-0.5 * (x-mU)**2 / sigmaX2)
    return f

print(gausFunc(x,mU,sigmaX2))

#calculate new parameters of current point
#mU and sigmaX2 - aposterious, predicted point
#nU and roX2 - measurement
#return calculated current position
def updateMeasure (mU, sigmaX2, nU, roX2):
    mU_New = 1/(sigmaX2+roX2)*(roX2*mU + sigmaX2*nU)
    sigmaX2_New = 1/(1/sigmaX2 + 1/roX2)
    return [mU_New, sigmaX2_New]

#predict next position based on current and predicted position
def predictMotion (mU, sigmaX2, Ustep, roX2):
    mU_New = mU + Ustep
    sigmaX2_New = sigmaX2 + roX2
    return [mU_New, sigmaX2_New]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sigma = 4.
motion_sigma = 2.
mU = 0.
sigmaX2 = 1000.

for i in range (len(measurements)):
    [mU, sigmaX2] = updateMeasure(mU, sigmaX2, measurements[i],measurement_sigma)
    print("update: ", [mU, sigmaX2])
    [mU, sigmaX2] = predictMotion(mU, sigmaX2, motion[i], motion_sigma)
    print("predict: " , [mU, sigmaX2])