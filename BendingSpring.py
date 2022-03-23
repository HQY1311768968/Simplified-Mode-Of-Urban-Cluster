
# This code is for define bending spring material and bending spring elements
 
import openseespy.opensees as op
 
# Load the initial stiffness(RK1) and yield stiffness(SK2) of the bending springs
RK1 = 4295395019257.0864
SK2 = 0.25*RK1
 
# Load the yield shear force of the bending spring on each floor
My1 = 397073062.55733144
My2 = 396198508.9614438
My3 = 394471204.5660256
My4 = 391917552.14361435
My5 = 388565383.8200871
My6 = 384442904.31169164
My7 = 379577926.2454214
My8 = 373997427.91563135
My9 = 367727271.3786011
My10 = 360791989.94449496
My11 = 353214675.3070089
My12 = 345016916.95513237
My13 = 336218761.5843322
My14 = 326838719.6975728
My15 = 316893804.598861
My16 = 306399587.2896068
My17 = 295370291.1088434
My18 = 283818921.51193243
My19 = 271757413.743678
My20 = 259196815.3386777
My21 = 246147500.84975407
My22 = 232619394.6071
My23 = 218622215.19546825
My24 = 204165746.50153813
My25 = 189260105.77095625
My26 = 173916029.5827259
My27 = 158145205.09538522
My28 = 141960607.7482235
My29 = 125376883.48932478
My30 = 108410856.16720219
My31 = 91082080.91659434
My32 = 73413519.67662649
My33 = 55432644.81939696
My34 = 37172703.62138109
My35 = 18674473.674160402
 
# Calculate the yield shear displacements of the bending spring on each floor
setay1 = My1/RK1
setay2 = My2/RK1
setay3 = My3/RK1
setay4 = My4/RK1
setay5 = My5/RK1
setay6 = My6/RK1
setay7 = My7/RK1
setay8 = My8/RK1
setay9 = My9/RK1
setay10 = My10/RK1
setay11 = My11/RK1
setay12 = My12/RK1
setay13 = My13/RK1
setay14 = My14/RK1
setay15 = My15/RK1
setay16 = My16/RK1
setay17 = My17/RK1
setay18 = My18/RK1
setay19 = My19/RK1
setay20 = My20/RK1
setay21 = My21/RK1
setay22 = My22/RK1
setay23 = My23/RK1
setay24 = My24/RK1
setay25 = My25/RK1
setay26 = My26/RK1
setay27 = My27/RK1
setay28 = My28/RK1
setay29 = My29/RK1
setay30 = My30/RK1
setay31 = My31/RK1
setay32 = My32/RK1
setay33 = My33/RK1
setay34 = My34/RK1
setay35 = My35/RK1
 
# Calculate the shear force at the peak point of the bending springs
Mp1 = 2.23*My1
Mp2 = 2.23*My2
Mp3 = 2.23*My3
Mp4 = 2.23*My4
Mp5 = 2.23*My5
Mp6 = 2.23*My6
Mp7 = 2.23*My7
Mp8 = 2.23*My8
Mp9 = 2.23*My9
Mp10 = 2.23*My10
Mp11 = 2.23*My11
Mp12 = 2.23*My12
Mp13 = 2.23*My13
Mp14 = 2.23*My14
Mp15 = 2.23*My15
Mp16 = 2.23*My16
Mp17 = 2.23*My17
Mp18 = 2.23*My18
Mp19 = 2.23*My19
Mp20 = 2.23*My20
Mp21 = 2.23*My21
Mp22 = 2.23*My22
Mp23 = 2.23*My23
Mp24 = 2.23*My24
Mp25 = 2.23*My25
Mp26 = 2.23*My26
Mp27 = 2.23*My27
Mp28 = 2.23*My28
Mp29 = 2.23*My29
Mp30 = 2.23*My30
Mp31 = 2.23*My31
Mp32 = 2.23*My32
Mp33 = 2.23*My33
Mp34 = 2.23*My34
Mp35 = 2.23*My35
 
