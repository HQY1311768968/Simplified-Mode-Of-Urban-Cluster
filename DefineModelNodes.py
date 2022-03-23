#This code is for define the nodes

def DefineModelNodes(StoryNumber,m,StoryH):

    fid = open('ModelNodes.py','w')
    fid.write('# This code is for define all nodes required by the model')
    fid.write('\n')
    
    fid.write('\nimport openseespy.opensees as op')
    fid.write('\nimport pickle')
    fid.write('\n')
    
    fid.write('\n# Define the dimensions and degrees of freedom of the model')
    fid.write("\nop.model('basic', '-ndm', 2, '-ndf', 3) ")
    fid.write('\n')
    
    fid.write('\n# Define structure-geometry parameters')
    fid.write('\nNStories = '+''+str(StoryNumber))
    fid.write('\nHStory1 = '+''+str(StoryH))
    fid.write('\nHStoryTyp = '+''+str(StoryH))
    fid.write('\n')
    

    if StoryNumber>8:
    
        fid.write('\n# Define nodal masses')
        fid.write('\nNodalMassTyp = '+''+str(m)+''+'/2')
        fid.write('\nNegligible = 1e-9')
        fid.write('\n')
        
        Pier1 = 0.0
        Pier2 = 4.0
    
        fid.write('\n# Define the concentrated mass node on the left side of the floor')
        fid.write('\nop.node(10, 0.0, 0.0 )')
        for ii in range(1,StoryNumber+1):
            fid.write('\nop.node(1'+''+str(ii)+''+', '+''+str(Pier1)+''+', '+''+str(StoryH*ii)+''+'  )')
        fid.write('\n')
        
        for ii in range(1,StoryNumber+1):
            fid.write('\nop.mass(1'+''+str(ii)+''+', NodalMassTyp, Negligible, Negligible)')
        fid.write('\n')
        
        fid.write('\n# Define the concentrated mass node on the right side of the floor')
        fid.write('\nop.node(20, 4.0, 0.0 )')
        for ii in range(1,StoryNumber+1):
            fid.write('\nop.node(2'+''+str(ii)+''+', '+''+str(Pier2)+''+', '+''+str(StoryH*ii)+''+'  )')
        fid.write('\n')
        
        for ii in range(1,StoryNumber+1):
            fid.write('\nop.mass(2'+''+str(ii)+''+', NodalMassTyp, Negligible, Negligible)')
        fid.write('\n')
        
        fid.write('\n# Define boundary conditions')
        fid.write('\nop.fix(10, 1,1,1)')
        fid.write('\nop.fix(20, 1,1,1)')
        fid.write('\n')
        
        fid.write('\n# Define the freedom constraints between nodes')
        for ii in range(1,StoryNumber+1):
            fid.write('\nop.equalDOF(1'+''+str(ii)+''+',2'+''+str(ii)+''+',1)')
        
    else:
    
        fid.write('\n# Define nodal masses')
        fid.write('\nNodalMassTyp = '+''+str(m))
        fid.write('\nNegligible = 1e-9')
        fid.write('\n')
        
        Pier1 = 0.0
    
        fid.write('\nop.node(10, 0.0, 0.0 )')
        for ii in range(1,StoryNumber+1):
            fid.write('\nop.node(1'+''+str(ii)+''+', '+''+str(Pier1)+''+', '+''+str(StoryH*ii)+''+'  )')
        fid.write('\n')
        
        for ii in range(1,StoryNumber+1):
            fid.write('\nop.mass(1'+''+str(ii)+''+', NodalMassTyp, Negligible, Negligible)')
        fid.write('\n')
        
        fid.write('\n# Define spring element nodes (located between two floor nodes)')
        for ii in range(1,StoryNumber+1):
            fid.write('\nop.node('+''+str(ii)+''+str(ii-1)+''+'1 ,'+''+str(Pier1)+''+', '+''+str(0.5*StoryH*(2*ii-1))+''+' )')
            fid.write('\nop.node('+''+str(ii)+''+str(ii-1)+''+'2 ,'+''+str(Pier1)+''+', '+''+str(0.5*StoryH*(2*ii-1))+''+' )')
        fid.write('\n')
        
        fid.write('\n# Define boundary conditions')
        fid.write('\nop.fix(10, 1,1,1)')
        fid.write('\n')
        
        for ii in range(1,StoryNumber+1):
            fid.write("\nop.rigidLink('beam', 1"+''+str(ii-1)+''+', '+''+str(ii)+''+str(ii-1)+''+'1)')
            fid.write("\nop.rigidLink('beam', 1"+''+str(ii)+''+', '+''+str(ii)+''+str(ii-1)+''+'2)')
            
    fid.close()

