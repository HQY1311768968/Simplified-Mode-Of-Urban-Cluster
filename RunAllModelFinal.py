# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:15:33 2022

@author: DELL
"""

#This code is for run all the MATLAB codes used to build the OpenSees model
#[globals().pop(var) for var in dir() if not var.startswith("__")]
import openseespy.opensees as op
import pickle
op.wipe()

import pandas as pd


for ii in range(929,930):


    # Change variable ID and the number of cycles to run the time history analysis for the required floor
    #ID = [85 4 68 28 129 31 15 33 1 112 537 6 7 709 41 151 179 736 747 755]
    ID = list(range(1,946))
    
    f = open('ii.dat','wb')
    pickle.dump(ii, f)
    f.close()
    

    BuildingID = ID[ii-1]
    f = open('BuildingID.dat','wb')
    pickle.dump(BuildingID, f)
    f.close()

    %run CalculateFloorParameters.py
    
    %run DefineModelNodes.py 
    DefineModelNodes(StoryNumber,m,StoryH)

    %run DefineShearSpring 
    DefineShearSpring(StoryNumber,SK0,Vy,Vp)

    if StoryNumber>8:
        %run DefineBendingSpring 
        DefineBendingSpring(RK0,My,StoryNumber)
   
    %run DefineOutputPath.py
    DefineOutputPath(StoryNumber,BuildingID)

    %run DefineTimeHistoryAnalysis.py
    DefineTimeHistoryAnalysis(StoryNumber,StoryH)

    [globals().pop(var) for var in dir() if not var.startswith("__")]
     
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
    numberOfRunIDs = 29

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
    
    #AllScales = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
    AllScales = [140]
    
    # Running the entire model
    for runNumber in range(29,numberOfRunIDs+1):
   
        global groundMotionID
        global groundMotiondt
        global groundMotionSF
        global numPoints
        
        groundMotionID = groundMotionIDs[runNumber - 1]
        groundMotiondt = groundMotionTimeSteps[runNumber - 1]
        ii = pickle.load(open("ii.dat", "rb"))
        groundMotionSF = groundMotionScaleFactors[ii - 1]
        numPoints = groundMotionNumPoints[runNumber - 1]
        
        for scale in AllScales:
        
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
            f = open('scale.dat','wb')
            pickle.dump(scale, f)
            f.close()
            
            os.chdir(baseDir)
            
            %run ModelNodes
            %run ShearSpring
            StoryNumber = pickle.load(open("StoryNumber.dat", "rb"))
            if StoryNumber>8:
                %run BendingSpring
            %run EigenvalueAnalysis
            %run OutputPath
            %run TimeHistoryAnalysis
            
            op.wipe()
        

    
    
        