# Calculate the displacement of the peak point of the bending springs
setap1 = (Mp1-My1)/SK2+My1/RK1
setap2 = (Mp2-My2)/SK2+My2/RK1
setap3 = (Mp3-My3)/SK2+My3/RK1
setap4 = (Mp4-My4)/SK2+My4/RK1
setap5 = (Mp5-My5)/SK2+My5/RK1
setap6 = (Mp6-My6)/SK2+My6/RK1
setap7 = (Mp7-My7)/SK2+My7/RK1
setap8 = (Mp8-My8)/SK2+My8/RK1
setap9 = (Mp9-My9)/SK2+My9/RK1
setap10 = (Mp10-My10)/SK2+My10/RK1
setap11 = (Mp11-My11)/SK2+My11/RK1
setap12 = (Mp12-My12)/SK2+My12/RK1
setap13 = (Mp13-My13)/SK2+My13/RK1
setap14 = (Mp14-My14)/SK2+My14/RK1
setap15 = (Mp15-My15)/SK2+My15/RK1
setap16 = (Mp16-My16)/SK2+My16/RK1
setap17 = (Mp17-My17)/SK2+My17/RK1
setap18 = (Mp18-My18)/SK2+My18/RK1
setap19 = (Mp19-My19)/SK2+My19/RK1
setap20 = (Mp20-My20)/SK2+My20/RK1
setap21 = (Mp21-My21)/SK2+My21/RK1
setap22 = (Mp22-My22)/SK2+My22/RK1
setap23 = (Mp23-My23)/SK2+My23/RK1
setap24 = (Mp24-My24)/SK2+My24/RK1
setap25 = (Mp25-My25)/SK2+My25/RK1
setap26 = (Mp26-My26)/SK2+My26/RK1
setap27 = (Mp27-My27)/SK2+My27/RK1
setap28 = (Mp28-My28)/SK2+My28/RK1
setap29 = (Mp29-My29)/SK2+My29/RK1
setap30 = (Mp30-My30)/SK2+My30/RK1
setap31 = (Mp31-My31)/SK2+My31/RK1
setap32 = (Mp32-My32)/SK2+My32/RK1
setap33 = (Mp33-My33)/SK2+My33/RK1
setap34 = (Mp34-My34)/SK2+My34/RK1
setap35 = (Mp35-My35)/SK2+My35/RK1
 
