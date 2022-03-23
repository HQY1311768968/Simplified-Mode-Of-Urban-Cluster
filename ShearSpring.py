
# This code is for define shear spring material and shear spring elements
 
import openseespy.opensees as op
 
# Load the initial stiffness(SK1) and yield stiffness(SK2) of the shear springs
SK1 = 3587202205.8968043
SK2 = 0.25*SK1
 
# Load the yield shear force of the shear spring on each floor
Vy1 = 25271664.8122762
Vy2 = 25271664.8122762
Vy3 = 25271664.8122762
Vy4 = 25271664.8122762
Vy5 = 25271664.8122762
Vy6 = 25271664.8122762
Vy7 = 25271664.8122762
Vy8 = 25271664.8122762
Vy9 = 25271664.8122762
Vy10 = 25271664.8122762
Vy11 = 25271664.8122762
Vy12 = 25271664.8122762
Vy13 = 25271664.8122762
Vy14 = 25271664.8122762
Vy15 = 25271664.8122762
Vy16 = 25271664.8122762
Vy17 = 25271664.8122762
Vy18 = 25271664.8122762
Vy19 = 25271664.8122762
Vy20 = 25271664.8122762
Vy21 = 25271664.8122762
Vy22 = 25271664.8122762
Vy23 = 25271664.8122762
Vy24 = 25271664.8122762
Vy25 = 25271664.8122762
Vy26 = 25271664.8122762
Vy27 = 25271664.8122762
Vy28 = 25271664.8122762
Vy29 = 25271664.8122762
Vy30 = 25271664.8122762
Vy31 = 25271664.8122762
Vy32 = 25271664.8122762
Vy33 = 25271664.8122762
Vy34 = 25271664.8122762
Vy35 = 25271664.8122762
 
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
 
# Calculate the shear force at the peak point of the shear springs
Vp1 = 56355812.53137592
Vp2 = 56355812.53137592
Vp3 = 56355812.53137592
Vp4 = 56355812.53137592
Vp5 = 56355812.53137592
Vp6 = 56355812.53137592
Vp7 = 56355812.53137592
Vp8 = 56355812.53137592
Vp9 = 56355812.53137592
Vp10 = 56355812.53137592
Vp11 = 56355812.53137592
Vp12 = 56355812.53137592
Vp13 = 56355812.53137592
Vp14 = 56355812.53137592
Vp15 = 56355812.53137592
Vp16 = 56355812.53137592
Vp17 = 56355812.53137592
Vp18 = 56355812.53137592
Vp19 = 56355812.53137592
Vp20 = 56355812.53137592
Vp21 = 56355812.53137592
Vp22 = 56355812.53137592
Vp23 = 56355812.53137592
Vp24 = 56355812.53137592
Vp25 = 56355812.53137592
Vp26 = 56355812.53137592
Vp27 = 56355812.53137592
Vp28 = 56355812.53137592
Vp29 = 56355812.53137592
Vp30 = 56355812.53137592
Vp31 = 56355812.53137592
Vp32 = 56355812.53137592
Vp33 = 56355812.53137592
Vp34 = 56355812.53137592
Vp35 = 56355812.53137592
 
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
 