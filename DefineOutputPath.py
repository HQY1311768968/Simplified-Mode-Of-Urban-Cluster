# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:18:09 2022

@author: DELL
"""

#This code is for Ddefine the output path of analysis results

def DefineOutputPath(StoryNumber,BuildingID):
    fid = open('OutputPath.py','w')
    
    fid.write('\n#  This code is for define the output path of analysis results')
    fid.write('\n ')
    
    fid.write('\nimport os')
    fid.write('\nimport openseespy.opensees as op')
    fid.write('\nimport pickle')
    fid.write('\n ')
    
    fid.write('\n# Create a folder for analysis results')
    fid.write('\nbaseDir = os.getcwd()')
    fid.write("\ndataDir = baseDir+''+'\Model-Dynamic-Output'")
    fid.write('\nif not os.path.exists(dataDir):')
    fid.write('\n    os.mkdir(dataDir)')
    fid.write("\nEQDir = pickle.load(open('groundMotionID.dat', 'rb'))")
    fid.write("\nif not os.path.exists(dataDir+''+'/"+''+str(BuildingID)+''+"/'):")
    fid.write("\n    os.mkdir(dataDir+''+'/"+''+str(BuildingID)+''+"/')")
    fid.write("\nif not os.path.exists(dataDir+''+'/"+''+str(BuildingID)+''+"/'+''+EQDir):")
    fid.write("\n    os.mkdir(dataDir+''+'/"+''+str(BuildingID)+''+"/'+''+EQDir)")
    fid.write('\nscale = pickle.load(open("scale.dat", "rb"))')
    fid.write('\nscalestr = str(scale)')
    fid.write("\nif not os.path.exists(dataDir+''+'/"+''+str(BuildingID)+''+"/'+''+EQDir+''+'/'+''+scalestr):")
    fid.write("\n    os.mkdir(dataDir+''+'/"+''+str(BuildingID)+''+"/'+''+EQDir+''+'/'+''+scalestr)")
    fid.write('\n# Define the output path')
    fid.write("\npathToOutFile = dataDir+''+'/"+''+str(BuildingID)+''+"/'+''+EQDir+''+'/'+''+scalestr") 
    fid.write('\n ')
    
    fid.write('\n# record natural period of vibration')
    fid.write("\nperiodpath = dataDir+''+'/"+''+str(BuildingID)+''+"'")
    fid.write('\nT1 = pickle.load(open("T1.dat", "rb"))')
    fid.write('\nT2 = pickle.load(open("T2.dat", "rb"))')
    fid.write("\nperiod_file = open(periodpath+''+'/Periods.txt','w')")
    fid.write("\nperiod_file.write(str(T1)+''+'      '+''+str(T2))")
    fid.write('\nperiod_file.close()')
    fid.write('\n ')
    
    fid.write('\n# record floor displacements	')
    fid.write("\nop.recorder('Node', '-file', pathToOutFile+''+'/Disp-Story.out', '-time', '-node', ")
    for ii in range(1,StoryNumber+1):
        fid.write('1'+''+str(ii)+''+', ')
    fid.write("'-dof', 1, 'disp')")
    fid.write('\n ')
    
    #fid.write('\n# record floor acceleration')
    #fid.write("\nGMfile = baseDir+''+'/GroundMotionAccel/'+''+EQDir+''+'.txt'")
    #fid.write('\ndt = pickle.load(open("groundMotiondt.dat", "rb"))')
    #fid.write('\ngroundMotionSF = pickle.load(open("groundMotionSF.dat", "rb")) ')
    #fid.write('\ng = 9.8')
    #fid.write('\nScalefact = float(groundMotionSF)*g')
    #fid.write("\nop.timeSeries('Path', 1, '-dt', float(dt), '-filePath', GMfile, '-factor', Scalefact)")
    #fid.write("\nop.recorder('EnvelopeNode', '-file', pathToOutFile+''+'/Accel-Story.out', '-timeSeries', 1, '-time', '-node', ")
    #for ii in range(1,StoryNumber+1):
    #    fid.write('1'+''+str(ii)+''+', ')
    #fid.write("'-dof', 1, 'accel')")
    #fid.write('\n ')
    
    #fid.write('\n# record floor velocity')
    #fid.write("\nop.recorder('EnvelopeNode', '-file', pathToOutFile+''+'/Vel-Story.out', '-time', '-node', ")
    #for ii in range(1,StoryNumber+1):
    #    fid.write('1'+''+str(ii)+''+', ')
    #fid.write("'-dof', 1, 'vel')")
    #fid.write('\n ')
    
    #fid.write('\n# record base shear reactions')
    #fid.write("\nop.recorder('Node', '-file', pathToOutFile+''+'/Vbase.out', '-node', 10, '-dof', 1, 'reaction')")
    #fid.write('\n ')
    
    #fid.write('\n# record response history of all bing springs and shear springs ')
    #fid.write("\nop.region(1, '-ele'")
    #for ii in range(1,StoryNumber+1):
    #    fid.write(', 111'+''+str(ii))
    #fid.write(')')
    #fid.write("\nop.recorder('Element', '-file', pathToOutFile+''+'/ForceShearSpringsBasic.out', '-time', '-region', 1, 'basicForce')")
    #fid.write("\nop.recorder('Element', '-file', pathToOutFile+''+'/DisShearSpringsBasic.out', '-time', '-region', 1, 'basicDisplacement')")
    #fid.write('\n ')
    #
    #
    #if StoryNumber>8:
    #    fid.write("\nop.region(2, '-ele'")
    #    for ii in range(1,StoryNumber+1):
    #        fid.write(', 222'+''+str(ii))
    #    fid.write(')')
    #    fid.write("\nop.recorder('Element', '-file', pathToOutFile+''+'/ForceBendingSpringsBasic.out', '-time', '-region', 2, 'basicForce')")
    #    fid.write("\nop.recorder('Element', '-file', pathToOutFile+''+'/DisBendingSpringsBasic.out', '-time', '-region', 2, 'basicDisplacement')")
    
    fid.close()
