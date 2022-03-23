#  This code is for eigenvalue analysis 

import openseespy.opensees as op
import pickle

#  Eigenvalue analysis 
import math
pi = math.pi
nEigenI = 1
nEigenJ = 2
lambdaN = op.eigen('-fullGenLapack', nEigenJ)
lambdaI = lambdaN[0]
lambdaJ = lambdaN[1]
global w1
global w2
w1 = math.sqrt(lambdaI)
w2 = math.sqrt(lambdaJ)
T1 = 2.0*pi/w1
T2 = 2.0*pi/w2

f = open('T1.dat','wb')
pickle.dump(T1, f)
f.close()
f = open('T2.dat','wb')
pickle.dump(T2, f)
f.close()

print('T1 = ',T1)
print('T2 = ',T2)



