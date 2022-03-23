# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:39:46 2022

@author: DELL
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:01:19 2022

@author: DELL
"""
#This code is for bending spring definition

def DefineBendingSpring(RK0,My,StoryNumber):
    
    fid = open('BendingSpring.py','w')
    fid.write('\n# This code is for define bending spring material and bending spring elements')
    fid.write('\n ')
    fid.write('\nimport openseespy.opensees as op')
    fid.write('\n ')
    
    if StoryNumber>8:
        RK1 = 0.35*RK0
    else:
        RK1 = RK0

    fid.write('\n# Load the initial stiffness(RK1) and yield stiffness(SK2) of the bending springs')
    fid.write('\nRK1 = '+''+str(RK1))
    fid.write('\nSK2 = 0.25*RK1')
    fid.write('\n ')
    
    fid.write('\n# Load the yield shear force of the bending spring on each floor')
    for ii in range(1,StoryNumber+1):
        fid.write('\nMy'+''+str(ii)+''+' = '+''+str(My[ii-1,0]))
    fid.write('\n ')
    
    fid.write('\n# Calculate the yield shear displacements of the bending spring on each floor')
    for ii in range(1,StoryNumber+1):
        fid.write('\nsetay'+''+str(ii)+''+' = My'+''+str(ii)+''+'/RK1')
    fid.write('\n ')
    
    fid.write('\n# Calculate the shear force at the peak point of the bending springs')
    for ii in range(1,StoryNumber+1):
        fid.write('\nMp'+''+str(ii)+''+' = 2.23*My'+''+str(ii))
    fid.write('\n ')
    
    fid.write('\n# Calculate the displacement of the peak point of the bending springs')
    for ii in range(1,StoryNumber+1):
        fid.write('\nsetap'+''+str(ii)+''+' = (Mp'+''+str(ii)+''+'-My'+''+str(ii)+''+')/SK2+My'+''+str(ii)+''+'/RK1')
    fid.write('\n ')
    
    fid.write('\n# Define bending spring material')
    for ii in range(1,StoryNumber+1):
        fid.write('\ntensetap'+''+str(ii)+''+' = 10*setap'+''+str(ii))
        fid.write('\nMy'+''+str(ii)+''+'ne  = -1*My'+''+str(ii))
        fid.write('\nsetay'+''+str(ii)+''+'ne  = -1*setay'+''+str(ii))
        fid.write('\nMp'+''+str(ii)+''+'ne  = -1*Mp'+''+str(ii))
        fid.write('\nsetap'+''+str(ii)+''+'ne  = -1*setap'+''+str(ii))
        fid.write('\nMp'+''+str(ii)+''+'ne  = -1*Mp'+''+str(ii))
        fid.write('\ntensetap'+''+str(ii)+''+'ne = -1*tensetap'+''+str(ii))
        fid.write("\nop.uniaxialMaterial('Hysteretic', "+''+str(StoryNumber+ii)+''+', My'+''+str(ii)+''+', setay'+''+str(ii)+''+', Mp'+''+str(ii)+''+', setap'+''+str(ii)+''+', Mp'+''+str(ii)+''+', tensetap'+''+str(ii)+''+', My'+''+str(ii)+''+'ne, setay'+''+str(ii)+''+'ne, Mp'+''+str(ii)+''+'ne, setap'+''+str(ii)+''+'ne, Mp'+''+str(ii)+''+'ne, tensetap'+''+str(ii)+''+'ne, 1.0, 1.0, 0.0, 0.0) ')
        fid.write('\n ')
    fid.write('\n ')
       
    fid.write('\n# Define bing spring elements')
    for ii in range(1,StoryNumber+1):
        fid.write("\nop.element('twoNodeLink', 222"+''+str(ii)+''+', 1'+''+str(ii-1)+''+', 1'+''+str(ii)+''+", '-mat', 11111, 11111, "+''+str(StoryNumber+ii)+''+", '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)")
    fid.write('\n ')
    
    fid.close()
    