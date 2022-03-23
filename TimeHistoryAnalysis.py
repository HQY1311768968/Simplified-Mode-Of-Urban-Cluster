
#  This code is for define time history analysis 

import openseespy.opensees as op
import os
import pickle

# Check whether the previous code is working correctly
print("Running dynamic analysis...")

baseDir = os.getcwd()

# Rayleigh Damping
# Calculate damping parameters
zeta  = 0.04		# percentage of critical damping
import math
pi = math.pi
T1 = pickle.load(open("T1.dat", "rb"))
T2 = pickle.load(open("T2.dat", "rb"))
w1 = 2.0*pi/T1
w2 = 2.0*pi/T2
a0 = zeta*2.0*w1*w2/(w1 + w2)
a1 = zeta*2.0/(w1 + w2)
 
# Assign damping to mode and element
op.region(3, '-eleRange', 1111, 22235, '-rayleigh', 0.0, 0.0, a1, 0.0)
op.region(4, '-node', 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 21, 22, 23, 24, 25, 26, 27, 28, 29, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, '-rayleigh', a0, 0.0, 0.0, 0.0)
 
# Define ground motion parameters
patternID = 1            # load pattern ID
GMdirection = 1
dt = pickle.load(open("groundMotiondt.dat", "rb"))
TotalNumberOfSteps = pickle.load(open("numPoints.dat", "rb"))	# number of steps in ground motion
GMtime = float(dt)*float(TotalNumberOfSteps) + 10.0	# total time of ground motion + 10 sec of free vibration
 
# Define the acceleration series for the ground motion
EQDir = pickle.load(open("groundMotionID.dat", "rb"))
GMfile = baseDir+''+'/GroundMotionAccel/'+''+EQDir+''+'.txt'
groundMotionSF = pickle.load(open("groundMotionSF.dat", "rb")) 
g = 9.8
 
scale = pickle.load(open("scale.dat", "rb"))
Scalefact = float(groundMotionSF)*scale/100*g
op.timeSeries('Path', 501, '-dt', float(dt), '-filePath', GMfile, '-factor', Scalefact)
 
# Create load pattern: apply acceleration to all fixed nodes with UniformExcitation
op.pattern('UniformExcitation', patternID, GMdirection, '-accel', 501)
 
# Define a list of nodes
FloorNodes = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235]
 
# Define dynamic analysis parameters
dt_analysis = 0.01
 
# Run Dynamic Analysis Collapse Solver 
NStories = 35
HStory1 = 4.0
HStoryTyp = 4.0
from DynamicAnalysisCollapseSolver import *
DynamicAnalysisCollapseSolvers(dt, dt_analysis, GMtime, NStories, 0.1, FloorNodes, HStory1, HStoryTyp, GMdirection)
 
# Clear data
op.wipe()