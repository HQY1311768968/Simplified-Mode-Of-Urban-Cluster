
# This code is for define shear spring material and shear spring elements
 
import openseespy.opensees as op
 
# Load the initial stiffness(SK1) and yield stiffness(SK2) of the shear springs
SK1 = 11376696975.844332
SK2 = 0.25*SK1
 
# Load the yield shear force of the shear spring on each floor
Vy1 = 400736982.6170663
Vy2 = 400736982.6170663
Vy3 = 400736982.6170663
Vy4 = 400736982.6170663
Vy5 = 400736982.6170663
Vy6 = 400736982.6170663
Vy7 = 400736982.6170663
Vy8 = 400736982.6170663
Vy9 = 400736982.6170663
Vy10 = 400736982.6170663
Vy11 = 400736982.6170663
Vy12 = 400736982.6170663
Vy13 = 400736982.6170663
Vy14 = 400736982.6170663
Vy15 = 400736982.6170663
Vy16 = 400736982.6170663
Vy17 = 400736982.6170663
Vy18 = 400736982.6170663
Vy19 = 400736982.6170663
Vy20 = 400736982.6170663
Vy21 = 400736982.6170663
Vy22 = 400736982.6170663
Vy23 = 400736982.6170663
Vy24 = 400736982.6170663
Vy25 = 400736982.6170663
Vy26 = 400736982.6170663
Vy27 = 400736982.6170663
Vy28 = 400736982.6170663
Vy29 = 400736982.6170663
Vy30 = 400736982.6170663
Vy31 = 400736982.6170663
Vy32 = 400736982.6170663
Vy33 = 400736982.6170663
Vy34 = 400736982.6170663
Vy35 = 400736982.6170663
Vy36 = 400736982.6170663
Vy37 = 400736982.6170663
Vy38 = 400736982.6170663
Vy39 = 400736982.6170663
Vy40 = 400736982.6170663
Vy41 = 400736982.6170663
Vy42 = 400736982.6170663
Vy43 = 400736982.6170663
Vy44 = 400736982.6170663
Vy45 = 400736982.6170663
Vy46 = 400736982.6170663
Vy47 = 400736982.6170663
Vy48 = 400736982.6170663
Vy49 = 400736982.6170663
Vy50 = 400736982.6170663
Vy51 = 400736982.6170663
Vy52 = 400736982.6170663
Vy53 = 400736982.6170663
Vy54 = 400736982.6170663
Vy55 = 400736982.6170663
Vy56 = 400736982.6170663
Vy57 = 400736982.6170663
Vy58 = 400736982.6170663
Vy59 = 400736982.6170663
Vy60 = 400736982.6170663
Vy61 = 400736982.6170663
Vy62 = 400736982.6170663
Vy63 = 400736982.6170663
Vy64 = 400736982.6170663
Vy65 = 400736982.6170663
Vy66 = 400736982.6170663
Vy67 = 400736982.6170663
Vy68 = 400736982.6170663
Vy69 = 400736982.6170663
Vy70 = 400736982.6170663
Vy71 = 400736982.6170663
Vy72 = 400736982.6170663
Vy73 = 400736982.6170663
Vy74 = 400736982.6170663
Vy75 = 400736982.6170663
Vy76 = 400736982.6170663
Vy77 = 400736982.6170663
Vy78 = 400736982.6170663
Vy79 = 400736982.6170663
Vy80 = 400736982.6170663
Vy81 = 400736982.6170663
Vy82 = 400736982.6170663
Vy83 = 400736982.6170663
Vy84 = 400736982.6170663
Vy85 = 400736982.6170663
Vy86 = 400736982.6170663
Vy87 = 400736982.6170663
Vy88 = 400736982.6170663
Vy89 = 400736982.6170663
Vy90 = 400736982.6170663
Vy91 = 400736982.6170663
Vy92 = 400736982.6170663
Vy93 = 400736982.6170663
Vy94 = 400736982.6170663
Vy95 = 400736982.6170663
Vy96 = 400736982.6170663
Vy97 = 400736982.6170663
Vy98 = 400736982.6170663
Vy99 = 400736982.6170663
Vy100 = 400736982.6170663
Vy101 = 400736982.6170663
Vy102 = 400736982.6170663
Vy103 = 400736982.6170663
Vy104 = 400736982.6170663
Vy105 = 400736982.6170663
Vy106 = 400736982.6170663
Vy107 = 400736982.6170663
Vy108 = 400736982.6170663
Vy109 = 400736982.6170663
Vy110 = 400736982.6170663
Vy111 = 400736982.6170663
Vy112 = 400736982.6170663
Vy113 = 400736982.6170663
Vy114 = 400736982.6170663
Vy115 = 400736982.6170663
Vy116 = 400736982.6170663
Vy117 = 400736982.6170663
Vy118 = 400736982.6170663
Vy119 = 400736982.6170663
Vy120 = 400736982.6170663
Vy121 = 400736982.6170663
Vy122 = 400736982.6170663
Vy123 = 400736982.6170663
Vy124 = 400736982.6170663
Vy125 = 400736982.6170663
Vy126 = 400736982.6170663
Vy127 = 400736982.6170663
Vy128 = 400736982.6170663
Vy129 = 400736982.6170663
Vy130 = 400736982.6170663
Vy131 = 400736982.6170663
Vy132 = 400736982.6170663
Vy133 = 400736982.6170663
Vy134 = 400736982.6170663
Vy135 = 400736982.6170663
Vy136 = 400736982.6170663
Vy137 = 400736982.6170663
Vy138 = 400736982.6170663
Vy139 = 400736982.6170663
 
# Calculate the yield shear displacements of the shear spring on each floor
uy1 = Vy1/SK1
uy2 = Vy2/SK1
uy3 = Vy3/SK1
uy4 = Vy4/SK1
uy5 = Vy5/SK1
uy6 = Vy6/SK1
uy7 = Vy7/SK1
uy8 = Vy8/SK1
uy9 = Vy9/SK1
uy10 = Vy10/SK1
uy11 = Vy11/SK1
uy12 = Vy12/SK1
uy13 = Vy13/SK1
uy14 = Vy14/SK1
uy15 = Vy15/SK1
uy16 = Vy16/SK1
uy17 = Vy17/SK1
uy18 = Vy18/SK1
uy19 = Vy19/SK1
uy20 = Vy20/SK1
uy21 = Vy21/SK1
uy22 = Vy22/SK1
uy23 = Vy23/SK1
uy24 = Vy24/SK1
uy25 = Vy25/SK1
uy26 = Vy26/SK1
uy27 = Vy27/SK1
uy28 = Vy28/SK1
uy29 = Vy29/SK1
uy30 = Vy30/SK1
uy31 = Vy31/SK1
uy32 = Vy32/SK1
uy33 = Vy33/SK1
uy34 = Vy34/SK1
uy35 = Vy35/SK1
uy36 = Vy36/SK1
uy37 = Vy37/SK1
uy38 = Vy38/SK1
uy39 = Vy39/SK1
uy40 = Vy40/SK1
uy41 = Vy41/SK1
uy42 = Vy42/SK1
uy43 = Vy43/SK1
uy44 = Vy44/SK1
uy45 = Vy45/SK1
uy46 = Vy46/SK1
uy47 = Vy47/SK1
uy48 = Vy48/SK1
uy49 = Vy49/SK1
uy50 = Vy50/SK1
uy51 = Vy51/SK1
uy52 = Vy52/SK1
uy53 = Vy53/SK1
uy54 = Vy54/SK1
uy55 = Vy55/SK1
uy56 = Vy56/SK1
uy57 = Vy57/SK1
uy58 = Vy58/SK1
uy59 = Vy59/SK1
uy60 = Vy60/SK1
uy61 = Vy61/SK1
uy62 = Vy62/SK1
uy63 = Vy63/SK1
uy64 = Vy64/SK1
uy65 = Vy65/SK1
uy66 = Vy66/SK1
uy67 = Vy67/SK1
uy68 = Vy68/SK1
uy69 = Vy69/SK1
uy70 = Vy70/SK1
uy71 = Vy71/SK1
uy72 = Vy72/SK1
uy73 = Vy73/SK1
uy74 = Vy74/SK1
uy75 = Vy75/SK1
uy76 = Vy76/SK1
uy77 = Vy77/SK1
uy78 = Vy78/SK1
uy79 = Vy79/SK1
uy80 = Vy80/SK1
uy81 = Vy81/SK1
uy82 = Vy82/SK1
uy83 = Vy83/SK1
uy84 = Vy84/SK1
uy85 = Vy85/SK1
uy86 = Vy86/SK1
uy87 = Vy87/SK1
uy88 = Vy88/SK1
uy89 = Vy89/SK1
uy90 = Vy90/SK1
uy91 = Vy91/SK1
uy92 = Vy92/SK1
uy93 = Vy93/SK1
uy94 = Vy94/SK1
uy95 = Vy95/SK1
uy96 = Vy96/SK1
uy97 = Vy97/SK1
uy98 = Vy98/SK1
uy99 = Vy99/SK1
uy100 = Vy100/SK1
uy101 = Vy101/SK1
uy102 = Vy102/SK1
uy103 = Vy103/SK1
uy104 = Vy104/SK1
uy105 = Vy105/SK1
uy106 = Vy106/SK1
uy107 = Vy107/SK1
uy108 = Vy108/SK1
uy109 = Vy109/SK1
uy110 = Vy110/SK1
uy111 = Vy111/SK1
uy112 = Vy112/SK1
uy113 = Vy113/SK1
uy114 = Vy114/SK1
uy115 = Vy115/SK1
uy116 = Vy116/SK1
uy117 = Vy117/SK1
uy118 = Vy118/SK1
uy119 = Vy119/SK1
uy120 = Vy120/SK1
uy121 = Vy121/SK1
uy122 = Vy122/SK1
uy123 = Vy123/SK1
uy124 = Vy124/SK1
uy125 = Vy125/SK1
uy126 = Vy126/SK1
uy127 = Vy127/SK1
uy128 = Vy128/SK1
uy129 = Vy129/SK1
uy130 = Vy130/SK1
uy131 = Vy131/SK1
uy132 = Vy132/SK1
uy133 = Vy133/SK1
uy134 = Vy134/SK1
uy135 = Vy135/SK1
uy136 = Vy136/SK1
uy137 = Vy137/SK1
uy138 = Vy138/SK1
uy139 = Vy139/SK1
 