# Define bending spring material
tensetap1 = 10*setap1
My1ne  = -1*My1
setay1ne  = -1*setay1
Mp1ne  = -1*Mp1
setap1ne  = -1*setap1
Mp1ne  = -1*Mp1
tensetap1ne = -1*tensetap1
op.uniaxialMaterial('Hysteretic', 36, My1, setay1, Mp1, setap1, Mp1, tensetap1, My1ne, setay1ne, Mp1ne, setap1ne, Mp1ne, tensetap1ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap2 = 10*setap2
My2ne  = -1*My2
setay2ne  = -1*setay2
Mp2ne  = -1*Mp2
setap2ne  = -1*setap2
Mp2ne  = -1*Mp2
tensetap2ne = -1*tensetap2
op.uniaxialMaterial('Hysteretic', 37, My2, setay2, Mp2, setap2, Mp2, tensetap2, My2ne, setay2ne, Mp2ne, setap2ne, Mp2ne, tensetap2ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap3 = 10*setap3
My3ne  = -1*My3
setay3ne  = -1*setay3
Mp3ne  = -1*Mp3
setap3ne  = -1*setap3
Mp3ne  = -1*Mp3
tensetap3ne = -1*tensetap3
op.uniaxialMaterial('Hysteretic', 38, My3, setay3, Mp3, setap3, Mp3, tensetap3, My3ne, setay3ne, Mp3ne, setap3ne, Mp3ne, tensetap3ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap4 = 10*setap4
My4ne  = -1*My4
setay4ne  = -1*setay4
Mp4ne  = -1*Mp4
setap4ne  = -1*setap4
Mp4ne  = -1*Mp4
tensetap4ne = -1*tensetap4
op.uniaxialMaterial('Hysteretic', 39, My4, setay4, Mp4, setap4, Mp4, tensetap4, My4ne, setay4ne, Mp4ne, setap4ne, Mp4ne, tensetap4ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap5 = 10*setap5
My5ne  = -1*My5
setay5ne  = -1*setay5
Mp5ne  = -1*Mp5
setap5ne  = -1*setap5
Mp5ne  = -1*Mp5
tensetap5ne = -1*tensetap5
op.uniaxialMaterial('Hysteretic', 40, My5, setay5, Mp5, setap5, Mp5, tensetap5, My5ne, setay5ne, Mp5ne, setap5ne, Mp5ne, tensetap5ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap6 = 10*setap6
My6ne  = -1*My6
setay6ne  = -1*setay6
Mp6ne  = -1*Mp6
setap6ne  = -1*setap6
Mp6ne  = -1*Mp6
tensetap6ne = -1*tensetap6
op.uniaxialMaterial('Hysteretic', 41, My6, setay6, Mp6, setap6, Mp6, tensetap6, My6ne, setay6ne, Mp6ne, setap6ne, Mp6ne, tensetap6ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap7 = 10*setap7
My7ne  = -1*My7
setay7ne  = -1*setay7
Mp7ne  = -1*Mp7
setap7ne  = -1*setap7
Mp7ne  = -1*Mp7
tensetap7ne = -1*tensetap7
op.uniaxialMaterial('Hysteretic', 42, My7, setay7, Mp7, setap7, Mp7, tensetap7, My7ne, setay7ne, Mp7ne, setap7ne, Mp7ne, tensetap7ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap8 = 10*setap8
My8ne  = -1*My8
setay8ne  = -1*setay8
Mp8ne  = -1*Mp8
setap8ne  = -1*setap8
Mp8ne  = -1*Mp8
tensetap8ne = -1*tensetap8
op.uniaxialMaterial('Hysteretic', 43, My8, setay8, Mp8, setap8, Mp8, tensetap8, My8ne, setay8ne, Mp8ne, setap8ne, Mp8ne, tensetap8ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap9 = 10*setap9
My9ne  = -1*My9
setay9ne  = -1*setay9
Mp9ne  = -1*Mp9
setap9ne  = -1*setap9
Mp9ne  = -1*Mp9
tensetap9ne = -1*tensetap9
op.uniaxialMaterial('Hysteretic', 44, My9, setay9, Mp9, setap9, Mp9, tensetap9, My9ne, setay9ne, Mp9ne, setap9ne, Mp9ne, tensetap9ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap10 = 10*setap10
My10ne  = -1*My10
setay10ne  = -1*setay10
Mp10ne  = -1*Mp10
setap10ne  = -1*setap10
Mp10ne  = -1*Mp10
tensetap10ne = -1*tensetap10
op.uniaxialMaterial('Hysteretic', 45, My10, setay10, Mp10, setap10, Mp10, tensetap10, My10ne, setay10ne, Mp10ne, setap10ne, Mp10ne, tensetap10ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap11 = 10*setap11
My11ne  = -1*My11
setay11ne  = -1*setay11
Mp11ne  = -1*Mp11
setap11ne  = -1*setap11
Mp11ne  = -1*Mp11
tensetap11ne = -1*tensetap11
op.uniaxialMaterial('Hysteretic', 46, My11, setay11, Mp11, setap11, Mp11, tensetap11, My11ne, setay11ne, Mp11ne, setap11ne, Mp11ne, tensetap11ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap12 = 10*setap12
My12ne  = -1*My12
setay12ne  = -1*setay12
Mp12ne  = -1*Mp12
setap12ne  = -1*setap12
Mp12ne  = -1*Mp12
tensetap12ne = -1*tensetap12
op.uniaxialMaterial('Hysteretic', 47, My12, setay12, Mp12, setap12, Mp12, tensetap12, My12ne, setay12ne, Mp12ne, setap12ne, Mp12ne, tensetap12ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap13 = 10*setap13
My13ne  = -1*My13
setay13ne  = -1*setay13
Mp13ne  = -1*Mp13
setap13ne  = -1*setap13
Mp13ne  = -1*Mp13
tensetap13ne = -1*tensetap13
op.uniaxialMaterial('Hysteretic', 48, My13, setay13, Mp13, setap13, Mp13, tensetap13, My13ne, setay13ne, Mp13ne, setap13ne, Mp13ne, tensetap13ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap14 = 10*setap14
My14ne  = -1*My14
setay14ne  = -1*setay14
Mp14ne  = -1*Mp14
setap14ne  = -1*setap14
Mp14ne  = -1*Mp14
tensetap14ne = -1*tensetap14
op.uniaxialMaterial('Hysteretic', 49, My14, setay14, Mp14, setap14, Mp14, tensetap14, My14ne, setay14ne, Mp14ne, setap14ne, Mp14ne, tensetap14ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap15 = 10*setap15
My15ne  = -1*My15
setay15ne  = -1*setay15
Mp15ne  = -1*Mp15
setap15ne  = -1*setap15
Mp15ne  = -1*Mp15
tensetap15ne = -1*tensetap15
op.uniaxialMaterial('Hysteretic', 50, My15, setay15, Mp15, setap15, Mp15, tensetap15, My15ne, setay15ne, Mp15ne, setap15ne, Mp15ne, tensetap15ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap16 = 10*setap16
My16ne  = -1*My16
setay16ne  = -1*setay16
Mp16ne  = -1*Mp16
setap16ne  = -1*setap16
Mp16ne  = -1*Mp16
tensetap16ne = -1*tensetap16
op.uniaxialMaterial('Hysteretic', 51, My16, setay16, Mp16, setap16, Mp16, tensetap16, My16ne, setay16ne, Mp16ne, setap16ne, Mp16ne, tensetap16ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap17 = 10*setap17
My17ne  = -1*My17
setay17ne  = -1*setay17
Mp17ne  = -1*Mp17
setap17ne  = -1*setap17
Mp17ne  = -1*Mp17
tensetap17ne = -1*tensetap17
op.uniaxialMaterial('Hysteretic', 52, My17, setay17, Mp17, setap17, Mp17, tensetap17, My17ne, setay17ne, Mp17ne, setap17ne, Mp17ne, tensetap17ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap18 = 10*setap18
My18ne  = -1*My18
setay18ne  = -1*setay18
Mp18ne  = -1*Mp18
setap18ne  = -1*setap18
Mp18ne  = -1*Mp18
tensetap18ne = -1*tensetap18
op.uniaxialMaterial('Hysteretic', 53, My18, setay18, Mp18, setap18, Mp18, tensetap18, My18ne, setay18ne, Mp18ne, setap18ne, Mp18ne, tensetap18ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap19 = 10*setap19
My19ne  = -1*My19
setay19ne  = -1*setay19
Mp19ne  = -1*Mp19
setap19ne  = -1*setap19
Mp19ne  = -1*Mp19
tensetap19ne = -1*tensetap19
op.uniaxialMaterial('Hysteretic', 54, My19, setay19, Mp19, setap19, Mp19, tensetap19, My19ne, setay19ne, Mp19ne, setap19ne, Mp19ne, tensetap19ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap20 = 10*setap20
My20ne  = -1*My20
setay20ne  = -1*setay20
Mp20ne  = -1*Mp20
setap20ne  = -1*setap20
Mp20ne  = -1*Mp20
tensetap20ne = -1*tensetap20
op.uniaxialMaterial('Hysteretic', 55, My20, setay20, Mp20, setap20, Mp20, tensetap20, My20ne, setay20ne, Mp20ne, setap20ne, Mp20ne, tensetap20ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap21 = 10*setap21
My21ne  = -1*My21
setay21ne  = -1*setay21
Mp21ne  = -1*Mp21
setap21ne  = -1*setap21
Mp21ne  = -1*Mp21
tensetap21ne = -1*tensetap21
op.uniaxialMaterial('Hysteretic', 56, My21, setay21, Mp21, setap21, Mp21, tensetap21, My21ne, setay21ne, Mp21ne, setap21ne, Mp21ne, tensetap21ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap22 = 10*setap22
My22ne  = -1*My22
setay22ne  = -1*setay22
Mp22ne  = -1*Mp22
setap22ne  = -1*setap22
Mp22ne  = -1*Mp22
tensetap22ne = -1*tensetap22
op.uniaxialMaterial('Hysteretic', 57, My22, setay22, Mp22, setap22, Mp22, tensetap22, My22ne, setay22ne, Mp22ne, setap22ne, Mp22ne, tensetap22ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap23 = 10*setap23
My23ne  = -1*My23
setay23ne  = -1*setay23
Mp23ne  = -1*Mp23
setap23ne  = -1*setap23
Mp23ne  = -1*Mp23
tensetap23ne = -1*tensetap23
op.uniaxialMaterial('Hysteretic', 58, My23, setay23, Mp23, setap23, Mp23, tensetap23, My23ne, setay23ne, Mp23ne, setap23ne, Mp23ne, tensetap23ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap24 = 10*setap24
My24ne  = -1*My24
setay24ne  = -1*setay24
Mp24ne  = -1*Mp24
setap24ne  = -1*setap24
Mp24ne  = -1*Mp24
tensetap24ne = -1*tensetap24
op.uniaxialMaterial('Hysteretic', 59, My24, setay24, Mp24, setap24, Mp24, tensetap24, My24ne, setay24ne, Mp24ne, setap24ne, Mp24ne, tensetap24ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap25 = 10*setap25
My25ne  = -1*My25
setay25ne  = -1*setay25
Mp25ne  = -1*Mp25
setap25ne  = -1*setap25
Mp25ne  = -1*Mp25
tensetap25ne = -1*tensetap25
op.uniaxialMaterial('Hysteretic', 60, My25, setay25, Mp25, setap25, Mp25, tensetap25, My25ne, setay25ne, Mp25ne, setap25ne, Mp25ne, tensetap25ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap26 = 10*setap26
My26ne  = -1*My26
setay26ne  = -1*setay26
Mp26ne  = -1*Mp26
setap26ne  = -1*setap26
Mp26ne  = -1*Mp26
tensetap26ne = -1*tensetap26
op.uniaxialMaterial('Hysteretic', 61, My26, setay26, Mp26, setap26, Mp26, tensetap26, My26ne, setay26ne, Mp26ne, setap26ne, Mp26ne, tensetap26ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap27 = 10*setap27
My27ne  = -1*My27
setay27ne  = -1*setay27
Mp27ne  = -1*Mp27
setap27ne  = -1*setap27
Mp27ne  = -1*Mp27
tensetap27ne = -1*tensetap27
op.uniaxialMaterial('Hysteretic', 62, My27, setay27, Mp27, setap27, Mp27, tensetap27, My27ne, setay27ne, Mp27ne, setap27ne, Mp27ne, tensetap27ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap28 = 10*setap28
My28ne  = -1*My28
setay28ne  = -1*setay28
Mp28ne  = -1*Mp28
setap28ne  = -1*setap28
Mp28ne  = -1*Mp28
tensetap28ne = -1*tensetap28
op.uniaxialMaterial('Hysteretic', 63, My28, setay28, Mp28, setap28, Mp28, tensetap28, My28ne, setay28ne, Mp28ne, setap28ne, Mp28ne, tensetap28ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap29 = 10*setap29
My29ne  = -1*My29
setay29ne  = -1*setay29
Mp29ne  = -1*Mp29
setap29ne  = -1*setap29
Mp29ne  = -1*Mp29
tensetap29ne = -1*tensetap29
op.uniaxialMaterial('Hysteretic', 64, My29, setay29, Mp29, setap29, Mp29, tensetap29, My29ne, setay29ne, Mp29ne, setap29ne, Mp29ne, tensetap29ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap30 = 10*setap30
My30ne  = -1*My30
setay30ne  = -1*setay30
Mp30ne  = -1*Mp30
setap30ne  = -1*setap30
Mp30ne  = -1*Mp30
tensetap30ne = -1*tensetap30
op.uniaxialMaterial('Hysteretic', 65, My30, setay30, Mp30, setap30, Mp30, tensetap30, My30ne, setay30ne, Mp30ne, setap30ne, Mp30ne, tensetap30ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap31 = 10*setap31
My31ne  = -1*My31
setay31ne  = -1*setay31
Mp31ne  = -1*Mp31
setap31ne  = -1*setap31
Mp31ne  = -1*Mp31
tensetap31ne = -1*tensetap31
op.uniaxialMaterial('Hysteretic', 66, My31, setay31, Mp31, setap31, Mp31, tensetap31, My31ne, setay31ne, Mp31ne, setap31ne, Mp31ne, tensetap31ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap32 = 10*setap32
My32ne  = -1*My32
setay32ne  = -1*setay32
Mp32ne  = -1*Mp32
setap32ne  = -1*setap32
Mp32ne  = -1*Mp32
tensetap32ne = -1*tensetap32
op.uniaxialMaterial('Hysteretic', 67, My32, setay32, Mp32, setap32, Mp32, tensetap32, My32ne, setay32ne, Mp32ne, setap32ne, Mp32ne, tensetap32ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap33 = 10*setap33
My33ne  = -1*My33
setay33ne  = -1*setay33
Mp33ne  = -1*Mp33
setap33ne  = -1*setap33
Mp33ne  = -1*Mp33
tensetap33ne = -1*tensetap33
op.uniaxialMaterial('Hysteretic', 68, My33, setay33, Mp33, setap33, Mp33, tensetap33, My33ne, setay33ne, Mp33ne, setap33ne, Mp33ne, tensetap33ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap34 = 10*setap34
My34ne  = -1*My34
setay34ne  = -1*setay34
Mp34ne  = -1*Mp34
setap34ne  = -1*setap34
Mp34ne  = -1*Mp34
tensetap34ne = -1*tensetap34
op.uniaxialMaterial('Hysteretic', 69, My34, setay34, Mp34, setap34, Mp34, tensetap34, My34ne, setay34ne, Mp34ne, setap34ne, Mp34ne, tensetap34ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap35 = 10*setap35
My35ne  = -1*My35
setay35ne  = -1*setay35
Mp35ne  = -1*Mp35
setap35ne  = -1*setap35
Mp35ne  = -1*Mp35
tensetap35ne = -1*tensetap35
op.uniaxialMaterial('Hysteretic', 70, My35, setay35, Mp35, setap35, Mp35, tensetap35, My35ne, setay35ne, Mp35ne, setap35ne, Mp35ne, tensetap35ne, 1.0, 1.0, 0.0, 0.0) 
 
 
# Define bing spring elements
op.element('twoNodeLink', 2221, 10, 11, '-mat', 11111, 11111, 36, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2222, 11, 12, '-mat', 11111, 11111, 37, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2223, 12, 13, '-mat', 11111, 11111, 38, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2224, 13, 14, '-mat', 11111, 11111, 39, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2225, 14, 15, '-mat', 11111, 11111, 40, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2226, 15, 16, '-mat', 11111, 11111, 41, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2227, 16, 17, '-mat', 11111, 11111, 42, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2228, 17, 18, '-mat', 11111, 11111, 43, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2229, 18, 19, '-mat', 11111, 11111, 44, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22210, 19, 110, '-mat', 11111, 11111, 45, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22211, 110, 111, '-mat', 11111, 11111, 46, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22212, 111, 112, '-mat', 11111, 11111, 47, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22213, 112, 113, '-mat', 11111, 11111, 48, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22214, 113, 114, '-mat', 11111, 11111, 49, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22215, 114, 115, '-mat', 11111, 11111, 50, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22216, 115, 116, '-mat', 11111, 11111, 51, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22217, 116, 117, '-mat', 11111, 11111, 52, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22218, 117, 118, '-mat', 11111, 11111, 53, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22219, 118, 119, '-mat', 11111, 11111, 54, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22220, 119, 120, '-mat', 11111, 11111, 55, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22221, 120, 121, '-mat', 11111, 11111, 56, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22222, 121, 122, '-mat', 11111, 11111, 57, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22223, 122, 123, '-mat', 11111, 11111, 58, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22224, 123, 124, '-mat', 11111, 11111, 59, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22225, 124, 125, '-mat', 11111, 11111, 60, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22226, 125, 126, '-mat', 11111, 11111, 61, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22227, 126, 127, '-mat', 11111, 11111, 62, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22228, 127, 128, '-mat', 11111, 11111, 63, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22229, 128, 129, '-mat', 11111, 11111, 64, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22230, 129, 130, '-mat', 11111, 11111, 65, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22231, 130, 131, '-mat', 11111, 11111, 66, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22232, 131, 132, '-mat', 11111, 11111, 67, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22233, 132, 133, '-mat', 11111, 11111, 68, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22234, 133, 134, '-mat', 11111, 11111, 69, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22235, 134, 135, '-mat', 11111, 11111, 70, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
 