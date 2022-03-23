# Check if the analysis is successful and change the method to perform the analysis
 
def DynamicAnalysisCollapseSolvers(dt, dt_analysis, GMtime, NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection):
    global CollapseFlag                        # global variable to monitor collapse
    global nIterationsFlag                     # global variable to monitor number of iterations
    global IterationCounter
    IterationCounter = 1
    CollapseFlag = "NO"
    nIterationsFlag = "NO"
    import openseespy.opensees as op
    import os
    op.wipeAnalysis()
    op.constraints('Transformation')
    op.numberer('Plain') 
    op.system('UmfPack')
    op.test('NormDispIncr', 1.0e-8, 50)
    op.algorithm('NewtonLineSearch')   
    op.integrator('Newmark', 0.5, 0.25)
    op.analysis('Transient')
    NumSteps =  round(GMtime/dt_analysis)    # number of steps in analysis
    ok = op.analyze(NumSteps, dt_analysis)
    if  ok == 0:
        print('Dynamic analysis complete')
         
    def MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection):
        import openseespy.opensees as op
        global CollapseFlag
        CollapseFlag = "NO"
        Drift = [0]
        
        for i in range(0,NStories):
            if i==0 :
                Node = FloorNodes[i]
                NodeDisplI = op.nodeDisp(Node, GMdirection)
                
                SDR = NodeDisplI/HStory1
                Drift.insert(i+1, SDR)
            
            elif i > 0 :
                NodeI = FloorNodes[i]
                NodeDisplI = op.nodeDisp(NodeI, GMdirection)
                NodeJ = FloorNodes[i-1]
                NodeDisplJ = op.nodeDisp(NodeJ, GMdirection)
                
                SDR = (NodeDisplI - NodeDisplJ)/HStoryTyp
                Drift.insert(i+1, SDR)
                
        del Drift[0]
        
        MAXDrift = DriftLimit
        
        for h in range(0, NStories):
            TDrift = Drift[h]
            TDrift = abs( TDrift )
            
            if TDrift > MAXDrift:
                CollapseFlag = "YES"
                print("Collapse")
                Collapse_file = open(pathToOutFile+''+'/Collapse.txt','w')
                Collapse_file.write('Collapse!!!!!')
                Collapse_file.close()
    
    # Check Max Drifts for Collapse by Monitoring the CollapseFlag Variable

    MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
    
    if  nIterationsFlag == "YES":
        print("Too many iterations. Stoping Analysis!")
        
    if  CollapseFlag == "YES":
        ok = 0
        print("Collapse Occured")
        
        
        
    # If analysis failed
    if  ok != 0:
        print("Analysis did not converge...")
        # The analysis will be time-controlled and is done for the remaining time
        ok = 0
        controlTime = op.getTime()
     
        # While the GM did not finish OR while analysis is failing
        while controlTime < GMtime or ok != 0 :
            MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
            if  CollapseFlag == "YES":
                ok = 0
                break
            else:
                ok = 1
                
            # Get Control Time inside the loop
            controlTime = op.getTime()
            print("Currently at time controlTime out of GMtime")
     
            if  ok != 0:
                print(" Run Newton 100 steps with 1/2 of step..")
                controlTime = op.getTime()
                remainTime = GMtime - controlTime
                NewRemainSteps = round((remainTime)/(dt_analysis/2.0))
     
                op.test('EnergyIncr', 1.0e-3, 100, 0)
                op.algorithm('KrylovNewton')
                op.integrator('Newmark', 0.50, 0.25)
                dt_analysis_2 = dt_analysis/2.0
                ok = op.analyze(10, dt_analysis_2)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0
                
            if  ok != 0 :
                print(" Go Back to KrylovNewton with tangent Tangent and original step..")
                op.test('EnergyIncr', 1.0e-2, 100, 0)
                controlTime = op.getTime()
                remainTime = GMtime - controlTime
                NewRemainSteps = round((remainTime)/(dt_analysis))
     
                op.algorithm('KrylovNewton')
                op.integrator('Newmark', 0.50, 0.25)
                ok = op.analyze('NewRemainSteps', dt_analysis)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0

            if  ok != 0 :
                print(" Run 10 steps KrylovNewton with Initial Tangent with 1/2 of original step..")
                op.test('EnergyIncr', 1.0e-2, 200, 0)    
                controlTime = op.getTime()
                remainTime = GMtime - controlTime
                NewRemainSteps = round((remainTime)/(dt_analysis_2/2.0))
                op.algorithm('KrylovNewton', '-initial')
                dt_analysis_2 = dt_analysis/2.0
                ok = op.analyze(10, dt_analysis_2)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0

            if  ok != 0 :    
                print(" Go Back to KrylovNewton with tangent Tangent and original step..")
                op.test('EnergyIncr', 1.0e-2, 100, 0)
                controlTime = op.getTime()
                remainTime = GMtime - controlTime
                NewRemainSteps = round((remainTime)/(dt_analysis))
                op.algorithm('KrylovNewton')
                op.integrator('Newmark', 0.50, 0.25)
                ok = op.analyze('NewRemainSteps', dt_analysis)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0    
     
            if  ok != 0 :    
                print("Go Back to KrylovNewton with tangent Tangent and 0.001 step..")
                op.test('EnergyIncr', 1.0e-1, 20, 0)
                controlTime = op.getTime()
                remainTime = GMtime - controlTime
                NewRemainSteps = round((remainTime)/(0.001))
                op.algorithm('KrylovNewton')
                op.integrator('Newmark', 0.50, 0.25)
                ok = op.analyze('NewRemainSteps', 0.001)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0

            if  ok != 0 :
                print(" KrylovNewton Initial with 1/2 of step and Displacement Control Convergence..")
                op.test('EnergyIncr', 1.0e-1, 50, 0)
                op.algorithm('KrylovNewton', '-initial')
                dt_analysis_2 = dt_analysis/2.0
                ok = op.analyze(10, dt_analysis_2)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0

            if  ok != 0 :    
                print(" Go Back to KrylovNewton with tangent Tangent and 0.0001 step..")
                op.test('EnergyIncr', 1.0e-2, 100, 0)
                controlTime = op.getTime()
                remainTime = GMtime - controlTime
                NewRemainSteps = round((remainTime)/(0.0001))
                op.algorithm('KrylovNewton')
                op.integrator('Newmark', 0.50, 0.25)
                ok = op.analyze(5, 0.0001)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0    
     
            if  ok != 0 :    
                print(" Go Back to KrylovNewton with tangent Tangent and original step..")
                op.test('EnergyIncr', 1.0e-2, 100, 0)
                controlTime = op.getTime()
                remainTime = GMtime - controlTime
                NewRemainSteps = round((remainTime)/(dt_analysis))
                op.algorithm('KrylovNewton')
                op.integrator('Newmark', 0.50, 0.25)
                ok = op.analyze('NewRemainSteps', dt_analysis)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0
    
            if  ok != 0 :
                print(" Newton with Fixed Number of Iteratios else continue")
                controlTime = op.getTime()
                remainTime = GMtime - controlTime
                NewRemainSteps = round((remainTime)/(0.0001))
                print(NewRemainSteps)
                op.test('FixedNumIter', 50)
                op.integrator('NewmarkHSFixedNumIter', 0.5, 0.25)
     
                op.algorithm('Newton')
     
                ok = op.analyze(10, 0.0001)
                MaxDriftTester(NStories, DriftLimit, FloorNodes, HStory1, HStoryTyp, GMdirection)
                if  CollapseFlag == "YES":
                    ok = 0
            controlTime = op.getTime()    