# Calculate the shear force at the peak point of the shear springs
Vp1 = 893643471.2360579
Vp2 = 893643471.2360579
Vp3 = 893643471.2360579
Vp4 = 893643471.2360579
Vp5 = 893643471.2360579
Vp6 = 893643471.2360579
Vp7 = 893643471.2360579
Vp8 = 893643471.2360579
Vp9 = 893643471.2360579
Vp10 = 893643471.2360579
Vp11 = 893643471.2360579
Vp12 = 893643471.2360579
Vp13 = 893643471.2360579
Vp14 = 893643471.2360579
Vp15 = 893643471.2360579
Vp16 = 893643471.2360579
Vp17 = 893643471.2360579
Vp18 = 893643471.2360579
Vp19 = 893643471.2360579
Vp20 = 893643471.2360579
Vp21 = 893643471.2360579
Vp22 = 893643471.2360579
Vp23 = 893643471.2360579
Vp24 = 893643471.2360579
Vp25 = 893643471.2360579
Vp26 = 893643471.2360579
Vp27 = 893643471.2360579
Vp28 = 893643471.2360579
Vp29 = 893643471.2360579
Vp30 = 893643471.2360579
Vp31 = 893643471.2360579
Vp32 = 893643471.2360579
Vp33 = 893643471.2360579
Vp34 = 893643471.2360579
Vp35 = 893643471.2360579
Vp36 = 893643471.2360579
Vp37 = 893643471.2360579
Vp38 = 893643471.2360579
Vp39 = 893643471.2360579
Vp40 = 893643471.2360579
Vp41 = 893643471.2360579
Vp42 = 893643471.2360579
Vp43 = 893643471.2360579
Vp44 = 893643471.2360579
Vp45 = 893643471.2360579
Vp46 = 893643471.2360579
Vp47 = 893643471.2360579
Vp48 = 893643471.2360579
Vp49 = 893643471.2360579
Vp50 = 893643471.2360579
Vp51 = 893643471.2360579
Vp52 = 893643471.2360579
Vp53 = 893643471.2360579
Vp54 = 893643471.2360579
Vp55 = 893643471.2360579
Vp56 = 893643471.2360579
Vp57 = 893643471.2360579
Vp58 = 893643471.2360579
Vp59 = 893643471.2360579
Vp60 = 893643471.2360579
Vp61 = 893643471.2360579
Vp62 = 893643471.2360579
Vp63 = 893643471.2360579
Vp64 = 893643471.2360579
Vp65 = 893643471.2360579
Vp66 = 893643471.2360579
Vp67 = 893643471.2360579
Vp68 = 893643471.2360579
Vp69 = 893643471.2360579
Vp70 = 893643471.2360579
Vp71 = 893643471.2360579
Vp72 = 893643471.2360579
Vp73 = 893643471.2360579
Vp74 = 893643471.2360579
Vp75 = 893643471.2360579
Vp76 = 893643471.2360579
Vp77 = 893643471.2360579
Vp78 = 893643471.2360579
Vp79 = 893643471.2360579
Vp80 = 893643471.2360579
Vp81 = 893643471.2360579
Vp82 = 893643471.2360579
Vp83 = 893643471.2360579
Vp84 = 893643471.2360579
Vp85 = 893643471.2360579
Vp86 = 893643471.2360579
Vp87 = 893643471.2360579
Vp88 = 893643471.2360579
Vp89 = 893643471.2360579
Vp90 = 893643471.2360579
Vp91 = 893643471.2360579
Vp92 = 893643471.2360579
Vp93 = 893643471.2360579
Vp94 = 893643471.2360579
Vp95 = 893643471.2360579
Vp96 = 893643471.2360579
Vp97 = 893643471.2360579
Vp98 = 893643471.2360579
Vp99 = 893643471.2360579
Vp100 = 893643471.2360579
Vp101 = 893643471.2360579
Vp102 = 893643471.2360579
Vp103 = 893643471.2360579
Vp104 = 893643471.2360579
Vp105 = 893643471.2360579
Vp106 = 893643471.2360579
Vp107 = 893643471.2360579
Vp108 = 893643471.2360579
Vp109 = 893643471.2360579
Vp110 = 893643471.2360579
Vp111 = 893643471.2360579
Vp112 = 893643471.2360579
Vp113 = 893643471.2360579
Vp114 = 893643471.2360579
Vp115 = 893643471.2360579
Vp116 = 893643471.2360579
Vp117 = 893643471.2360579
Vp118 = 893643471.2360579
Vp119 = 893643471.2360579
Vp120 = 893643471.2360579
Vp121 = 893643471.2360579
Vp122 = 893643471.2360579
Vp123 = 893643471.2360579
Vp124 = 893643471.2360579
Vp125 = 893643471.2360579
Vp126 = 893643471.2360579
Vp127 = 893643471.2360579
Vp128 = 893643471.2360579
Vp129 = 893643471.2360579
Vp130 = 893643471.2360579
Vp131 = 893643471.2360579
Vp132 = 893643471.2360579
Vp133 = 893643471.2360579
Vp134 = 893643471.2360579
Vp135 = 893643471.2360579
Vp136 = 893643471.2360579
Vp137 = 893643471.2360579
Vp138 = 893643471.2360579
Vp139 = 893643471.2360579
 
# Calculate the displacement of the peak point of the shear springs
up1 = (Vp1-Vy1)/SK2+Vy1/SK1
up2 = (Vp2-Vy2)/SK2+Vy2/SK1
up3 = (Vp3-Vy3)/SK2+Vy3/SK1
up4 = (Vp4-Vy4)/SK2+Vy4/SK1
up5 = (Vp5-Vy5)/SK2+Vy5/SK1
up6 = (Vp6-Vy6)/SK2+Vy6/SK1
up7 = (Vp7-Vy7)/SK2+Vy7/SK1
up8 = (Vp8-Vy8)/SK2+Vy8/SK1
up9 = (Vp9-Vy9)/SK2+Vy9/SK1
up10 = (Vp10-Vy10)/SK2+Vy10/SK1
up11 = (Vp11-Vy11)/SK2+Vy11/SK1
up12 = (Vp12-Vy12)/SK2+Vy12/SK1
up13 = (Vp13-Vy13)/SK2+Vy13/SK1
up14 = (Vp14-Vy14)/SK2+Vy14/SK1
up15 = (Vp15-Vy15)/SK2+Vy15/SK1
up16 = (Vp16-Vy16)/SK2+Vy16/SK1
up17 = (Vp17-Vy17)/SK2+Vy17/SK1
up18 = (Vp18-Vy18)/SK2+Vy18/SK1
up19 = (Vp19-Vy19)/SK2+Vy19/SK1
up20 = (Vp20-Vy20)/SK2+Vy20/SK1
up21 = (Vp21-Vy21)/SK2+Vy21/SK1
up22 = (Vp22-Vy22)/SK2+Vy22/SK1
up23 = (Vp23-Vy23)/SK2+Vy23/SK1
up24 = (Vp24-Vy24)/SK2+Vy24/SK1
up25 = (Vp25-Vy25)/SK2+Vy25/SK1
up26 = (Vp26-Vy26)/SK2+Vy26/SK1
up27 = (Vp27-Vy27)/SK2+Vy27/SK1
up28 = (Vp28-Vy28)/SK2+Vy28/SK1
up29 = (Vp29-Vy29)/SK2+Vy29/SK1
up30 = (Vp30-Vy30)/SK2+Vy30/SK1
up31 = (Vp31-Vy31)/SK2+Vy31/SK1
up32 = (Vp32-Vy32)/SK2+Vy32/SK1
up33 = (Vp33-Vy33)/SK2+Vy33/SK1
up34 = (Vp34-Vy34)/SK2+Vy34/SK1
up35 = (Vp35-Vy35)/SK2+Vy35/SK1
up36 = (Vp36-Vy36)/SK2+Vy36/SK1
up37 = (Vp37-Vy37)/SK2+Vy37/SK1
up38 = (Vp38-Vy38)/SK2+Vy38/SK1
up39 = (Vp39-Vy39)/SK2+Vy39/SK1
up40 = (Vp40-Vy40)/SK2+Vy40/SK1
up41 = (Vp41-Vy41)/SK2+Vy41/SK1
up42 = (Vp42-Vy42)/SK2+Vy42/SK1
up43 = (Vp43-Vy43)/SK2+Vy43/SK1
up44 = (Vp44-Vy44)/SK2+Vy44/SK1
up45 = (Vp45-Vy45)/SK2+Vy45/SK1
up46 = (Vp46-Vy46)/SK2+Vy46/SK1
up47 = (Vp47-Vy47)/SK2+Vy47/SK1
up48 = (Vp48-Vy48)/SK2+Vy48/SK1
up49 = (Vp49-Vy49)/SK2+Vy49/SK1
up50 = (Vp50-Vy50)/SK2+Vy50/SK1
up51 = (Vp51-Vy51)/SK2+Vy51/SK1
up52 = (Vp52-Vy52)/SK2+Vy52/SK1
up53 = (Vp53-Vy53)/SK2+Vy53/SK1
up54 = (Vp54-Vy54)/SK2+Vy54/SK1
up55 = (Vp55-Vy55)/SK2+Vy55/SK1
up56 = (Vp56-Vy56)/SK2+Vy56/SK1
up57 = (Vp57-Vy57)/SK2+Vy57/SK1
up58 = (Vp58-Vy58)/SK2+Vy58/SK1
up59 = (Vp59-Vy59)/SK2+Vy59/SK1
up60 = (Vp60-Vy60)/SK2+Vy60/SK1
up61 = (Vp61-Vy61)/SK2+Vy61/SK1
up62 = (Vp62-Vy62)/SK2+Vy62/SK1
up63 = (Vp63-Vy63)/SK2+Vy63/SK1
up64 = (Vp64-Vy64)/SK2+Vy64/SK1
up65 = (Vp65-Vy65)/SK2+Vy65/SK1
up66 = (Vp66-Vy66)/SK2+Vy66/SK1
up67 = (Vp67-Vy67)/SK2+Vy67/SK1
up68 = (Vp68-Vy68)/SK2+Vy68/SK1
up69 = (Vp69-Vy69)/SK2+Vy69/SK1
up70 = (Vp70-Vy70)/SK2+Vy70/SK1
up71 = (Vp71-Vy71)/SK2+Vy71/SK1
up72 = (Vp72-Vy72)/SK2+Vy72/SK1
up73 = (Vp73-Vy73)/SK2+Vy73/SK1
up74 = (Vp74-Vy74)/SK2+Vy74/SK1
up75 = (Vp75-Vy75)/SK2+Vy75/SK1
up76 = (Vp76-Vy76)/SK2+Vy76/SK1
up77 = (Vp77-Vy77)/SK2+Vy77/SK1
up78 = (Vp78-Vy78)/SK2+Vy78/SK1
up79 = (Vp79-Vy79)/SK2+Vy79/SK1
up80 = (Vp80-Vy80)/SK2+Vy80/SK1
up81 = (Vp81-Vy81)/SK2+Vy81/SK1
up82 = (Vp82-Vy82)/SK2+Vy82/SK1
up83 = (Vp83-Vy83)/SK2+Vy83/SK1
up84 = (Vp84-Vy84)/SK2+Vy84/SK1
up85 = (Vp85-Vy85)/SK2+Vy85/SK1
up86 = (Vp86-Vy86)/SK2+Vy86/SK1
up87 = (Vp87-Vy87)/SK2+Vy87/SK1
up88 = (Vp88-Vy88)/SK2+Vy88/SK1
up89 = (Vp89-Vy89)/SK2+Vy89/SK1
up90 = (Vp90-Vy90)/SK2+Vy90/SK1
up91 = (Vp91-Vy91)/SK2+Vy91/SK1
up92 = (Vp92-Vy92)/SK2+Vy92/SK1
up93 = (Vp93-Vy93)/SK2+Vy93/SK1
up94 = (Vp94-Vy94)/SK2+Vy94/SK1
up95 = (Vp95-Vy95)/SK2+Vy95/SK1
up96 = (Vp96-Vy96)/SK2+Vy96/SK1
up97 = (Vp97-Vy97)/SK2+Vy97/SK1
up98 = (Vp98-Vy98)/SK2+Vy98/SK1
up99 = (Vp99-Vy99)/SK2+Vy99/SK1
up100 = (Vp100-Vy100)/SK2+Vy100/SK1
up101 = (Vp101-Vy101)/SK2+Vy101/SK1
up102 = (Vp102-Vy102)/SK2+Vy102/SK1
up103 = (Vp103-Vy103)/SK2+Vy103/SK1
up104 = (Vp104-Vy104)/SK2+Vy104/SK1
up105 = (Vp105-Vy105)/SK2+Vy105/SK1
up106 = (Vp106-Vy106)/SK2+Vy106/SK1
up107 = (Vp107-Vy107)/SK2+Vy107/SK1
up108 = (Vp108-Vy108)/SK2+Vy108/SK1
up109 = (Vp109-Vy109)/SK2+Vy109/SK1
up110 = (Vp110-Vy110)/SK2+Vy110/SK1
up111 = (Vp111-Vy111)/SK2+Vy111/SK1
up112 = (Vp112-Vy112)/SK2+Vy112/SK1
up113 = (Vp113-Vy113)/SK2+Vy113/SK1
up114 = (Vp114-Vy114)/SK2+Vy114/SK1
up115 = (Vp115-Vy115)/SK2+Vy115/SK1
up116 = (Vp116-Vy116)/SK2+Vy116/SK1
up117 = (Vp117-Vy117)/SK2+Vy117/SK1
up118 = (Vp118-Vy118)/SK2+Vy118/SK1
up119 = (Vp119-Vy119)/SK2+Vy119/SK1
up120 = (Vp120-Vy120)/SK2+Vy120/SK1
up121 = (Vp121-Vy121)/SK2+Vy121/SK1
up122 = (Vp122-Vy122)/SK2+Vy122/SK1
up123 = (Vp123-Vy123)/SK2+Vy123/SK1
up124 = (Vp124-Vy124)/SK2+Vy124/SK1
up125 = (Vp125-Vy125)/SK2+Vy125/SK1
up126 = (Vp126-Vy126)/SK2+Vy126/SK1
up127 = (Vp127-Vy127)/SK2+Vy127/SK1
up128 = (Vp128-Vy128)/SK2+Vy128/SK1
up129 = (Vp129-Vy129)/SK2+Vy129/SK1
up130 = (Vp130-Vy130)/SK2+Vy130/SK1
up131 = (Vp131-Vy131)/SK2+Vy131/SK1
up132 = (Vp132-Vy132)/SK2+Vy132/SK1
up133 = (Vp133-Vy133)/SK2+Vy133/SK1
up134 = (Vp134-Vy134)/SK2+Vy134/SK1
up135 = (Vp135-Vy135)/SK2+Vy135/SK1
up136 = (Vp136-Vy136)/SK2+Vy136/SK1
up137 = (Vp137-Vy137)/SK2+Vy137/SK1
up138 = (Vp138-Vy138)/SK2+Vy138/SK1
up139 = (Vp139-Vy139)/SK2+Vy139/SK1
 
