# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:05:48 2022

@author: DELL
"""
# This code is for define Time history analysis function

def DefineTimeHistoryAnalysis(StoryNumber,StoryH):

    fid = open('TimeHistoryAnalysis.py','w')
    fid.write('\n#  This code is for define time history analysis ')
    fid.write('\n')
    fid.write('\nimport openseespy.opensees as op')
    fid.write('\nimport os')
    fid.write('\nimport pickle')
    fid.write('\n')
    fid.write('\n# Check whether the previous code is working correctly')
    fid.write('\nprint("Running dynamic analysis...")')
    fid.write('\n')
    fid.write('\nbaseDir = os.getcwd()')
    fid.write('\n')
    
    fid.write('\n# Rayleigh Damping')
    fid.write('\n# Calculate damping parameters')
    fid.write('\nzeta  = 0.04		# percentage of critical damping')
    fid.write('\nimport math')
    fid.write('\npi = math.pi')
    fid.write('\nT1 = pickle.load(open("T1.dat", "rb"))')
    fid.write('\nT2 = pickle.load(open("T2.dat", "rb"))')
    fid.write('\nw1 = 2.0*pi/T1')
    fid.write('\nw2 = 2.0*pi/T2')
    fid.write('\na0 = zeta*2.0*w1*w2/(w1 + w2)')
    fid.write('\na1 = zeta*2.0/(w1 + w2)')
    
    fid.write('\n ')
    fid.write('\n# Assign damping to mode and element')
    if StoryNumber<9:
        fid.write("\nop.region(3, '-eleRange', 1111, 111"+''+str(StoryNumber)+''+", '-rayleigh', 0.0, 0.0, a1, 0.0)")
    else:
        fid.write("\nop.region(3, '-eleRange', 1111, 222"+''+str(StoryNumber)+''+", '-rayleigh', 0.0, 0.0, a1, 0.0)")
    fid.write("\nop.region(4, '-node', ")
    for ii in range(1,StoryNumber+1):
        fid.write('1'+''+str(ii)+''+', ')
    if StoryNumber>8:
        for ii in range(1,StoryNumber+1):
            fid.write('2'+''+str(ii)+''+', ')
    fid.write("'-rayleigh', a0, 0.0, 0.0, 0.0)")
    
    fid.write('\n ')
    fid.write('\n# Define ground motion parameters')
    fid.write('\npatternID = 1            # load pattern ID')
    fid.write('\nGMdirection = 1')
    fid.write('\ndt = pickle.load(open("groundMotiondt.dat", "rb"))')
    fid.write('\nTotalNumberOfSteps = pickle.load(open("numPoints.dat", "rb"))	# number of steps in ground motion')
    fid.write('\nGMtime = float(dt)*float(TotalNumberOfSteps) + 10.0	# total time of ground motion + 10 sec of free vibration')
    fid.write('\n ')
    
    fid.write('\n# Define the acceleration series for the ground motion')
    fid.write('\nEQDir = pickle.load(open("groundMotionID.dat", "rb"))')
    fid.write("\nGMfile = baseDir+''+'/GroundMotionAccel/'+''+EQDir+''+'.txt'")
    fid.write('\ngroundMotionSF = pickle.load(open("groundMotionSF.dat", "rb")) ')
    fid.write('\ng = 9.8')
    fid.write('\n ')
    
    fid.write('\nscale = pickle.load(open("scale.dat", "rb"))')
    fid.write('\nScalefact = float(groundMotionSF)*scale/100*g')
    fid.write("\nop.timeSeries('Path', 501, '-dt', float(dt), '-filePath', GMfile, '-factor', Scalefact)")
    fid.write('\n ')
    
    fid.write('\n# Create load pattern: apply acceleration to all fixed nodes with UniformExcitation')
    fid.write("\nop.pattern('UniformExcitation', patternID, GMdirection, '-accel', 501)")
    fid.write('\n ')
    
    fid.write('\n# Define a list of nodes')
    fid.write('\nFloorNodes = [10')
    for ii in range(1,StoryNumber+1):
        fid.write(', 1'+''+str(ii))
    
    if StoryNumber>8:
        for ii in range(1,StoryNumber+2):
            fid.write(', 2'+''+str(ii-1))
    fid.write(']')
    fid.write('\n ')
    
    fid.write('\n# Define dynamic analysis parameters')
    fid.write('\ndt_analysis = float(dt)/8')
    fid.write('\n ')
    
    fid.write('\n# Run Dynamic Analysis Collapse Solver ')
    fid.write('\nNStories = '+''+str(StoryNumber))
    fid.write('\nHStory1 = '+''+str(StoryH))
    fid.write('\nHStoryTyp = '+''+str(StoryH))
    fid.write('\nfrom DynamicAnalysisCollapseSolver import *')
    fid.write('\nDynamicAnalysisCollapseSolvers(dt, dt_analysis, GMtime, NStories, 0.1, FloorNodes, HStory1, HStoryTyp, GMdirection)')
    fid.write('\n ')
    fid.write('\n# Clear data')
    fid.write('\nop.wipe()')
    
    fid.close()
    
    