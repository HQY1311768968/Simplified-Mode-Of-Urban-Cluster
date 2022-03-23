# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:01:19 2022

@author: DELL
"""
#This code is for shear spring definition

def DefineShearSpring(StoryNumber,SK0,Vy,Vp):
    
    fid = open('ShearSpring.py','w')
    fid.write('\n# This code is for define shear spring material and shear spring elements')
    fid.write('\n ')
    fid.write('\nimport openseespy.opensees as op')
    fid.write('\n ')
    
    if StoryNumber>8:
        SK1 = 0.35*SK0
    else:
        SK1 = SK0

    fid.write('\n# Load the initial stiffness(SK1) and yield stiffness(SK2) of the shear springs')
    fid.write('\nSK1 = '+''+str(SK1))
    fid.write('\nSK2 = 0.25*SK1')
    fid.write('\n ')
    
    fid.write('\n# Load the yield shear force of the shear spring on each floor')
    for ii in range(1,StoryNumber+1):
        fid.write('\nVy'+''+str(ii)+''+' = '+''+str(Vy[ii-1,0]))
    fid.write('\n ')
    
    fid.write('\n# Calculate the yield shear displacements of the shear spring on each floor')
    for ii in range(1,StoryNumber+1):
        fid.write('\nuy'+''+str(ii)+''+' = Vy'+''+str(ii)+''+'/SK1')
    fid.write('\n ')
    
    fid.write('\n# Calculate the shear force at the peak point of the shear springs')
    for ii in range(1,StoryNumber+1):
        fid.write('\nVp'+''+str(ii)+''+' = '+''+str(Vp[ii-1,0]))
    fid.write('\n ')
    
    fid.write('\n# Calculate the displacement of the peak point of the shear springs')
    for ii in range(1,StoryNumber+1):
        fid.write('\nup'+''+str(ii)+''+' = (Vp'+''+str(ii)+''+'-Vy'+''+str(ii)+''+')/SK2+Vy'+''+str(ii)+''+'/SK1')
    fid.write('\n ')
    
    fid.write('\n# Define shear spring material')
    for ii in range(1,StoryNumber+1):
        fid.write('\ntenup'+''+str(ii)+''+' = 10*up'+''+str(ii))
        fid.write('\nVy'+''+str(ii)+''+'ne  = -1*Vy'+''+str(ii))
        fid.write('\nuy'+''+str(ii)+''+'ne  = -1*uy'+''+str(ii))
        fid.write('\nVp'+''+str(ii)+''+'ne  = -1*Vp'+''+str(ii))
        fid.write('\nup'+''+str(ii)+''+'ne  = -1*up'+''+str(ii))
        fid.write('\nVp'+''+str(ii)+''+'ne  = -1*Vp'+''+str(ii))
        fid.write('\ntenup'+''+str(ii)+''+'ne = -1*tenup'+''+str(ii))
        fid.write("\nop.uniaxialMaterial('Hysteretic', "+''+str(ii)+''+', Vy'+''+str(ii)+''+', uy'+''+str(ii)+''+', Vp'+''+str(ii)+''+', up'+''+str(ii)+''+', Vp'+''+str(ii)+''+', tenup'+''+str(ii)+''+', Vy'+''+str(ii)+''+'ne, uy'+''+str(ii)+''+'ne, Vp'+''+str(ii)+''+'ne, up'+''+str(ii)+''+'ne, Vp'+''+str(ii)+''+'ne, tenup'+''+str(ii)+''+'ne, 1.0, 1.0, 0.0, 0.0) ')
        fid.write('\n ')
    fid.write('\n ')
    
    fid.write('\n# Define materials whose stiffness is much greater or much less than the springs')
    fid.write("\nop.uniaxialMaterial('Elastic', 11111, 1e20)")
    fid.write('\n ')
    
    fid.write('\n# Define bing spring elements')
    if StoryNumber<9:
        for ii in range(1,StoryNumber+1):
            fid.write("\nop.element('zeroLength', 111"+''+str(ii)+''+', '+''+str(ii)+''+str(ii-1)+''+'1, '+''+str(ii)+''+str(ii-1)+''+"2, '-mat', "+''+str(ii)+''+", 11111, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1)")
        fid.write('\n ')
    else:
        for ii in range(1,StoryNumber+1):
            fid.write("\nop.element('twoNodeLink', 111"+''+str(ii)+''+', 2'+''+str(ii-1)+''+', 2'+''+str(ii)+''+", '-mat', 11111, "+''+str(ii)+''+", 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)")
        fid.write('\n ')
    
    fid.close()
    
    