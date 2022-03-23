# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:02:53 2022

@author: DELL
"""

#[globals().pop(var) for var in dir() if not var.startswith("__")]
 
import openseespy.opensees as op
import sys
import pickle
import os
op.wipe()

# Dfine the information input path for ground motion
baseDir = os.getcwd() 
pathToAccelFile = baseDir+''+'/GroundMotionAccel'
pathToTextFile = baseDir+''+'/GroundMotionInfo'
 
# Load the ground motion IDs  
groundMotionIDsFile = open(pathToTextFile+''+'/GMFileNames.txt')
groundMotionIDs = groundMotionIDsFile.read()
groundMotionIDs = groundMotionIDs.split('\n')
groundMotionIDsFile.close()

# Define an array of run IDs 
numberOfRunIDs = 44 

# Load the number of points of the ground motion  
groundMotionNumPointsFile = open(pathToTextFile+''+'/GMNumPoints.txt')
groundMotionNumPoints = groundMotionNumPointsFile.read()
groundMotionNumPoints = groundMotionNumPoints.split('\n')
groundMotionNumPointsFile.close()

# Load the time steps of the ground motion
groundMotionTimeStepsFile = open(pathToTextFile+''+'/GMTimeStep.txt')
groundMotionTimeSteps = groundMotionTimeStepsFile.read()
groundMotionTimeSteps = groundMotionTimeSteps.split('\n')
groundMotionTimeStepsFile.close()

# Load the scale factors of the ground motion
groundMotionScaleFactorsFile = open(pathToTextFile+''+'/GMScaleFactor.txt')
groundMotionScaleFactors = groundMotionScaleFactorsFile.read()
groundMotionScaleFactors = groundMotionScaleFactors.split('\n')
groundMotionScaleFactorsFile.close()

# Running the entire model
for runNumber in range(1,numberOfRunIDs+1):
   
    global groundMotionID
    global groundMotiondt
    global groundMotionSF
    global numPoints
    
    groundMotionID = groundMotionIDs[runNumber - 1]
    groundMotiondt = groundMotionTimeSteps[runNumber - 1]
    groundMotionSF = groundMotionScaleFactors[runNumber - 1]
    numPoints = groundMotionNumPoints[runNumber - 1]
    
    f = open('groundMotionID.dat','wb')
    pickle.dump(groundMotionID, f)
    f.close()
    f = open('groundMotiondt.dat','wb')
    pickle.dump(groundMotiondt, f)
    f.close()
    f = open('groundMotionSF.dat','wb')
    pickle.dump(groundMotionSF, f)
    f.close()
    f = open('numPoints.dat','wb')
    pickle.dump(numPoints, f)
    f.close()
    
    os.chdir(baseDir)
    
    %run ModelNodes
    %run ShearSpring
    %run BendingSpring
    %run EigenvalueAnalysis
    %run OutputPath
    %run TimeHistoryAnalysis

    
    op.wipe()