# Define shear spring material
tenup1 = 10*up1
Vy1ne  = -1*Vy1
uy1ne  = -1*uy1
Vp1ne  = -1*Vp1
up1ne  = -1*up1
Vp1ne  = -1*Vp1
tenup1ne = -1*tenup1
op.uniaxialMaterial('Hysteretic', 1, Vy1, uy1, Vp1, up1, Vp1, tenup1, Vy1ne, uy1ne, Vp1ne, up1ne, Vp1ne, tenup1ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup2 = 10*up2
Vy2ne  = -1*Vy2
uy2ne  = -1*uy2
Vp2ne  = -1*Vp2
up2ne  = -1*up2
Vp2ne  = -1*Vp2
tenup2ne = -1*tenup2
op.uniaxialMaterial('Hysteretic', 2, Vy2, uy2, Vp2, up2, Vp2, tenup2, Vy2ne, uy2ne, Vp2ne, up2ne, Vp2ne, tenup2ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup3 = 10*up3
Vy3ne  = -1*Vy3
uy3ne  = -1*uy3
Vp3ne  = -1*Vp3
up3ne  = -1*up3
Vp3ne  = -1*Vp3
tenup3ne = -1*tenup3
op.uniaxialMaterial('Hysteretic', 3, Vy3, uy3, Vp3, up3, Vp3, tenup3, Vy3ne, uy3ne, Vp3ne, up3ne, Vp3ne, tenup3ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup4 = 10*up4
Vy4ne  = -1*Vy4
uy4ne  = -1*uy4
Vp4ne  = -1*Vp4
up4ne  = -1*up4
Vp4ne  = -1*Vp4
tenup4ne = -1*tenup4
op.uniaxialMaterial('Hysteretic', 4, Vy4, uy4, Vp4, up4, Vp4, tenup4, Vy4ne, uy4ne, Vp4ne, up4ne, Vp4ne, tenup4ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup5 = 10*up5
Vy5ne  = -1*Vy5
uy5ne  = -1*uy5
Vp5ne  = -1*Vp5
up5ne  = -1*up5
Vp5ne  = -1*Vp5
tenup5ne = -1*tenup5
op.uniaxialMaterial('Hysteretic', 5, Vy5, uy5, Vp5, up5, Vp5, tenup5, Vy5ne, uy5ne, Vp5ne, up5ne, Vp5ne, tenup5ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup6 = 10*up6
Vy6ne  = -1*Vy6
uy6ne  = -1*uy6
Vp6ne  = -1*Vp6
up6ne  = -1*up6
Vp6ne  = -1*Vp6
tenup6ne = -1*tenup6
op.uniaxialMaterial('Hysteretic', 6, Vy6, uy6, Vp6, up6, Vp6, tenup6, Vy6ne, uy6ne, Vp6ne, up6ne, Vp6ne, tenup6ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup7 = 10*up7
Vy7ne  = -1*Vy7
uy7ne  = -1*uy7
Vp7ne  = -1*Vp7
up7ne  = -1*up7
Vp7ne  = -1*Vp7
tenup7ne = -1*tenup7
op.uniaxialMaterial('Hysteretic', 7, Vy7, uy7, Vp7, up7, Vp7, tenup7, Vy7ne, uy7ne, Vp7ne, up7ne, Vp7ne, tenup7ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup8 = 10*up8
Vy8ne  = -1*Vy8
uy8ne  = -1*uy8
Vp8ne  = -1*Vp8
up8ne  = -1*up8
Vp8ne  = -1*Vp8
tenup8ne = -1*tenup8
op.uniaxialMaterial('Hysteretic', 8, Vy8, uy8, Vp8, up8, Vp8, tenup8, Vy8ne, uy8ne, Vp8ne, up8ne, Vp8ne, tenup8ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup9 = 10*up9
Vy9ne  = -1*Vy9
uy9ne  = -1*uy9
Vp9ne  = -1*Vp9
up9ne  = -1*up9
Vp9ne  = -1*Vp9
tenup9ne = -1*tenup9
op.uniaxialMaterial('Hysteretic', 9, Vy9, uy9, Vp9, up9, Vp9, tenup9, Vy9ne, uy9ne, Vp9ne, up9ne, Vp9ne, tenup9ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup10 = 10*up10
Vy10ne  = -1*Vy10
uy10ne  = -1*uy10
Vp10ne  = -1*Vp10
up10ne  = -1*up10
Vp10ne  = -1*Vp10
tenup10ne = -1*tenup10
op.uniaxialMaterial('Hysteretic', 10, Vy10, uy10, Vp10, up10, Vp10, tenup10, Vy10ne, uy10ne, Vp10ne, up10ne, Vp10ne, tenup10ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup11 = 10*up11
Vy11ne  = -1*Vy11
uy11ne  = -1*uy11
Vp11ne  = -1*Vp11
up11ne  = -1*up11
Vp11ne  = -1*Vp11
tenup11ne = -1*tenup11
op.uniaxialMaterial('Hysteretic', 11, Vy11, uy11, Vp11, up11, Vp11, tenup11, Vy11ne, uy11ne, Vp11ne, up11ne, Vp11ne, tenup11ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup12 = 10*up12
Vy12ne  = -1*Vy12
uy12ne  = -1*uy12
Vp12ne  = -1*Vp12
up12ne  = -1*up12
Vp12ne  = -1*Vp12
tenup12ne = -1*tenup12
op.uniaxialMaterial('Hysteretic', 12, Vy12, uy12, Vp12, up12, Vp12, tenup12, Vy12ne, uy12ne, Vp12ne, up12ne, Vp12ne, tenup12ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup13 = 10*up13
Vy13ne  = -1*Vy13
uy13ne  = -1*uy13
Vp13ne  = -1*Vp13
up13ne  = -1*up13
Vp13ne  = -1*Vp13
tenup13ne = -1*tenup13
op.uniaxialMaterial('Hysteretic', 13, Vy13, uy13, Vp13, up13, Vp13, tenup13, Vy13ne, uy13ne, Vp13ne, up13ne, Vp13ne, tenup13ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup14 = 10*up14
Vy14ne  = -1*Vy14
uy14ne  = -1*uy14
Vp14ne  = -1*Vp14
up14ne  = -1*up14
Vp14ne  = -1*Vp14
tenup14ne = -1*tenup14
op.uniaxialMaterial('Hysteretic', 14, Vy14, uy14, Vp14, up14, Vp14, tenup14, Vy14ne, uy14ne, Vp14ne, up14ne, Vp14ne, tenup14ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup15 = 10*up15
Vy15ne  = -1*Vy15
uy15ne  = -1*uy15
Vp15ne  = -1*Vp15
up15ne  = -1*up15
Vp15ne  = -1*Vp15
tenup15ne = -1*tenup15
op.uniaxialMaterial('Hysteretic', 15, Vy15, uy15, Vp15, up15, Vp15, tenup15, Vy15ne, uy15ne, Vp15ne, up15ne, Vp15ne, tenup15ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup16 = 10*up16
Vy16ne  = -1*Vy16
uy16ne  = -1*uy16
Vp16ne  = -1*Vp16
up16ne  = -1*up16
Vp16ne  = -1*Vp16
tenup16ne = -1*tenup16
op.uniaxialMaterial('Hysteretic', 16, Vy16, uy16, Vp16, up16, Vp16, tenup16, Vy16ne, uy16ne, Vp16ne, up16ne, Vp16ne, tenup16ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup17 = 10*up17
Vy17ne  = -1*Vy17
uy17ne  = -1*uy17
Vp17ne  = -1*Vp17
up17ne  = -1*up17
Vp17ne  = -1*Vp17
tenup17ne = -1*tenup17
op.uniaxialMaterial('Hysteretic', 17, Vy17, uy17, Vp17, up17, Vp17, tenup17, Vy17ne, uy17ne, Vp17ne, up17ne, Vp17ne, tenup17ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup18 = 10*up18
Vy18ne  = -1*Vy18
uy18ne  = -1*uy18
Vp18ne  = -1*Vp18
up18ne  = -1*up18
Vp18ne  = -1*Vp18
tenup18ne = -1*tenup18
op.uniaxialMaterial('Hysteretic', 18, Vy18, uy18, Vp18, up18, Vp18, tenup18, Vy18ne, uy18ne, Vp18ne, up18ne, Vp18ne, tenup18ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup19 = 10*up19
Vy19ne  = -1*Vy19
uy19ne  = -1*uy19
Vp19ne  = -1*Vp19
up19ne  = -1*up19
Vp19ne  = -1*Vp19
tenup19ne = -1*tenup19
op.uniaxialMaterial('Hysteretic', 19, Vy19, uy19, Vp19, up19, Vp19, tenup19, Vy19ne, uy19ne, Vp19ne, up19ne, Vp19ne, tenup19ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup20 = 10*up20
Vy20ne  = -1*Vy20
uy20ne  = -1*uy20
Vp20ne  = -1*Vp20
up20ne  = -1*up20
Vp20ne  = -1*Vp20
tenup20ne = -1*tenup20
op.uniaxialMaterial('Hysteretic', 20, Vy20, uy20, Vp20, up20, Vp20, tenup20, Vy20ne, uy20ne, Vp20ne, up20ne, Vp20ne, tenup20ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup21 = 10*up21
Vy21ne  = -1*Vy21
uy21ne  = -1*uy21
Vp21ne  = -1*Vp21
up21ne  = -1*up21
Vp21ne  = -1*Vp21
tenup21ne = -1*tenup21
op.uniaxialMaterial('Hysteretic', 21, Vy21, uy21, Vp21, up21, Vp21, tenup21, Vy21ne, uy21ne, Vp21ne, up21ne, Vp21ne, tenup21ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup22 = 10*up22
Vy22ne  = -1*Vy22
uy22ne  = -1*uy22
Vp22ne  = -1*Vp22
up22ne  = -1*up22
Vp22ne  = -1*Vp22
tenup22ne = -1*tenup22
op.uniaxialMaterial('Hysteretic', 22, Vy22, uy22, Vp22, up22, Vp22, tenup22, Vy22ne, uy22ne, Vp22ne, up22ne, Vp22ne, tenup22ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup23 = 10*up23
Vy23ne  = -1*Vy23
uy23ne  = -1*uy23
Vp23ne  = -1*Vp23
up23ne  = -1*up23
Vp23ne  = -1*Vp23
tenup23ne = -1*tenup23
op.uniaxialMaterial('Hysteretic', 23, Vy23, uy23, Vp23, up23, Vp23, tenup23, Vy23ne, uy23ne, Vp23ne, up23ne, Vp23ne, tenup23ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup24 = 10*up24
Vy24ne  = -1*Vy24
uy24ne  = -1*uy24
Vp24ne  = -1*Vp24
up24ne  = -1*up24
Vp24ne  = -1*Vp24
tenup24ne = -1*tenup24
op.uniaxialMaterial('Hysteretic', 24, Vy24, uy24, Vp24, up24, Vp24, tenup24, Vy24ne, uy24ne, Vp24ne, up24ne, Vp24ne, tenup24ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup25 = 10*up25
Vy25ne  = -1*Vy25
uy25ne  = -1*uy25
Vp25ne  = -1*Vp25
up25ne  = -1*up25
Vp25ne  = -1*Vp25
tenup25ne = -1*tenup25
op.uniaxialMaterial('Hysteretic', 25, Vy25, uy25, Vp25, up25, Vp25, tenup25, Vy25ne, uy25ne, Vp25ne, up25ne, Vp25ne, tenup25ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup26 = 10*up26
Vy26ne  = -1*Vy26
uy26ne  = -1*uy26
Vp26ne  = -1*Vp26
up26ne  = -1*up26
Vp26ne  = -1*Vp26
tenup26ne = -1*tenup26
op.uniaxialMaterial('Hysteretic', 26, Vy26, uy26, Vp26, up26, Vp26, tenup26, Vy26ne, uy26ne, Vp26ne, up26ne, Vp26ne, tenup26ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup27 = 10*up27
Vy27ne  = -1*Vy27
uy27ne  = -1*uy27
Vp27ne  = -1*Vp27
up27ne  = -1*up27
Vp27ne  = -1*Vp27
tenup27ne = -1*tenup27
op.uniaxialMaterial('Hysteretic', 27, Vy27, uy27, Vp27, up27, Vp27, tenup27, Vy27ne, uy27ne, Vp27ne, up27ne, Vp27ne, tenup27ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup28 = 10*up28
Vy28ne  = -1*Vy28
uy28ne  = -1*uy28
Vp28ne  = -1*Vp28
up28ne  = -1*up28
Vp28ne  = -1*Vp28
tenup28ne = -1*tenup28
op.uniaxialMaterial('Hysteretic', 28, Vy28, uy28, Vp28, up28, Vp28, tenup28, Vy28ne, uy28ne, Vp28ne, up28ne, Vp28ne, tenup28ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup29 = 10*up29
Vy29ne  = -1*Vy29
uy29ne  = -1*uy29
Vp29ne  = -1*Vp29
up29ne  = -1*up29
Vp29ne  = -1*Vp29
tenup29ne = -1*tenup29
op.uniaxialMaterial('Hysteretic', 29, Vy29, uy29, Vp29, up29, Vp29, tenup29, Vy29ne, uy29ne, Vp29ne, up29ne, Vp29ne, tenup29ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup30 = 10*up30
Vy30ne  = -1*Vy30
uy30ne  = -1*uy30
Vp30ne  = -1*Vp30
up30ne  = -1*up30
Vp30ne  = -1*Vp30
tenup30ne = -1*tenup30
op.uniaxialMaterial('Hysteretic', 30, Vy30, uy30, Vp30, up30, Vp30, tenup30, Vy30ne, uy30ne, Vp30ne, up30ne, Vp30ne, tenup30ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup31 = 10*up31
Vy31ne  = -1*Vy31
uy31ne  = -1*uy31
Vp31ne  = -1*Vp31
up31ne  = -1*up31
Vp31ne  = -1*Vp31
tenup31ne = -1*tenup31
op.uniaxialMaterial('Hysteretic', 31, Vy31, uy31, Vp31, up31, Vp31, tenup31, Vy31ne, uy31ne, Vp31ne, up31ne, Vp31ne, tenup31ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup32 = 10*up32
Vy32ne  = -1*Vy32
uy32ne  = -1*uy32
Vp32ne  = -1*Vp32
up32ne  = -1*up32
Vp32ne  = -1*Vp32
tenup32ne = -1*tenup32
op.uniaxialMaterial('Hysteretic', 32, Vy32, uy32, Vp32, up32, Vp32, tenup32, Vy32ne, uy32ne, Vp32ne, up32ne, Vp32ne, tenup32ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup33 = 10*up33
Vy33ne  = -1*Vy33
uy33ne  = -1*uy33
Vp33ne  = -1*Vp33
up33ne  = -1*up33
Vp33ne  = -1*Vp33
tenup33ne = -1*tenup33
op.uniaxialMaterial('Hysteretic', 33, Vy33, uy33, Vp33, up33, Vp33, tenup33, Vy33ne, uy33ne, Vp33ne, up33ne, Vp33ne, tenup33ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup34 = 10*up34
Vy34ne  = -1*Vy34
uy34ne  = -1*uy34
Vp34ne  = -1*Vp34
up34ne  = -1*up34
Vp34ne  = -1*Vp34
tenup34ne = -1*tenup34
op.uniaxialMaterial('Hysteretic', 34, Vy34, uy34, Vp34, up34, Vp34, tenup34, Vy34ne, uy34ne, Vp34ne, up34ne, Vp34ne, tenup34ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup35 = 10*up35
Vy35ne  = -1*Vy35
uy35ne  = -1*uy35
Vp35ne  = -1*Vp35
up35ne  = -1*up35
Vp35ne  = -1*Vp35
tenup35ne = -1*tenup35
op.uniaxialMaterial('Hysteretic', 35, Vy35, uy35, Vp35, up35, Vp35, tenup35, Vy35ne, uy35ne, Vp35ne, up35ne, Vp35ne, tenup35ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup36 = 10*up36
Vy36ne  = -1*Vy36
uy36ne  = -1*uy36
Vp36ne  = -1*Vp36
up36ne  = -1*up36
Vp36ne  = -1*Vp36
tenup36ne = -1*tenup36
op.uniaxialMaterial('Hysteretic', 36, Vy36, uy36, Vp36, up36, Vp36, tenup36, Vy36ne, uy36ne, Vp36ne, up36ne, Vp36ne, tenup36ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup37 = 10*up37
Vy37ne  = -1*Vy37
uy37ne  = -1*uy37
Vp37ne  = -1*Vp37
up37ne  = -1*up37
Vp37ne  = -1*Vp37
tenup37ne = -1*tenup37
op.uniaxialMaterial('Hysteretic', 37, Vy37, uy37, Vp37, up37, Vp37, tenup37, Vy37ne, uy37ne, Vp37ne, up37ne, Vp37ne, tenup37ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup38 = 10*up38
Vy38ne  = -1*Vy38
uy38ne  = -1*uy38
Vp38ne  = -1*Vp38
up38ne  = -1*up38
Vp38ne  = -1*Vp38
tenup38ne = -1*tenup38
op.uniaxialMaterial('Hysteretic', 38, Vy38, uy38, Vp38, up38, Vp38, tenup38, Vy38ne, uy38ne, Vp38ne, up38ne, Vp38ne, tenup38ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup39 = 10*up39
Vy39ne  = -1*Vy39
uy39ne  = -1*uy39
Vp39ne  = -1*Vp39
up39ne  = -1*up39
Vp39ne  = -1*Vp39
tenup39ne = -1*tenup39
op.uniaxialMaterial('Hysteretic', 39, Vy39, uy39, Vp39, up39, Vp39, tenup39, Vy39ne, uy39ne, Vp39ne, up39ne, Vp39ne, tenup39ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup40 = 10*up40
Vy40ne  = -1*Vy40
uy40ne  = -1*uy40
Vp40ne  = -1*Vp40
up40ne  = -1*up40
Vp40ne  = -1*Vp40
tenup40ne = -1*tenup40
op.uniaxialMaterial('Hysteretic', 40, Vy40, uy40, Vp40, up40, Vp40, tenup40, Vy40ne, uy40ne, Vp40ne, up40ne, Vp40ne, tenup40ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup41 = 10*up41
Vy41ne  = -1*Vy41
uy41ne  = -1*uy41
Vp41ne  = -1*Vp41
up41ne  = -1*up41
Vp41ne  = -1*Vp41
tenup41ne = -1*tenup41
op.uniaxialMaterial('Hysteretic', 41, Vy41, uy41, Vp41, up41, Vp41, tenup41, Vy41ne, uy41ne, Vp41ne, up41ne, Vp41ne, tenup41ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup42 = 10*up42
Vy42ne  = -1*Vy42
uy42ne  = -1*uy42
Vp42ne  = -1*Vp42
up42ne  = -1*up42
Vp42ne  = -1*Vp42
tenup42ne = -1*tenup42
op.uniaxialMaterial('Hysteretic', 42, Vy42, uy42, Vp42, up42, Vp42, tenup42, Vy42ne, uy42ne, Vp42ne, up42ne, Vp42ne, tenup42ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup43 = 10*up43
Vy43ne  = -1*Vy43
uy43ne  = -1*uy43
Vp43ne  = -1*Vp43
up43ne  = -1*up43
Vp43ne  = -1*Vp43
tenup43ne = -1*tenup43
op.uniaxialMaterial('Hysteretic', 43, Vy43, uy43, Vp43, up43, Vp43, tenup43, Vy43ne, uy43ne, Vp43ne, up43ne, Vp43ne, tenup43ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup44 = 10*up44
Vy44ne  = -1*Vy44
uy44ne  = -1*uy44
Vp44ne  = -1*Vp44
up44ne  = -1*up44
Vp44ne  = -1*Vp44
tenup44ne = -1*tenup44
op.uniaxialMaterial('Hysteretic', 44, Vy44, uy44, Vp44, up44, Vp44, tenup44, Vy44ne, uy44ne, Vp44ne, up44ne, Vp44ne, tenup44ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup45 = 10*up45
Vy45ne  = -1*Vy45
uy45ne  = -1*uy45
Vp45ne  = -1*Vp45
up45ne  = -1*up45
Vp45ne  = -1*Vp45
tenup45ne = -1*tenup45
op.uniaxialMaterial('Hysteretic', 45, Vy45, uy45, Vp45, up45, Vp45, tenup45, Vy45ne, uy45ne, Vp45ne, up45ne, Vp45ne, tenup45ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup46 = 10*up46
Vy46ne  = -1*Vy46
uy46ne  = -1*uy46
Vp46ne  = -1*Vp46
up46ne  = -1*up46
Vp46ne  = -1*Vp46
tenup46ne = -1*tenup46
op.uniaxialMaterial('Hysteretic', 46, Vy46, uy46, Vp46, up46, Vp46, tenup46, Vy46ne, uy46ne, Vp46ne, up46ne, Vp46ne, tenup46ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup47 = 10*up47
Vy47ne  = -1*Vy47
uy47ne  = -1*uy47
Vp47ne  = -1*Vp47
up47ne  = -1*up47
Vp47ne  = -1*Vp47
tenup47ne = -1*tenup47
op.uniaxialMaterial('Hysteretic', 47, Vy47, uy47, Vp47, up47, Vp47, tenup47, Vy47ne, uy47ne, Vp47ne, up47ne, Vp47ne, tenup47ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup48 = 10*up48
Vy48ne  = -1*Vy48
uy48ne  = -1*uy48
Vp48ne  = -1*Vp48
up48ne  = -1*up48
Vp48ne  = -1*Vp48
tenup48ne = -1*tenup48
op.uniaxialMaterial('Hysteretic', 48, Vy48, uy48, Vp48, up48, Vp48, tenup48, Vy48ne, uy48ne, Vp48ne, up48ne, Vp48ne, tenup48ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup49 = 10*up49
Vy49ne  = -1*Vy49
uy49ne  = -1*uy49
Vp49ne  = -1*Vp49
up49ne  = -1*up49
Vp49ne  = -1*Vp49
tenup49ne = -1*tenup49
op.uniaxialMaterial('Hysteretic', 49, Vy49, uy49, Vp49, up49, Vp49, tenup49, Vy49ne, uy49ne, Vp49ne, up49ne, Vp49ne, tenup49ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup50 = 10*up50
Vy50ne  = -1*Vy50
uy50ne  = -1*uy50
Vp50ne  = -1*Vp50
up50ne  = -1*up50
Vp50ne  = -1*Vp50
tenup50ne = -1*tenup50
op.uniaxialMaterial('Hysteretic', 50, Vy50, uy50, Vp50, up50, Vp50, tenup50, Vy50ne, uy50ne, Vp50ne, up50ne, Vp50ne, tenup50ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup51 = 10*up51
Vy51ne  = -1*Vy51
uy51ne  = -1*uy51
Vp51ne  = -1*Vp51
up51ne  = -1*up51
Vp51ne  = -1*Vp51
tenup51ne = -1*tenup51
op.uniaxialMaterial('Hysteretic', 51, Vy51, uy51, Vp51, up51, Vp51, tenup51, Vy51ne, uy51ne, Vp51ne, up51ne, Vp51ne, tenup51ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup52 = 10*up52
Vy52ne  = -1*Vy52
uy52ne  = -1*uy52
Vp52ne  = -1*Vp52
up52ne  = -1*up52
Vp52ne  = -1*Vp52
tenup52ne = -1*tenup52
op.uniaxialMaterial('Hysteretic', 52, Vy52, uy52, Vp52, up52, Vp52, tenup52, Vy52ne, uy52ne, Vp52ne, up52ne, Vp52ne, tenup52ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup53 = 10*up53
Vy53ne  = -1*Vy53
uy53ne  = -1*uy53
Vp53ne  = -1*Vp53
up53ne  = -1*up53
Vp53ne  = -1*Vp53
tenup53ne = -1*tenup53
op.uniaxialMaterial('Hysteretic', 53, Vy53, uy53, Vp53, up53, Vp53, tenup53, Vy53ne, uy53ne, Vp53ne, up53ne, Vp53ne, tenup53ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup54 = 10*up54
Vy54ne  = -1*Vy54
uy54ne  = -1*uy54
Vp54ne  = -1*Vp54
up54ne  = -1*up54
Vp54ne  = -1*Vp54
tenup54ne = -1*tenup54
op.uniaxialMaterial('Hysteretic', 54, Vy54, uy54, Vp54, up54, Vp54, tenup54, Vy54ne, uy54ne, Vp54ne, up54ne, Vp54ne, tenup54ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup55 = 10*up55
Vy55ne  = -1*Vy55
uy55ne  = -1*uy55
Vp55ne  = -1*Vp55
up55ne  = -1*up55
Vp55ne  = -1*Vp55
tenup55ne = -1*tenup55
op.uniaxialMaterial('Hysteretic', 55, Vy55, uy55, Vp55, up55, Vp55, tenup55, Vy55ne, uy55ne, Vp55ne, up55ne, Vp55ne, tenup55ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup56 = 10*up56
Vy56ne  = -1*Vy56
uy56ne  = -1*uy56
Vp56ne  = -1*Vp56
up56ne  = -1*up56
Vp56ne  = -1*Vp56
tenup56ne = -1*tenup56
op.uniaxialMaterial('Hysteretic', 56, Vy56, uy56, Vp56, up56, Vp56, tenup56, Vy56ne, uy56ne, Vp56ne, up56ne, Vp56ne, tenup56ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup57 = 10*up57
Vy57ne  = -1*Vy57
uy57ne  = -1*uy57
Vp57ne  = -1*Vp57
up57ne  = -1*up57
Vp57ne  = -1*Vp57
tenup57ne = -1*tenup57
op.uniaxialMaterial('Hysteretic', 57, Vy57, uy57, Vp57, up57, Vp57, tenup57, Vy57ne, uy57ne, Vp57ne, up57ne, Vp57ne, tenup57ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup58 = 10*up58
Vy58ne  = -1*Vy58
uy58ne  = -1*uy58
Vp58ne  = -1*Vp58
up58ne  = -1*up58
Vp58ne  = -1*Vp58
tenup58ne = -1*tenup58
op.uniaxialMaterial('Hysteretic', 58, Vy58, uy58, Vp58, up58, Vp58, tenup58, Vy58ne, uy58ne, Vp58ne, up58ne, Vp58ne, tenup58ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup59 = 10*up59
Vy59ne  = -1*Vy59
uy59ne  = -1*uy59
Vp59ne  = -1*Vp59
up59ne  = -1*up59
Vp59ne  = -1*Vp59
tenup59ne = -1*tenup59
op.uniaxialMaterial('Hysteretic', 59, Vy59, uy59, Vp59, up59, Vp59, tenup59, Vy59ne, uy59ne, Vp59ne, up59ne, Vp59ne, tenup59ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup60 = 10*up60
Vy60ne  = -1*Vy60
uy60ne  = -1*uy60
Vp60ne  = -1*Vp60
up60ne  = -1*up60
Vp60ne  = -1*Vp60
tenup60ne = -1*tenup60
op.uniaxialMaterial('Hysteretic', 60, Vy60, uy60, Vp60, up60, Vp60, tenup60, Vy60ne, uy60ne, Vp60ne, up60ne, Vp60ne, tenup60ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup61 = 10*up61
Vy61ne  = -1*Vy61
uy61ne  = -1*uy61
Vp61ne  = -1*Vp61
up61ne  = -1*up61
Vp61ne  = -1*Vp61
tenup61ne = -1*tenup61
op.uniaxialMaterial('Hysteretic', 61, Vy61, uy61, Vp61, up61, Vp61, tenup61, Vy61ne, uy61ne, Vp61ne, up61ne, Vp61ne, tenup61ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup62 = 10*up62
Vy62ne  = -1*Vy62
uy62ne  = -1*uy62
Vp62ne  = -1*Vp62
up62ne  = -1*up62
Vp62ne  = -1*Vp62
tenup62ne = -1*tenup62
op.uniaxialMaterial('Hysteretic', 62, Vy62, uy62, Vp62, up62, Vp62, tenup62, Vy62ne, uy62ne, Vp62ne, up62ne, Vp62ne, tenup62ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup63 = 10*up63
Vy63ne  = -1*Vy63
uy63ne  = -1*uy63
Vp63ne  = -1*Vp63
up63ne  = -1*up63
Vp63ne  = -1*Vp63
tenup63ne = -1*tenup63
op.uniaxialMaterial('Hysteretic', 63, Vy63, uy63, Vp63, up63, Vp63, tenup63, Vy63ne, uy63ne, Vp63ne, up63ne, Vp63ne, tenup63ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup64 = 10*up64
Vy64ne  = -1*Vy64
uy64ne  = -1*uy64
Vp64ne  = -1*Vp64
up64ne  = -1*up64
Vp64ne  = -1*Vp64
tenup64ne = -1*tenup64
op.uniaxialMaterial('Hysteretic', 64, Vy64, uy64, Vp64, up64, Vp64, tenup64, Vy64ne, uy64ne, Vp64ne, up64ne, Vp64ne, tenup64ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup65 = 10*up65
Vy65ne  = -1*Vy65
uy65ne  = -1*uy65
Vp65ne  = -1*Vp65
up65ne  = -1*up65
Vp65ne  = -1*Vp65
tenup65ne = -1*tenup65
op.uniaxialMaterial('Hysteretic', 65, Vy65, uy65, Vp65, up65, Vp65, tenup65, Vy65ne, uy65ne, Vp65ne, up65ne, Vp65ne, tenup65ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup66 = 10*up66
Vy66ne  = -1*Vy66
uy66ne  = -1*uy66
Vp66ne  = -1*Vp66
up66ne  = -1*up66
Vp66ne  = -1*Vp66
tenup66ne = -1*tenup66
op.uniaxialMaterial('Hysteretic', 66, Vy66, uy66, Vp66, up66, Vp66, tenup66, Vy66ne, uy66ne, Vp66ne, up66ne, Vp66ne, tenup66ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup67 = 10*up67
Vy67ne  = -1*Vy67
uy67ne  = -1*uy67
Vp67ne  = -1*Vp67
up67ne  = -1*up67
Vp67ne  = -1*Vp67
tenup67ne = -1*tenup67
op.uniaxialMaterial('Hysteretic', 67, Vy67, uy67, Vp67, up67, Vp67, tenup67, Vy67ne, uy67ne, Vp67ne, up67ne, Vp67ne, tenup67ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup68 = 10*up68
Vy68ne  = -1*Vy68
uy68ne  = -1*uy68
Vp68ne  = -1*Vp68
up68ne  = -1*up68
Vp68ne  = -1*Vp68
tenup68ne = -1*tenup68
op.uniaxialMaterial('Hysteretic', 68, Vy68, uy68, Vp68, up68, Vp68, tenup68, Vy68ne, uy68ne, Vp68ne, up68ne, Vp68ne, tenup68ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup69 = 10*up69
Vy69ne  = -1*Vy69
uy69ne  = -1*uy69
Vp69ne  = -1*Vp69
up69ne  = -1*up69
Vp69ne  = -1*Vp69
tenup69ne = -1*tenup69
op.uniaxialMaterial('Hysteretic', 69, Vy69, uy69, Vp69, up69, Vp69, tenup69, Vy69ne, uy69ne, Vp69ne, up69ne, Vp69ne, tenup69ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup70 = 10*up70
Vy70ne  = -1*Vy70
uy70ne  = -1*uy70
Vp70ne  = -1*Vp70
up70ne  = -1*up70
Vp70ne  = -1*Vp70
tenup70ne = -1*tenup70
op.uniaxialMaterial('Hysteretic', 70, Vy70, uy70, Vp70, up70, Vp70, tenup70, Vy70ne, uy70ne, Vp70ne, up70ne, Vp70ne, tenup70ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup71 = 10*up71
Vy71ne  = -1*Vy71
uy71ne  = -1*uy71
Vp71ne  = -1*Vp71
up71ne  = -1*up71
Vp71ne  = -1*Vp71
tenup71ne = -1*tenup71
op.uniaxialMaterial('Hysteretic', 71, Vy71, uy71, Vp71, up71, Vp71, tenup71, Vy71ne, uy71ne, Vp71ne, up71ne, Vp71ne, tenup71ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup72 = 10*up72
Vy72ne  = -1*Vy72
uy72ne  = -1*uy72
Vp72ne  = -1*Vp72
up72ne  = -1*up72
Vp72ne  = -1*Vp72
tenup72ne = -1*tenup72
op.uniaxialMaterial('Hysteretic', 72, Vy72, uy72, Vp72, up72, Vp72, tenup72, Vy72ne, uy72ne, Vp72ne, up72ne, Vp72ne, tenup72ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup73 = 10*up73
Vy73ne  = -1*Vy73
uy73ne  = -1*uy73
Vp73ne  = -1*Vp73
up73ne  = -1*up73
Vp73ne  = -1*Vp73
tenup73ne = -1*tenup73
op.uniaxialMaterial('Hysteretic', 73, Vy73, uy73, Vp73, up73, Vp73, tenup73, Vy73ne, uy73ne, Vp73ne, up73ne, Vp73ne, tenup73ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup74 = 10*up74
Vy74ne  = -1*Vy74
uy74ne  = -1*uy74
Vp74ne  = -1*Vp74
up74ne  = -1*up74
Vp74ne  = -1*Vp74
tenup74ne = -1*tenup74
op.uniaxialMaterial('Hysteretic', 74, Vy74, uy74, Vp74, up74, Vp74, tenup74, Vy74ne, uy74ne, Vp74ne, up74ne, Vp74ne, tenup74ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup75 = 10*up75
Vy75ne  = -1*Vy75
uy75ne  = -1*uy75
Vp75ne  = -1*Vp75
up75ne  = -1*up75
Vp75ne  = -1*Vp75
tenup75ne = -1*tenup75
op.uniaxialMaterial('Hysteretic', 75, Vy75, uy75, Vp75, up75, Vp75, tenup75, Vy75ne, uy75ne, Vp75ne, up75ne, Vp75ne, tenup75ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup76 = 10*up76
Vy76ne  = -1*Vy76
uy76ne  = -1*uy76
Vp76ne  = -1*Vp76
up76ne  = -1*up76
Vp76ne  = -1*Vp76
tenup76ne = -1*tenup76
op.uniaxialMaterial('Hysteretic', 76, Vy76, uy76, Vp76, up76, Vp76, tenup76, Vy76ne, uy76ne, Vp76ne, up76ne, Vp76ne, tenup76ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup77 = 10*up77
Vy77ne  = -1*Vy77
uy77ne  = -1*uy77
Vp77ne  = -1*Vp77
up77ne  = -1*up77
Vp77ne  = -1*Vp77
tenup77ne = -1*tenup77
op.uniaxialMaterial('Hysteretic', 77, Vy77, uy77, Vp77, up77, Vp77, tenup77, Vy77ne, uy77ne, Vp77ne, up77ne, Vp77ne, tenup77ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup78 = 10*up78
Vy78ne  = -1*Vy78
uy78ne  = -1*uy78
Vp78ne  = -1*Vp78
up78ne  = -1*up78
Vp78ne  = -1*Vp78
tenup78ne = -1*tenup78
op.uniaxialMaterial('Hysteretic', 78, Vy78, uy78, Vp78, up78, Vp78, tenup78, Vy78ne, uy78ne, Vp78ne, up78ne, Vp78ne, tenup78ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup79 = 10*up79
Vy79ne  = -1*Vy79
uy79ne  = -1*uy79
Vp79ne  = -1*Vp79
up79ne  = -1*up79
Vp79ne  = -1*Vp79
tenup79ne = -1*tenup79
op.uniaxialMaterial('Hysteretic', 79, Vy79, uy79, Vp79, up79, Vp79, tenup79, Vy79ne, uy79ne, Vp79ne, up79ne, Vp79ne, tenup79ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup80 = 10*up80
Vy80ne  = -1*Vy80
uy80ne  = -1*uy80
Vp80ne  = -1*Vp80
up80ne  = -1*up80
Vp80ne  = -1*Vp80
tenup80ne = -1*tenup80
op.uniaxialMaterial('Hysteretic', 80, Vy80, uy80, Vp80, up80, Vp80, tenup80, Vy80ne, uy80ne, Vp80ne, up80ne, Vp80ne, tenup80ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup81 = 10*up81
Vy81ne  = -1*Vy81
uy81ne  = -1*uy81
Vp81ne  = -1*Vp81
up81ne  = -1*up81
Vp81ne  = -1*Vp81
tenup81ne = -1*tenup81
op.uniaxialMaterial('Hysteretic', 81, Vy81, uy81, Vp81, up81, Vp81, tenup81, Vy81ne, uy81ne, Vp81ne, up81ne, Vp81ne, tenup81ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup82 = 10*up82
Vy82ne  = -1*Vy82
uy82ne  = -1*uy82
Vp82ne  = -1*Vp82
up82ne  = -1*up82
Vp82ne  = -1*Vp82
tenup82ne = -1*tenup82
op.uniaxialMaterial('Hysteretic', 82, Vy82, uy82, Vp82, up82, Vp82, tenup82, Vy82ne, uy82ne, Vp82ne, up82ne, Vp82ne, tenup82ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup83 = 10*up83
Vy83ne  = -1*Vy83
uy83ne  = -1*uy83
Vp83ne  = -1*Vp83
up83ne  = -1*up83
Vp83ne  = -1*Vp83
tenup83ne = -1*tenup83
op.uniaxialMaterial('Hysteretic', 83, Vy83, uy83, Vp83, up83, Vp83, tenup83, Vy83ne, uy83ne, Vp83ne, up83ne, Vp83ne, tenup83ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup84 = 10*up84
Vy84ne  = -1*Vy84
uy84ne  = -1*uy84
Vp84ne  = -1*Vp84
up84ne  = -1*up84
Vp84ne  = -1*Vp84
tenup84ne = -1*tenup84
op.uniaxialMaterial('Hysteretic', 84, Vy84, uy84, Vp84, up84, Vp84, tenup84, Vy84ne, uy84ne, Vp84ne, up84ne, Vp84ne, tenup84ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup85 = 10*up85
Vy85ne  = -1*Vy85
uy85ne  = -1*uy85
Vp85ne  = -1*Vp85
up85ne  = -1*up85
Vp85ne  = -1*Vp85
tenup85ne = -1*tenup85
op.uniaxialMaterial('Hysteretic', 85, Vy85, uy85, Vp85, up85, Vp85, tenup85, Vy85ne, uy85ne, Vp85ne, up85ne, Vp85ne, tenup85ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup86 = 10*up86
Vy86ne  = -1*Vy86
uy86ne  = -1*uy86
Vp86ne  = -1*Vp86
up86ne  = -1*up86
Vp86ne  = -1*Vp86
tenup86ne = -1*tenup86
op.uniaxialMaterial('Hysteretic', 86, Vy86, uy86, Vp86, up86, Vp86, tenup86, Vy86ne, uy86ne, Vp86ne, up86ne, Vp86ne, tenup86ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup87 = 10*up87
Vy87ne  = -1*Vy87
uy87ne  = -1*uy87
Vp87ne  = -1*Vp87
up87ne  = -1*up87
Vp87ne  = -1*Vp87
tenup87ne = -1*tenup87
op.uniaxialMaterial('Hysteretic', 87, Vy87, uy87, Vp87, up87, Vp87, tenup87, Vy87ne, uy87ne, Vp87ne, up87ne, Vp87ne, tenup87ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup88 = 10*up88
Vy88ne  = -1*Vy88
uy88ne  = -1*uy88
Vp88ne  = -1*Vp88
up88ne  = -1*up88
Vp88ne  = -1*Vp88
tenup88ne = -1*tenup88
op.uniaxialMaterial('Hysteretic', 88, Vy88, uy88, Vp88, up88, Vp88, tenup88, Vy88ne, uy88ne, Vp88ne, up88ne, Vp88ne, tenup88ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup89 = 10*up89
Vy89ne  = -1*Vy89
uy89ne  = -1*uy89
Vp89ne  = -1*Vp89
up89ne  = -1*up89
Vp89ne  = -1*Vp89
tenup89ne = -1*tenup89
op.uniaxialMaterial('Hysteretic', 89, Vy89, uy89, Vp89, up89, Vp89, tenup89, Vy89ne, uy89ne, Vp89ne, up89ne, Vp89ne, tenup89ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup90 = 10*up90
Vy90ne  = -1*Vy90
uy90ne  = -1*uy90
Vp90ne  = -1*Vp90
up90ne  = -1*up90
Vp90ne  = -1*Vp90
tenup90ne = -1*tenup90
op.uniaxialMaterial('Hysteretic', 90, Vy90, uy90, Vp90, up90, Vp90, tenup90, Vy90ne, uy90ne, Vp90ne, up90ne, Vp90ne, tenup90ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup91 = 10*up91
Vy91ne  = -1*Vy91
uy91ne  = -1*uy91
Vp91ne  = -1*Vp91
up91ne  = -1*up91
Vp91ne  = -1*Vp91
tenup91ne = -1*tenup91
op.uniaxialMaterial('Hysteretic', 91, Vy91, uy91, Vp91, up91, Vp91, tenup91, Vy91ne, uy91ne, Vp91ne, up91ne, Vp91ne, tenup91ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup92 = 10*up92
Vy92ne  = -1*Vy92
uy92ne  = -1*uy92
Vp92ne  = -1*Vp92
up92ne  = -1*up92
Vp92ne  = -1*Vp92
tenup92ne = -1*tenup92
op.uniaxialMaterial('Hysteretic', 92, Vy92, uy92, Vp92, up92, Vp92, tenup92, Vy92ne, uy92ne, Vp92ne, up92ne, Vp92ne, tenup92ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup93 = 10*up93
Vy93ne  = -1*Vy93
uy93ne  = -1*uy93
Vp93ne  = -1*Vp93
up93ne  = -1*up93
Vp93ne  = -1*Vp93
tenup93ne = -1*tenup93
op.uniaxialMaterial('Hysteretic', 93, Vy93, uy93, Vp93, up93, Vp93, tenup93, Vy93ne, uy93ne, Vp93ne, up93ne, Vp93ne, tenup93ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup94 = 10*up94
Vy94ne  = -1*Vy94
uy94ne  = -1*uy94
Vp94ne  = -1*Vp94
up94ne  = -1*up94
Vp94ne  = -1*Vp94
tenup94ne = -1*tenup94
op.uniaxialMaterial('Hysteretic', 94, Vy94, uy94, Vp94, up94, Vp94, tenup94, Vy94ne, uy94ne, Vp94ne, up94ne, Vp94ne, tenup94ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup95 = 10*up95
Vy95ne  = -1*Vy95
uy95ne  = -1*uy95
Vp95ne  = -1*Vp95
up95ne  = -1*up95
Vp95ne  = -1*Vp95
tenup95ne = -1*tenup95
op.uniaxialMaterial('Hysteretic', 95, Vy95, uy95, Vp95, up95, Vp95, tenup95, Vy95ne, uy95ne, Vp95ne, up95ne, Vp95ne, tenup95ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup96 = 10*up96
Vy96ne  = -1*Vy96
uy96ne  = -1*uy96
Vp96ne  = -1*Vp96
up96ne  = -1*up96
Vp96ne  = -1*Vp96
tenup96ne = -1*tenup96
op.uniaxialMaterial('Hysteretic', 96, Vy96, uy96, Vp96, up96, Vp96, tenup96, Vy96ne, uy96ne, Vp96ne, up96ne, Vp96ne, tenup96ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup97 = 10*up97
Vy97ne  = -1*Vy97
uy97ne  = -1*uy97
Vp97ne  = -1*Vp97
up97ne  = -1*up97
Vp97ne  = -1*Vp97
tenup97ne = -1*tenup97
op.uniaxialMaterial('Hysteretic', 97, Vy97, uy97, Vp97, up97, Vp97, tenup97, Vy97ne, uy97ne, Vp97ne, up97ne, Vp97ne, tenup97ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup98 = 10*up98
Vy98ne  = -1*Vy98
uy98ne  = -1*uy98
Vp98ne  = -1*Vp98
up98ne  = -1*up98
Vp98ne  = -1*Vp98
tenup98ne = -1*tenup98
op.uniaxialMaterial('Hysteretic', 98, Vy98, uy98, Vp98, up98, Vp98, tenup98, Vy98ne, uy98ne, Vp98ne, up98ne, Vp98ne, tenup98ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup99 = 10*up99
Vy99ne  = -1*Vy99
uy99ne  = -1*uy99
Vp99ne  = -1*Vp99
up99ne  = -1*up99
Vp99ne  = -1*Vp99
tenup99ne = -1*tenup99
op.uniaxialMaterial('Hysteretic', 99, Vy99, uy99, Vp99, up99, Vp99, tenup99, Vy99ne, uy99ne, Vp99ne, up99ne, Vp99ne, tenup99ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup100 = 10*up100
Vy100ne  = -1*Vy100
uy100ne  = -1*uy100
Vp100ne  = -1*Vp100
up100ne  = -1*up100
Vp100ne  = -1*Vp100
tenup100ne = -1*tenup100
op.uniaxialMaterial('Hysteretic', 100, Vy100, uy100, Vp100, up100, Vp100, tenup100, Vy100ne, uy100ne, Vp100ne, up100ne, Vp100ne, tenup100ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup101 = 10*up101
Vy101ne  = -1*Vy101
uy101ne  = -1*uy101
Vp101ne  = -1*Vp101
up101ne  = -1*up101
Vp101ne  = -1*Vp101
tenup101ne = -1*tenup101
op.uniaxialMaterial('Hysteretic', 101, Vy101, uy101, Vp101, up101, Vp101, tenup101, Vy101ne, uy101ne, Vp101ne, up101ne, Vp101ne, tenup101ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup102 = 10*up102
Vy102ne  = -1*Vy102
uy102ne  = -1*uy102
Vp102ne  = -1*Vp102
up102ne  = -1*up102
Vp102ne  = -1*Vp102
tenup102ne = -1*tenup102
op.uniaxialMaterial('Hysteretic', 102, Vy102, uy102, Vp102, up102, Vp102, tenup102, Vy102ne, uy102ne, Vp102ne, up102ne, Vp102ne, tenup102ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup103 = 10*up103
Vy103ne  = -1*Vy103
uy103ne  = -1*uy103
Vp103ne  = -1*Vp103
up103ne  = -1*up103
Vp103ne  = -1*Vp103
tenup103ne = -1*tenup103
op.uniaxialMaterial('Hysteretic', 103, Vy103, uy103, Vp103, up103, Vp103, tenup103, Vy103ne, uy103ne, Vp103ne, up103ne, Vp103ne, tenup103ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup104 = 10*up104
Vy104ne  = -1*Vy104
uy104ne  = -1*uy104
Vp104ne  = -1*Vp104
up104ne  = -1*up104
Vp104ne  = -1*Vp104
tenup104ne = -1*tenup104
op.uniaxialMaterial('Hysteretic', 104, Vy104, uy104, Vp104, up104, Vp104, tenup104, Vy104ne, uy104ne, Vp104ne, up104ne, Vp104ne, tenup104ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup105 = 10*up105
Vy105ne  = -1*Vy105
uy105ne  = -1*uy105
Vp105ne  = -1*Vp105
up105ne  = -1*up105
Vp105ne  = -1*Vp105
tenup105ne = -1*tenup105
op.uniaxialMaterial('Hysteretic', 105, Vy105, uy105, Vp105, up105, Vp105, tenup105, Vy105ne, uy105ne, Vp105ne, up105ne, Vp105ne, tenup105ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup106 = 10*up106
Vy106ne  = -1*Vy106
uy106ne  = -1*uy106
Vp106ne  = -1*Vp106
up106ne  = -1*up106
Vp106ne  = -1*Vp106
tenup106ne = -1*tenup106
op.uniaxialMaterial('Hysteretic', 106, Vy106, uy106, Vp106, up106, Vp106, tenup106, Vy106ne, uy106ne, Vp106ne, up106ne, Vp106ne, tenup106ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup107 = 10*up107
Vy107ne  = -1*Vy107
uy107ne  = -1*uy107
Vp107ne  = -1*Vp107
up107ne  = -1*up107
Vp107ne  = -1*Vp107
tenup107ne = -1*tenup107
op.uniaxialMaterial('Hysteretic', 107, Vy107, uy107, Vp107, up107, Vp107, tenup107, Vy107ne, uy107ne, Vp107ne, up107ne, Vp107ne, tenup107ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup108 = 10*up108
Vy108ne  = -1*Vy108
uy108ne  = -1*uy108
Vp108ne  = -1*Vp108
up108ne  = -1*up108
Vp108ne  = -1*Vp108
tenup108ne = -1*tenup108
op.uniaxialMaterial('Hysteretic', 108, Vy108, uy108, Vp108, up108, Vp108, tenup108, Vy108ne, uy108ne, Vp108ne, up108ne, Vp108ne, tenup108ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup109 = 10*up109
Vy109ne  = -1*Vy109
uy109ne  = -1*uy109
Vp109ne  = -1*Vp109
up109ne  = -1*up109
Vp109ne  = -1*Vp109
tenup109ne = -1*tenup109
op.uniaxialMaterial('Hysteretic', 109, Vy109, uy109, Vp109, up109, Vp109, tenup109, Vy109ne, uy109ne, Vp109ne, up109ne, Vp109ne, tenup109ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup110 = 10*up110
Vy110ne  = -1*Vy110
uy110ne  = -1*uy110
Vp110ne  = -1*Vp110
up110ne  = -1*up110
Vp110ne  = -1*Vp110
tenup110ne = -1*tenup110
op.uniaxialMaterial('Hysteretic', 110, Vy110, uy110, Vp110, up110, Vp110, tenup110, Vy110ne, uy110ne, Vp110ne, up110ne, Vp110ne, tenup110ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup111 = 10*up111
Vy111ne  = -1*Vy111
uy111ne  = -1*uy111
Vp111ne  = -1*Vp111
up111ne  = -1*up111
Vp111ne  = -1*Vp111
tenup111ne = -1*tenup111
op.uniaxialMaterial('Hysteretic', 111, Vy111, uy111, Vp111, up111, Vp111, tenup111, Vy111ne, uy111ne, Vp111ne, up111ne, Vp111ne, tenup111ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup112 = 10*up112
Vy112ne  = -1*Vy112
uy112ne  = -1*uy112
Vp112ne  = -1*Vp112
up112ne  = -1*up112
Vp112ne  = -1*Vp112
tenup112ne = -1*tenup112
op.uniaxialMaterial('Hysteretic', 112, Vy112, uy112, Vp112, up112, Vp112, tenup112, Vy112ne, uy112ne, Vp112ne, up112ne, Vp112ne, tenup112ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup113 = 10*up113
Vy113ne  = -1*Vy113
uy113ne  = -1*uy113
Vp113ne  = -1*Vp113
up113ne  = -1*up113
Vp113ne  = -1*Vp113
tenup113ne = -1*tenup113
op.uniaxialMaterial('Hysteretic', 113, Vy113, uy113, Vp113, up113, Vp113, tenup113, Vy113ne, uy113ne, Vp113ne, up113ne, Vp113ne, tenup113ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup114 = 10*up114
Vy114ne  = -1*Vy114
uy114ne  = -1*uy114
Vp114ne  = -1*Vp114
up114ne  = -1*up114
Vp114ne  = -1*Vp114
tenup114ne = -1*tenup114
op.uniaxialMaterial('Hysteretic', 114, Vy114, uy114, Vp114, up114, Vp114, tenup114, Vy114ne, uy114ne, Vp114ne, up114ne, Vp114ne, tenup114ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup115 = 10*up115
Vy115ne  = -1*Vy115
uy115ne  = -1*uy115
Vp115ne  = -1*Vp115
up115ne  = -1*up115
Vp115ne  = -1*Vp115
tenup115ne = -1*tenup115
op.uniaxialMaterial('Hysteretic', 115, Vy115, uy115, Vp115, up115, Vp115, tenup115, Vy115ne, uy115ne, Vp115ne, up115ne, Vp115ne, tenup115ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup116 = 10*up116
Vy116ne  = -1*Vy116
uy116ne  = -1*uy116
Vp116ne  = -1*Vp116
up116ne  = -1*up116
Vp116ne  = -1*Vp116
tenup116ne = -1*tenup116
op.uniaxialMaterial('Hysteretic', 116, Vy116, uy116, Vp116, up116, Vp116, tenup116, Vy116ne, uy116ne, Vp116ne, up116ne, Vp116ne, tenup116ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup117 = 10*up117
Vy117ne  = -1*Vy117
uy117ne  = -1*uy117
Vp117ne  = -1*Vp117
up117ne  = -1*up117
Vp117ne  = -1*Vp117
tenup117ne = -1*tenup117
op.uniaxialMaterial('Hysteretic', 117, Vy117, uy117, Vp117, up117, Vp117, tenup117, Vy117ne, uy117ne, Vp117ne, up117ne, Vp117ne, tenup117ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup118 = 10*up118
Vy118ne  = -1*Vy118
uy118ne  = -1*uy118
Vp118ne  = -1*Vp118
up118ne  = -1*up118
Vp118ne  = -1*Vp118
tenup118ne = -1*tenup118
op.uniaxialMaterial('Hysteretic', 118, Vy118, uy118, Vp118, up118, Vp118, tenup118, Vy118ne, uy118ne, Vp118ne, up118ne, Vp118ne, tenup118ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup119 = 10*up119
Vy119ne  = -1*Vy119
uy119ne  = -1*uy119
Vp119ne  = -1*Vp119
up119ne  = -1*up119
Vp119ne  = -1*Vp119
tenup119ne = -1*tenup119
op.uniaxialMaterial('Hysteretic', 119, Vy119, uy119, Vp119, up119, Vp119, tenup119, Vy119ne, uy119ne, Vp119ne, up119ne, Vp119ne, tenup119ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup120 = 10*up120
Vy120ne  = -1*Vy120
uy120ne  = -1*uy120
Vp120ne  = -1*Vp120
up120ne  = -1*up120
Vp120ne  = -1*Vp120
tenup120ne = -1*tenup120
op.uniaxialMaterial('Hysteretic', 120, Vy120, uy120, Vp120, up120, Vp120, tenup120, Vy120ne, uy120ne, Vp120ne, up120ne, Vp120ne, tenup120ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup121 = 10*up121
Vy121ne  = -1*Vy121
uy121ne  = -1*uy121
Vp121ne  = -1*Vp121
up121ne  = -1*up121
Vp121ne  = -1*Vp121
tenup121ne = -1*tenup121
op.uniaxialMaterial('Hysteretic', 121, Vy121, uy121, Vp121, up121, Vp121, tenup121, Vy121ne, uy121ne, Vp121ne, up121ne, Vp121ne, tenup121ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup122 = 10*up122
Vy122ne  = -1*Vy122
uy122ne  = -1*uy122
Vp122ne  = -1*Vp122
up122ne  = -1*up122
Vp122ne  = -1*Vp122
tenup122ne = -1*tenup122
op.uniaxialMaterial('Hysteretic', 122, Vy122, uy122, Vp122, up122, Vp122, tenup122, Vy122ne, uy122ne, Vp122ne, up122ne, Vp122ne, tenup122ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup123 = 10*up123
Vy123ne  = -1*Vy123
uy123ne  = -1*uy123
Vp123ne  = -1*Vp123
up123ne  = -1*up123
Vp123ne  = -1*Vp123
tenup123ne = -1*tenup123
op.uniaxialMaterial('Hysteretic', 123, Vy123, uy123, Vp123, up123, Vp123, tenup123, Vy123ne, uy123ne, Vp123ne, up123ne, Vp123ne, tenup123ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup124 = 10*up124
Vy124ne  = -1*Vy124
uy124ne  = -1*uy124
Vp124ne  = -1*Vp124
up124ne  = -1*up124
Vp124ne  = -1*Vp124
tenup124ne = -1*tenup124
op.uniaxialMaterial('Hysteretic', 124, Vy124, uy124, Vp124, up124, Vp124, tenup124, Vy124ne, uy124ne, Vp124ne, up124ne, Vp124ne, tenup124ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup125 = 10*up125
Vy125ne  = -1*Vy125
uy125ne  = -1*uy125
Vp125ne  = -1*Vp125
up125ne  = -1*up125
Vp125ne  = -1*Vp125
tenup125ne = -1*tenup125
op.uniaxialMaterial('Hysteretic', 125, Vy125, uy125, Vp125, up125, Vp125, tenup125, Vy125ne, uy125ne, Vp125ne, up125ne, Vp125ne, tenup125ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup126 = 10*up126
Vy126ne  = -1*Vy126
uy126ne  = -1*uy126
Vp126ne  = -1*Vp126
up126ne  = -1*up126
Vp126ne  = -1*Vp126
tenup126ne = -1*tenup126
op.uniaxialMaterial('Hysteretic', 126, Vy126, uy126, Vp126, up126, Vp126, tenup126, Vy126ne, uy126ne, Vp126ne, up126ne, Vp126ne, tenup126ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup127 = 10*up127
Vy127ne  = -1*Vy127
uy127ne  = -1*uy127
Vp127ne  = -1*Vp127
up127ne  = -1*up127
Vp127ne  = -1*Vp127
tenup127ne = -1*tenup127
op.uniaxialMaterial('Hysteretic', 127, Vy127, uy127, Vp127, up127, Vp127, tenup127, Vy127ne, uy127ne, Vp127ne, up127ne, Vp127ne, tenup127ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup128 = 10*up128
Vy128ne  = -1*Vy128
uy128ne  = -1*uy128
Vp128ne  = -1*Vp128
up128ne  = -1*up128
Vp128ne  = -1*Vp128
tenup128ne = -1*tenup128
op.uniaxialMaterial('Hysteretic', 128, Vy128, uy128, Vp128, up128, Vp128, tenup128, Vy128ne, uy128ne, Vp128ne, up128ne, Vp128ne, tenup128ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup129 = 10*up129
Vy129ne  = -1*Vy129
uy129ne  = -1*uy129
Vp129ne  = -1*Vp129
up129ne  = -1*up129
Vp129ne  = -1*Vp129
tenup129ne = -1*tenup129
op.uniaxialMaterial('Hysteretic', 129, Vy129, uy129, Vp129, up129, Vp129, tenup129, Vy129ne, uy129ne, Vp129ne, up129ne, Vp129ne, tenup129ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup130 = 10*up130
Vy130ne  = -1*Vy130
uy130ne  = -1*uy130
Vp130ne  = -1*Vp130
up130ne  = -1*up130
Vp130ne  = -1*Vp130
tenup130ne = -1*tenup130
op.uniaxialMaterial('Hysteretic', 130, Vy130, uy130, Vp130, up130, Vp130, tenup130, Vy130ne, uy130ne, Vp130ne, up130ne, Vp130ne, tenup130ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup131 = 10*up131
Vy131ne  = -1*Vy131
uy131ne  = -1*uy131
Vp131ne  = -1*Vp131
up131ne  = -1*up131
Vp131ne  = -1*Vp131
tenup131ne = -1*tenup131
op.uniaxialMaterial('Hysteretic', 131, Vy131, uy131, Vp131, up131, Vp131, tenup131, Vy131ne, uy131ne, Vp131ne, up131ne, Vp131ne, tenup131ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup132 = 10*up132
Vy132ne  = -1*Vy132
uy132ne  = -1*uy132
Vp132ne  = -1*Vp132
up132ne  = -1*up132
Vp132ne  = -1*Vp132
tenup132ne = -1*tenup132
op.uniaxialMaterial('Hysteretic', 132, Vy132, uy132, Vp132, up132, Vp132, tenup132, Vy132ne, uy132ne, Vp132ne, up132ne, Vp132ne, tenup132ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup133 = 10*up133
Vy133ne  = -1*Vy133
uy133ne  = -1*uy133
Vp133ne  = -1*Vp133
up133ne  = -1*up133
Vp133ne  = -1*Vp133
tenup133ne = -1*tenup133
op.uniaxialMaterial('Hysteretic', 133, Vy133, uy133, Vp133, up133, Vp133, tenup133, Vy133ne, uy133ne, Vp133ne, up133ne, Vp133ne, tenup133ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup134 = 10*up134
Vy134ne  = -1*Vy134
uy134ne  = -1*uy134
Vp134ne  = -1*Vp134
up134ne  = -1*up134
Vp134ne  = -1*Vp134
tenup134ne = -1*tenup134
op.uniaxialMaterial('Hysteretic', 134, Vy134, uy134, Vp134, up134, Vp134, tenup134, Vy134ne, uy134ne, Vp134ne, up134ne, Vp134ne, tenup134ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup135 = 10*up135
Vy135ne  = -1*Vy135
uy135ne  = -1*uy135
Vp135ne  = -1*Vp135
up135ne  = -1*up135
Vp135ne  = -1*Vp135
tenup135ne = -1*tenup135
op.uniaxialMaterial('Hysteretic', 135, Vy135, uy135, Vp135, up135, Vp135, tenup135, Vy135ne, uy135ne, Vp135ne, up135ne, Vp135ne, tenup135ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup136 = 10*up136
Vy136ne  = -1*Vy136
uy136ne  = -1*uy136
Vp136ne  = -1*Vp136
up136ne  = -1*up136
Vp136ne  = -1*Vp136
tenup136ne = -1*tenup136
op.uniaxialMaterial('Hysteretic', 136, Vy136, uy136, Vp136, up136, Vp136, tenup136, Vy136ne, uy136ne, Vp136ne, up136ne, Vp136ne, tenup136ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup137 = 10*up137
Vy137ne  = -1*Vy137
uy137ne  = -1*uy137
Vp137ne  = -1*Vp137
up137ne  = -1*up137
Vp137ne  = -1*Vp137
tenup137ne = -1*tenup137
op.uniaxialMaterial('Hysteretic', 137, Vy137, uy137, Vp137, up137, Vp137, tenup137, Vy137ne, uy137ne, Vp137ne, up137ne, Vp137ne, tenup137ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup138 = 10*up138
Vy138ne  = -1*Vy138
uy138ne  = -1*uy138
Vp138ne  = -1*Vp138
up138ne  = -1*up138
Vp138ne  = -1*Vp138
tenup138ne = -1*tenup138
op.uniaxialMaterial('Hysteretic', 138, Vy138, uy138, Vp138, up138, Vp138, tenup138, Vy138ne, uy138ne, Vp138ne, up138ne, Vp138ne, tenup138ne, 1.0, 1.0, 0.0, 0.0) 
 
tenup139 = 10*up139
Vy139ne  = -1*Vy139
uy139ne  = -1*uy139
Vp139ne  = -1*Vp139
up139ne  = -1*up139
Vp139ne  = -1*Vp139
tenup139ne = -1*tenup139
op.uniaxialMaterial('Hysteretic', 139, Vy139, uy139, Vp139, up139, Vp139, tenup139, Vy139ne, uy139ne, Vp139ne, up139ne, Vp139ne, tenup139ne, 1.0, 1.0, 0.0, 0.0) 
 
 
# Define materials whose stiffness is much greater or much less than the springs
op.uniaxialMaterial('Elastic', 11111, 1e20)
 
# Define bing spring elements
op.element('twoNodeLink', 1111, 20, 21, '-mat', 11111, 1, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 1112, 21, 22, '-mat', 11111, 2, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 1113, 22, 23, '-mat', 11111, 3, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 1114, 23, 24, '-mat', 11111, 4, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 1115, 24, 25, '-mat', 11111, 5, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 1116, 25, 26, '-mat', 11111, 6, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 1117, 26, 27, '-mat', 11111, 7, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 1118, 27, 28, '-mat', 11111, 8, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 1119, 28, 29, '-mat', 11111, 9, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11110, 29, 210, '-mat', 11111, 10, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11111, 210, 211, '-mat', 11111, 11, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11112, 211, 212, '-mat', 11111, 12, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11113, 212, 213, '-mat', 11111, 13, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11114, 213, 214, '-mat', 11111, 14, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11115, 214, 215, '-mat', 11111, 15, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11116, 215, 216, '-mat', 11111, 16, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11117, 216, 217, '-mat', 11111, 17, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11118, 217, 218, '-mat', 11111, 18, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11119, 218, 219, '-mat', 11111, 19, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11120, 219, 220, '-mat', 11111, 20, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11121, 220, 221, '-mat', 11111, 21, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11122, 221, 222, '-mat', 11111, 22, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11123, 222, 223, '-mat', 11111, 23, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11124, 223, 224, '-mat', 11111, 24, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11125, 224, 225, '-mat', 11111, 25, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11126, 225, 226, '-mat', 11111, 26, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11127, 226, 227, '-mat', 11111, 27, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11128, 227, 228, '-mat', 11111, 28, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11129, 228, 229, '-mat', 11111, 29, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11130, 229, 230, '-mat', 11111, 30, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11131, 230, 231, '-mat', 11111, 31, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11132, 231, 232, '-mat', 11111, 32, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11133, 232, 233, '-mat', 11111, 33, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11134, 233, 234, '-mat', 11111, 34, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11135, 234, 235, '-mat', 11111, 35, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11136, 235, 236, '-mat', 11111, 36, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11137, 236, 237, '-mat', 11111, 37, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11138, 237, 238, '-mat', 11111, 38, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11139, 238, 239, '-mat', 11111, 39, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11140, 239, 240, '-mat', 11111, 40, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11141, 240, 241, '-mat', 11111, 41, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11142, 241, 242, '-mat', 11111, 42, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11143, 242, 243, '-mat', 11111, 43, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11144, 243, 244, '-mat', 11111, 44, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11145, 244, 245, '-mat', 11111, 45, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11146, 245, 246, '-mat', 11111, 46, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11147, 246, 247, '-mat', 11111, 47, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11148, 247, 248, '-mat', 11111, 48, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11149, 248, 249, '-mat', 11111, 49, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11150, 249, 250, '-mat', 11111, 50, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11151, 250, 251, '-mat', 11111, 51, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11152, 251, 252, '-mat', 11111, 52, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11153, 252, 253, '-mat', 11111, 53, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11154, 253, 254, '-mat', 11111, 54, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11155, 254, 255, '-mat', 11111, 55, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11156, 255, 256, '-mat', 11111, 56, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11157, 256, 257, '-mat', 11111, 57, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11158, 257, 258, '-mat', 11111, 58, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11159, 258, 259, '-mat', 11111, 59, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11160, 259, 260, '-mat', 11111, 60, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11161, 260, 261, '-mat', 11111, 61, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11162, 261, 262, '-mat', 11111, 62, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11163, 262, 263, '-mat', 11111, 63, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11164, 263, 264, '-mat', 11111, 64, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11165, 264, 265, '-mat', 11111, 65, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11166, 265, 266, '-mat', 11111, 66, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11167, 266, 267, '-mat', 11111, 67, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11168, 267, 268, '-mat', 11111, 68, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11169, 268, 269, '-mat', 11111, 69, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11170, 269, 270, '-mat', 11111, 70, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11171, 270, 271, '-mat', 11111, 71, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11172, 271, 272, '-mat', 11111, 72, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11173, 272, 273, '-mat', 11111, 73, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11174, 273, 274, '-mat', 11111, 74, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11175, 274, 275, '-mat', 11111, 75, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11176, 275, 276, '-mat', 11111, 76, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11177, 276, 277, '-mat', 11111, 77, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11178, 277, 278, '-mat', 11111, 78, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11179, 278, 279, '-mat', 11111, 79, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11180, 279, 280, '-mat', 11111, 80, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11181, 280, 281, '-mat', 11111, 81, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11182, 281, 282, '-mat', 11111, 82, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11183, 282, 283, '-mat', 11111, 83, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11184, 283, 284, '-mat', 11111, 84, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11185, 284, 285, '-mat', 11111, 85, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11186, 285, 286, '-mat', 11111, 86, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11187, 286, 287, '-mat', 11111, 87, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11188, 287, 288, '-mat', 11111, 88, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11189, 288, 289, '-mat', 11111, 89, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11190, 289, 290, '-mat', 11111, 90, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11191, 290, 291, '-mat', 11111, 91, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11192, 291, 292, '-mat', 11111, 92, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11193, 292, 293, '-mat', 11111, 93, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11194, 293, 294, '-mat', 11111, 94, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11195, 294, 295, '-mat', 11111, 95, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11196, 295, 296, '-mat', 11111, 96, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11197, 296, 297, '-mat', 11111, 97, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11198, 297, 298, '-mat', 11111, 98, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 11199, 298, 299, '-mat', 11111, 99, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111100, 299, 2100, '-mat', 11111, 100, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111101, 2100, 2101, '-mat', 11111, 101, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111102, 2101, 2102, '-mat', 11111, 102, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111103, 2102, 2103, '-mat', 11111, 103, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111104, 2103, 2104, '-mat', 11111, 104, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111105, 2104, 2105, '-mat', 11111, 105, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111106, 2105, 2106, '-mat', 11111, 106, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111107, 2106, 2107, '-mat', 11111, 107, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111108, 2107, 2108, '-mat', 11111, 108, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111109, 2108, 2109, '-mat', 11111, 109, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111110, 2109, 2110, '-mat', 11111, 110, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111111, 2110, 2111, '-mat', 11111, 111, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111112, 2111, 2112, '-mat', 11111, 112, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111113, 2112, 2113, '-mat', 11111, 113, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111114, 2113, 2114, '-mat', 11111, 114, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111115, 2114, 2115, '-mat', 11111, 115, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111116, 2115, 2116, '-mat', 11111, 116, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111117, 2116, 2117, '-mat', 11111, 117, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111118, 2117, 2118, '-mat', 11111, 118, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111119, 2118, 2119, '-mat', 11111, 119, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111120, 2119, 2120, '-mat', 11111, 120, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111121, 2120, 2121, '-mat', 11111, 121, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111122, 2121, 2122, '-mat', 11111, 122, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111123, 2122, 2123, '-mat', 11111, 123, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111124, 2123, 2124, '-mat', 11111, 124, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111125, 2124, 2125, '-mat', 11111, 125, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111126, 2125, 2126, '-mat', 11111, 126, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111127, 2126, 2127, '-mat', 11111, 127, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111128, 2127, 2128, '-mat', 11111, 128, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111129, 2128, 2129, '-mat', 11111, 129, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111130, 2129, 2130, '-mat', 11111, 130, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111131, 2130, 2131, '-mat', 11111, 131, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111132, 2131, 2132, '-mat', 11111, 132, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111133, 2132, 2133, '-mat', 11111, 133, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111134, 2133, 2134, '-mat', 11111, 134, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111135, 2134, 2135, '-mat', 11111, 135, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111136, 2135, 2136, '-mat', 11111, 136, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111137, 2136, 2137, '-mat', 11111, 137, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111138, 2137, 2138, '-mat', 11111, 138, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
op.element('twoNodeLink', 111139, 2138, 2139, '-mat', 11111, 139, 11111, '-dir', 1, 2, 3, '-doRayleigh', 1, '-pDelta', 0.5, 0.5)
 