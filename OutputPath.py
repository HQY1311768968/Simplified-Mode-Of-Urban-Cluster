
#  This code is for define the output path of analysis results
 
import os
import openseespy.opensees as op
import pickle
 
# Create a folder for analysis results
baseDir = os.getcwd()
dataDir = baseDir+''+'\Model-Dynamic-Output'
if not os.path.exists(dataDir):
    os.mkdir(dataDir)
EQDir = pickle.load(open('groundMotionID.dat', 'rb'))
if not os.path.exists(dataDir+''+'/799/'):
    os.mkdir(dataDir+''+'/799/')
if not os.path.exists(dataDir+''+'/799/'+''+EQDir):
    os.mkdir(dataDir+''+'/799/'+''+EQDir)
scale = pickle.load(open("scale.dat", "rb"))
scalestr = str(scale)
if not os.path.exists(dataDir+''+'/799/'+''+EQDir+''+'/'+''+scalestr):
    os.mkdir(dataDir+''+'/799/'+''+EQDir+''+'/'+''+scalestr)
# Define the output path
pathToOutFile = dataDir+''+'/799/'+''+EQDir+''+'/'+''+scalestr
 
# record natural period of vibration
periodpath = dataDir+''+'/799'
T1 = pickle.load(open("T1.dat", "rb"))
T2 = pickle.load(open("T2.dat", "rb"))
period_file = open(periodpath+''+'/Periods.txt','w')
period_file.write(str(T1)+''+'      '+''+str(T2))
period_file.close()
 
# record floor displacements	
op.recorder('EnvelopeNode', '-file', pathToOutFile+''+'/Disp-Story.out', '-time', '-node', 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, '-dof', 1, 'disp')
 
# record floor acceleration
GMfile = baseDir+''+'/GroundMotionAccel/'+''+EQDir+''+'.txt'
dt = pickle.load(open("groundMotiondt.dat", "rb"))
groundMotionSF = pickle.load(open("groundMotionSF.dat", "rb")) 
g = 9.8
Scalefact = float(groundMotionSF)*g
op.timeSeries('Path', 1, '-dt', float(dt), '-filePath', GMfile, '-factor', Scalefact)
op.recorder('EnvelopeNode', '-file', pathToOutFile+''+'/Accel-Story.out', '-timeSeries', 1, '-time', '-node', 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, '-dof', 1, 'accel')
 
# record floor velocity
op.recorder('EnvelopeNode', '-file', pathToOutFile+''+'/Vel-Story.out', '-time', '-node', 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, '-dof', 1, 'vel')
 