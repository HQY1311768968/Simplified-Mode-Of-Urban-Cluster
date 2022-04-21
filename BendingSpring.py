
# This code is for define bending spring material and bending spring elements
 
import openseespy.opensees as op
 
# Load the initial stiffness(RK1) and yield stiffness(SK2) of the bending springs
RK1 = 214860683837604.44
SK2 = 0.25*RK1
 
# Load the yield shear force of the bending spring on each floor
My1 = 2811670121.898059
My2 = 2811277500.3235965
My3 = 2810494033.5093455
My4 = 2809321770.8276563
My5 = 2807762845.697228
My6 = 2805819461.717309
My7 = 2803493884.827446
My8 = 2800788428.742503
My9 = 2797705444.2039657
My10 = 2794247315.9319553
My11 = 2790416461.570845
My12 = 2786215328.5002894
My13 = 2781646390.296536
My14 = 2776712145.1337748
My15 = 2771415114.893638
My16 = 2765757842.8320665
My17 = 2759742890.0702434
My18 = 2753372832.4509926
My19 = 2746650257.8607864
My20 = 2739577762.9291673
My21 = 2732157948.957409
My22 = 2724393418.0863843
My23 = 2716286770.2182846
My24 = 2707840600.1465955
My25 = 2699057494.515577
My26 = 2689940029.1177416
My27 = 2680490767.02654
My28 = 2670712257.2661953
My29 = 2660607033.504706
My30 = 2650177612.87955
My31 = 2639426495.3318133
My32 = 2628356163.3267665
My33 = 2616969081.490117
My34 = 2605267696.0518126
My35 = 2593254434.4122767
My36 = 2580931704.9060297
My37 = 2568301896.447952
My38 = 2555367377.901446
My39 = 2542130497.430609
My40 = 2528593582.053741
My41 = 2514758937.250521
My42 = 2500628846.432677
My43 = 2486205570.43058
My44 = 2471491347.24588
My45 = 2456488392.023419
My46 = 2441198897.011932
My47 = 2425625031.5157237
My48 = 2409768942.0593834
My49 = 2393632752.772271
My50 = 2377218565.7662334
My51 = 2360528461.4102716
My52 = 2343564498.662456
My53 = 2326328715.557534
My54 = 2308823129.686724
My55 = 2291049738.5221686
My56 = 2273010519.7084107
My57 = 2254707431.496121
My58 = 2236142413.234876
My59 = 2217317385.7668066
My60 = 2198234251.7726626
My61 = 2178894896.2676525
My62 = 2159301187.2424793
My63 = 2139454976.2737224
My64 = 2119358099.068289
My65 = 2099012376.1127717
My66 = 2078419613.4923308
My67 = 2057581603.7144053
My68 = 2036500126.4249463
My69 = 2015176949.1472547
My70 = 1993613828.187011
My71 = 1971812509.578114
My72 = 1949774729.9206438
My73 = 1927502217.1889973
My74 = 1904996691.6925106
My75 = 1882259867.1608942
My76 = 1859293451.7494826
My77 = 1836099148.9732487
My78 = 1812678658.7673264
My79 = 1789033678.7033515
My80 = 1765165905.1699753
My81 = 1741077034.4055588
My82 = 1716768763.5675652
My83 = 1692242791.9777215
My84 = 1667500822.3542473
My85 = 1642544561.868463
My86 = 1617375723.1679306
My87 = 1591996025.600036
My88 = 1566407196.5556228
My89 = 1540610972.6916156
My90 = 1514609101.1151574
My91 = 1488403340.8162603
My92 = 1461995464.3862689
My93 = 1435387259.7065203
My94 = 1408580531.538318
My95 = 1381577103.2964387
My96 = 1354378819.1415832
My97 = 1326987546.0528076
My98 = 1299405175.5943384
My99 = 1271633625.62643
My100 = 1243674842.255881
My101 = 1215530801.7634742
My102 = 1187203512.0917015
My103 = 1158695014.064897
My104 = 1130007382.9022162
My105 = 1101142730.010869
My106 = 1072103204.5464369
My107 = 1042890994.756042
My108 = 1013508329.8923154
My109 = 983957483.007848
My110 = 954240773.9870036
My111 = 924360572.4057393
My112 = 894319300.9810121
My113 = 864119440.269803
My114 = 833763533.811029
My115 = 803254192.5435221
My116 = 772594098.9151027
My117 = 741786011.8762096
My118 = 710832772.1038672
My119 = 679737305.3792256
My120 = 648502623.9100006
My121 = 617131827.7967179
My122 = 585628107.1587956
My123 = 553994741.9935921
My124 = 522235098.314218
My125 = 490352624.29984885
My126 = 458350850.0408078
My127 = 426233387.45732814
My128 = 394003925.32777315
My129 = 361666224.25199395
My130 = 329224122.4674584
My131 = 296681550.62984776
My132 = 264042539.40118837
My133 = 231311219.65956143
My134 = 198491847.86525792
My135 = 165588876.38269952
My136 = 132607015.48237236
My137 = 99551211.80279133
My138 = 66426645.83457105
My139 = 33239221.77489641
 
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
setay36 = My36/RK1
setay37 = My37/RK1
setay38 = My38/RK1
setay39 = My39/RK1
setay40 = My40/RK1
setay41 = My41/RK1
setay42 = My42/RK1
setay43 = My43/RK1
setay44 = My44/RK1
setay45 = My45/RK1
setay46 = My46/RK1
setay47 = My47/RK1
setay48 = My48/RK1
setay49 = My49/RK1
setay50 = My50/RK1
setay51 = My51/RK1
setay52 = My52/RK1
setay53 = My53/RK1
setay54 = My54/RK1
setay55 = My55/RK1
setay56 = My56/RK1
setay57 = My57/RK1
setay58 = My58/RK1
setay59 = My59/RK1
setay60 = My60/RK1
setay61 = My61/RK1
setay62 = My62/RK1
setay63 = My63/RK1
setay64 = My64/RK1
setay65 = My65/RK1
setay66 = My66/RK1
setay67 = My67/RK1
setay68 = My68/RK1
setay69 = My69/RK1
setay70 = My70/RK1
setay71 = My71/RK1
setay72 = My72/RK1
setay73 = My73/RK1
setay74 = My74/RK1
setay75 = My75/RK1
setay76 = My76/RK1
setay77 = My77/RK1
setay78 = My78/RK1
setay79 = My79/RK1
setay80 = My80/RK1
setay81 = My81/RK1
setay82 = My82/RK1
setay83 = My83/RK1
setay84 = My84/RK1
setay85 = My85/RK1
setay86 = My86/RK1
setay87 = My87/RK1
setay88 = My88/RK1
setay89 = My89/RK1
setay90 = My90/RK1
setay91 = My91/RK1
setay92 = My92/RK1
setay93 = My93/RK1
setay94 = My94/RK1
setay95 = My95/RK1
setay96 = My96/RK1
setay97 = My97/RK1
setay98 = My98/RK1
setay99 = My99/RK1
setay100 = My100/RK1
setay101 = My101/RK1
setay102 = My102/RK1
setay103 = My103/RK1
setay104 = My104/RK1
setay105 = My105/RK1
setay106 = My106/RK1
setay107 = My107/RK1
setay108 = My108/RK1
setay109 = My109/RK1
setay110 = My110/RK1
setay111 = My111/RK1
setay112 = My112/RK1
setay113 = My113/RK1
setay114 = My114/RK1
setay115 = My115/RK1
setay116 = My116/RK1
setay117 = My117/RK1
setay118 = My118/RK1
setay119 = My119/RK1
setay120 = My120/RK1
setay121 = My121/RK1
setay122 = My122/RK1
setay123 = My123/RK1
setay124 = My124/RK1
setay125 = My125/RK1
setay126 = My126/RK1
setay127 = My127/RK1
setay128 = My128/RK1
setay129 = My129/RK1
setay130 = My130/RK1
setay131 = My131/RK1
setay132 = My132/RK1
setay133 = My133/RK1
setay134 = My134/RK1
setay135 = My135/RK1
setay136 = My136/RK1
setay137 = My137/RK1
setay138 = My138/RK1
setay139 = My139/RK1
 
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
Mp36 = 2.23*My36
Mp37 = 2.23*My37
Mp38 = 2.23*My38
Mp39 = 2.23*My39
Mp40 = 2.23*My40
Mp41 = 2.23*My41
Mp42 = 2.23*My42
Mp43 = 2.23*My43
Mp44 = 2.23*My44
Mp45 = 2.23*My45
Mp46 = 2.23*My46
Mp47 = 2.23*My47
Mp48 = 2.23*My48
Mp49 = 2.23*My49
Mp50 = 2.23*My50
Mp51 = 2.23*My51
Mp52 = 2.23*My52
Mp53 = 2.23*My53
Mp54 = 2.23*My54
Mp55 = 2.23*My55
Mp56 = 2.23*My56
Mp57 = 2.23*My57
Mp58 = 2.23*My58
Mp59 = 2.23*My59
Mp60 = 2.23*My60
Mp61 = 2.23*My61
Mp62 = 2.23*My62
Mp63 = 2.23*My63
Mp64 = 2.23*My64
Mp65 = 2.23*My65
Mp66 = 2.23*My66
Mp67 = 2.23*My67
Mp68 = 2.23*My68
Mp69 = 2.23*My69
Mp70 = 2.23*My70
Mp71 = 2.23*My71
Mp72 = 2.23*My72
Mp73 = 2.23*My73
Mp74 = 2.23*My74
Mp75 = 2.23*My75
Mp76 = 2.23*My76
Mp77 = 2.23*My77
Mp78 = 2.23*My78
Mp79 = 2.23*My79
Mp80 = 2.23*My80
Mp81 = 2.23*My81
Mp82 = 2.23*My82
Mp83 = 2.23*My83
Mp84 = 2.23*My84
Mp85 = 2.23*My85
Mp86 = 2.23*My86
Mp87 = 2.23*My87
Mp88 = 2.23*My88
Mp89 = 2.23*My89
Mp90 = 2.23*My90
Mp91 = 2.23*My91
Mp92 = 2.23*My92
Mp93 = 2.23*My93
Mp94 = 2.23*My94
Mp95 = 2.23*My95
Mp96 = 2.23*My96
Mp97 = 2.23*My97
Mp98 = 2.23*My98
Mp99 = 2.23*My99
Mp100 = 2.23*My100
Mp101 = 2.23*My101
Mp102 = 2.23*My102
Mp103 = 2.23*My103
Mp104 = 2.23*My104
Mp105 = 2.23*My105
Mp106 = 2.23*My106
Mp107 = 2.23*My107
Mp108 = 2.23*My108
Mp109 = 2.23*My109
Mp110 = 2.23*My110
Mp111 = 2.23*My111
Mp112 = 2.23*My112
Mp113 = 2.23*My113
Mp114 = 2.23*My114
Mp115 = 2.23*My115
Mp116 = 2.23*My116
Mp117 = 2.23*My117
Mp118 = 2.23*My118
Mp119 = 2.23*My119
Mp120 = 2.23*My120
Mp121 = 2.23*My121
Mp122 = 2.23*My122
Mp123 = 2.23*My123
Mp124 = 2.23*My124
Mp125 = 2.23*My125
Mp126 = 2.23*My126
Mp127 = 2.23*My127
Mp128 = 2.23*My128
Mp129 = 2.23*My129
Mp130 = 2.23*My130
Mp131 = 2.23*My131
Mp132 = 2.23*My132
Mp133 = 2.23*My133
Mp134 = 2.23*My134
Mp135 = 2.23*My135
Mp136 = 2.23*My136
Mp137 = 2.23*My137
Mp138 = 2.23*My138
Mp139 = 2.23*My139
 
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
setap36 = (Mp36-My36)/SK2+My36/RK1
setap37 = (Mp37-My37)/SK2+My37/RK1
setap38 = (Mp38-My38)/SK2+My38/RK1
setap39 = (Mp39-My39)/SK2+My39/RK1
setap40 = (Mp40-My40)/SK2+My40/RK1
setap41 = (Mp41-My41)/SK2+My41/RK1
setap42 = (Mp42-My42)/SK2+My42/RK1
setap43 = (Mp43-My43)/SK2+My43/RK1
setap44 = (Mp44-My44)/SK2+My44/RK1
setap45 = (Mp45-My45)/SK2+My45/RK1
setap46 = (Mp46-My46)/SK2+My46/RK1
setap47 = (Mp47-My47)/SK2+My47/RK1
setap48 = (Mp48-My48)/SK2+My48/RK1
setap49 = (Mp49-My49)/SK2+My49/RK1
setap50 = (Mp50-My50)/SK2+My50/RK1
setap51 = (Mp51-My51)/SK2+My51/RK1
setap52 = (Mp52-My52)/SK2+My52/RK1
setap53 = (Mp53-My53)/SK2+My53/RK1
setap54 = (Mp54-My54)/SK2+My54/RK1
setap55 = (Mp55-My55)/SK2+My55/RK1
setap56 = (Mp56-My56)/SK2+My56/RK1
setap57 = (Mp57-My57)/SK2+My57/RK1
setap58 = (Mp58-My58)/SK2+My58/RK1
setap59 = (Mp59-My59)/SK2+My59/RK1
setap60 = (Mp60-My60)/SK2+My60/RK1
setap61 = (Mp61-My61)/SK2+My61/RK1
setap62 = (Mp62-My62)/SK2+My62/RK1
setap63 = (Mp63-My63)/SK2+My63/RK1
setap64 = (Mp64-My64)/SK2+My64/RK1
setap65 = (Mp65-My65)/SK2+My65/RK1
setap66 = (Mp66-My66)/SK2+My66/RK1
setap67 = (Mp67-My67)/SK2+My67/RK1
setap68 = (Mp68-My68)/SK2+My68/RK1
setap69 = (Mp69-My69)/SK2+My69/RK1
setap70 = (Mp70-My70)/SK2+My70/RK1
setap71 = (Mp71-My71)/SK2+My71/RK1
setap72 = (Mp72-My72)/SK2+My72/RK1
setap73 = (Mp73-My73)/SK2+My73/RK1
setap74 = (Mp74-My74)/SK2+My74/RK1
setap75 = (Mp75-My75)/SK2+My75/RK1
setap76 = (Mp76-My76)/SK2+My76/RK1
setap77 = (Mp77-My77)/SK2+My77/RK1
setap78 = (Mp78-My78)/SK2+My78/RK1
setap79 = (Mp79-My79)/SK2+My79/RK1
setap80 = (Mp80-My80)/SK2+My80/RK1
setap81 = (Mp81-My81)/SK2+My81/RK1
setap82 = (Mp82-My82)/SK2+My82/RK1
setap83 = (Mp83-My83)/SK2+My83/RK1
setap84 = (Mp84-My84)/SK2+My84/RK1
setap85 = (Mp85-My85)/SK2+My85/RK1
setap86 = (Mp86-My86)/SK2+My86/RK1
setap87 = (Mp87-My87)/SK2+My87/RK1
setap88 = (Mp88-My88)/SK2+My88/RK1
setap89 = (Mp89-My89)/SK2+My89/RK1
setap90 = (Mp90-My90)/SK2+My90/RK1
setap91 = (Mp91-My91)/SK2+My91/RK1
setap92 = (Mp92-My92)/SK2+My92/RK1
setap93 = (Mp93-My93)/SK2+My93/RK1
setap94 = (Mp94-My94)/SK2+My94/RK1
setap95 = (Mp95-My95)/SK2+My95/RK1
setap96 = (Mp96-My96)/SK2+My96/RK1
setap97 = (Mp97-My97)/SK2+My97/RK1
setap98 = (Mp98-My98)/SK2+My98/RK1
setap99 = (Mp99-My99)/SK2+My99/RK1
setap100 = (Mp100-My100)/SK2+My100/RK1
setap101 = (Mp101-My101)/SK2+My101/RK1
setap102 = (Mp102-My102)/SK2+My102/RK1
setap103 = (Mp103-My103)/SK2+My103/RK1
setap104 = (Mp104-My104)/SK2+My104/RK1
setap105 = (Mp105-My105)/SK2+My105/RK1
setap106 = (Mp106-My106)/SK2+My106/RK1
setap107 = (Mp107-My107)/SK2+My107/RK1
setap108 = (Mp108-My108)/SK2+My108/RK1
setap109 = (Mp109-My109)/SK2+My109/RK1
setap110 = (Mp110-My110)/SK2+My110/RK1
setap111 = (Mp111-My111)/SK2+My111/RK1
setap112 = (Mp112-My112)/SK2+My112/RK1
setap113 = (Mp113-My113)/SK2+My113/RK1
setap114 = (Mp114-My114)/SK2+My114/RK1
setap115 = (Mp115-My115)/SK2+My115/RK1
setap116 = (Mp116-My116)/SK2+My116/RK1
setap117 = (Mp117-My117)/SK2+My117/RK1
setap118 = (Mp118-My118)/SK2+My118/RK1
setap119 = (Mp119-My119)/SK2+My119/RK1
setap120 = (Mp120-My120)/SK2+My120/RK1
setap121 = (Mp121-My121)/SK2+My121/RK1
setap122 = (Mp122-My122)/SK2+My122/RK1
setap123 = (Mp123-My123)/SK2+My123/RK1
setap124 = (Mp124-My124)/SK2+My124/RK1
setap125 = (Mp125-My125)/SK2+My125/RK1
setap126 = (Mp126-My126)/SK2+My126/RK1
setap127 = (Mp127-My127)/SK2+My127/RK1
setap128 = (Mp128-My128)/SK2+My128/RK1
setap129 = (Mp129-My129)/SK2+My129/RK1
setap130 = (Mp130-My130)/SK2+My130/RK1
setap131 = (Mp131-My131)/SK2+My131/RK1
setap132 = (Mp132-My132)/SK2+My132/RK1
setap133 = (Mp133-My133)/SK2+My133/RK1
setap134 = (Mp134-My134)/SK2+My134/RK1
setap135 = (Mp135-My135)/SK2+My135/RK1
setap136 = (Mp136-My136)/SK2+My136/RK1
setap137 = (Mp137-My137)/SK2+My137/RK1
setap138 = (Mp138-My138)/SK2+My138/RK1
setap139 = (Mp139-My139)/SK2+My139/RK1
 
# Define bending spring material
tensetap1 = 10*setap1
My1ne  = -1*My1
setay1ne  = -1*setay1
Mp1ne  = -1*Mp1
setap1ne  = -1*setap1
Mp1ne  = -1*Mp1
tensetap1ne = -1*tensetap1
op.uniaxialMaterial('Hysteretic', 140, My1, setay1, Mp1, setap1, Mp1, tensetap1, My1ne, setay1ne, Mp1ne, setap1ne, Mp1ne, tensetap1ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap2 = 10*setap2
My2ne  = -1*My2
setay2ne  = -1*setay2
Mp2ne  = -1*Mp2
setap2ne  = -1*setap2
Mp2ne  = -1*Mp2
tensetap2ne = -1*tensetap2
op.uniaxialMaterial('Hysteretic', 141, My2, setay2, Mp2, setap2, Mp2, tensetap2, My2ne, setay2ne, Mp2ne, setap2ne, Mp2ne, tensetap2ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap3 = 10*setap3
My3ne  = -1*My3
setay3ne  = -1*setay3
Mp3ne  = -1*Mp3
setap3ne  = -1*setap3
Mp3ne  = -1*Mp3
tensetap3ne = -1*tensetap3
op.uniaxialMaterial('Hysteretic', 142, My3, setay3, Mp3, setap3, Mp3, tensetap3, My3ne, setay3ne, Mp3ne, setap3ne, Mp3ne, tensetap3ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap4 = 10*setap4
My4ne  = -1*My4
setay4ne  = -1*setay4
Mp4ne  = -1*Mp4
setap4ne  = -1*setap4
Mp4ne  = -1*Mp4
tensetap4ne = -1*tensetap4
op.uniaxialMaterial('Hysteretic', 143, My4, setay4, Mp4, setap4, Mp4, tensetap4, My4ne, setay4ne, Mp4ne, setap4ne, Mp4ne, tensetap4ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap5 = 10*setap5
My5ne  = -1*My5
setay5ne  = -1*setay5
Mp5ne  = -1*Mp5
setap5ne  = -1*setap5
Mp5ne  = -1*Mp5
tensetap5ne = -1*tensetap5
op.uniaxialMaterial('Hysteretic', 144, My5, setay5, Mp5, setap5, Mp5, tensetap5, My5ne, setay5ne, Mp5ne, setap5ne, Mp5ne, tensetap5ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap6 = 10*setap6
My6ne  = -1*My6
setay6ne  = -1*setay6
Mp6ne  = -1*Mp6
setap6ne  = -1*setap6
Mp6ne  = -1*Mp6
tensetap6ne = -1*tensetap6
op.uniaxialMaterial('Hysteretic', 145, My6, setay6, Mp6, setap6, Mp6, tensetap6, My6ne, setay6ne, Mp6ne, setap6ne, Mp6ne, tensetap6ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap7 = 10*setap7
My7ne  = -1*My7
setay7ne  = -1*setay7
Mp7ne  = -1*Mp7
setap7ne  = -1*setap7
Mp7ne  = -1*Mp7
tensetap7ne = -1*tensetap7
op.uniaxialMaterial('Hysteretic', 146, My7, setay7, Mp7, setap7, Mp7, tensetap7, My7ne, setay7ne, Mp7ne, setap7ne, Mp7ne, tensetap7ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap8 = 10*setap8
My8ne  = -1*My8
setay8ne  = -1*setay8
Mp8ne  = -1*Mp8
setap8ne  = -1*setap8
Mp8ne  = -1*Mp8
tensetap8ne = -1*tensetap8
op.uniaxialMaterial('Hysteretic', 147, My8, setay8, Mp8, setap8, Mp8, tensetap8, My8ne, setay8ne, Mp8ne, setap8ne, Mp8ne, tensetap8ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap9 = 10*setap9
My9ne  = -1*My9
setay9ne  = -1*setay9
Mp9ne  = -1*Mp9
setap9ne  = -1*setap9
Mp9ne  = -1*Mp9
tensetap9ne = -1*tensetap9
op.uniaxialMaterial('Hysteretic', 148, My9, setay9, Mp9, setap9, Mp9, tensetap9, My9ne, setay9ne, Mp9ne, setap9ne, Mp9ne, tensetap9ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap10 = 10*setap10
My10ne  = -1*My10
setay10ne  = -1*setay10
Mp10ne  = -1*Mp10
setap10ne  = -1*setap10
Mp10ne  = -1*Mp10
tensetap10ne = -1*tensetap10
op.uniaxialMaterial('Hysteretic', 149, My10, setay10, Mp10, setap10, Mp10, tensetap10, My10ne, setay10ne, Mp10ne, setap10ne, Mp10ne, tensetap10ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap11 = 10*setap11
My11ne  = -1*My11
setay11ne  = -1*setay11
Mp11ne  = -1*Mp11
setap11ne  = -1*setap11
Mp11ne  = -1*Mp11
tensetap11ne = -1*tensetap11
op.uniaxialMaterial('Hysteretic', 150, My11, setay11, Mp11, setap11, Mp11, tensetap11, My11ne, setay11ne, Mp11ne, setap11ne, Mp11ne, tensetap11ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap12 = 10*setap12
My12ne  = -1*My12
setay12ne  = -1*setay12
Mp12ne  = -1*Mp12
setap12ne  = -1*setap12
Mp12ne  = -1*Mp12
tensetap12ne = -1*tensetap12
op.uniaxialMaterial('Hysteretic', 151, My12, setay12, Mp12, setap12, Mp12, tensetap12, My12ne, setay12ne, Mp12ne, setap12ne, Mp12ne, tensetap12ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap13 = 10*setap13
My13ne  = -1*My13
setay13ne  = -1*setay13
Mp13ne  = -1*Mp13
setap13ne  = -1*setap13
Mp13ne  = -1*Mp13
tensetap13ne = -1*tensetap13
op.uniaxialMaterial('Hysteretic', 152, My13, setay13, Mp13, setap13, Mp13, tensetap13, My13ne, setay13ne, Mp13ne, setap13ne, Mp13ne, tensetap13ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap14 = 10*setap14
My14ne  = -1*My14
setay14ne  = -1*setay14
Mp14ne  = -1*Mp14
setap14ne  = -1*setap14
Mp14ne  = -1*Mp14
tensetap14ne = -1*tensetap14
op.uniaxialMaterial('Hysteretic', 153, My14, setay14, Mp14, setap14, Mp14, tensetap14, My14ne, setay14ne, Mp14ne, setap14ne, Mp14ne, tensetap14ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap15 = 10*setap15
My15ne  = -1*My15
setay15ne  = -1*setay15
Mp15ne  = -1*Mp15
setap15ne  = -1*setap15
Mp15ne  = -1*Mp15
tensetap15ne = -1*tensetap15
op.uniaxialMaterial('Hysteretic', 154, My15, setay15, Mp15, setap15, Mp15, tensetap15, My15ne, setay15ne, Mp15ne, setap15ne, Mp15ne, tensetap15ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap16 = 10*setap16
My16ne  = -1*My16
setay16ne  = -1*setay16
Mp16ne  = -1*Mp16
setap16ne  = -1*setap16
Mp16ne  = -1*Mp16
tensetap16ne = -1*tensetap16
op.uniaxialMaterial('Hysteretic', 155, My16, setay16, Mp16, setap16, Mp16, tensetap16, My16ne, setay16ne, Mp16ne, setap16ne, Mp16ne, tensetap16ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap17 = 10*setap17
My17ne  = -1*My17
setay17ne  = -1*setay17
Mp17ne  = -1*Mp17
setap17ne  = -1*setap17
Mp17ne  = -1*Mp17
tensetap17ne = -1*tensetap17
op.uniaxialMaterial('Hysteretic', 156, My17, setay17, Mp17, setap17, Mp17, tensetap17, My17ne, setay17ne, Mp17ne, setap17ne, Mp17ne, tensetap17ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap18 = 10*setap18
My18ne  = -1*My18
setay18ne  = -1*setay18
Mp18ne  = -1*Mp18
setap18ne  = -1*setap18
Mp18ne  = -1*Mp18
tensetap18ne = -1*tensetap18
op.uniaxialMaterial('Hysteretic', 157, My18, setay18, Mp18, setap18, Mp18, tensetap18, My18ne, setay18ne, Mp18ne, setap18ne, Mp18ne, tensetap18ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap19 = 10*setap19
My19ne  = -1*My19
setay19ne  = -1*setay19
Mp19ne  = -1*Mp19
setap19ne  = -1*setap19
Mp19ne  = -1*Mp19
tensetap19ne = -1*tensetap19
op.uniaxialMaterial('Hysteretic', 158, My19, setay19, Mp19, setap19, Mp19, tensetap19, My19ne, setay19ne, Mp19ne, setap19ne, Mp19ne, tensetap19ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap20 = 10*setap20
My20ne  = -1*My20
setay20ne  = -1*setay20
Mp20ne  = -1*Mp20
setap20ne  = -1*setap20
Mp20ne  = -1*Mp20
tensetap20ne = -1*tensetap20
op.uniaxialMaterial('Hysteretic', 159, My20, setay20, Mp20, setap20, Mp20, tensetap20, My20ne, setay20ne, Mp20ne, setap20ne, Mp20ne, tensetap20ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap21 = 10*setap21
My21ne  = -1*My21
setay21ne  = -1*setay21
Mp21ne  = -1*Mp21
setap21ne  = -1*setap21
Mp21ne  = -1*Mp21
tensetap21ne = -1*tensetap21
op.uniaxialMaterial('Hysteretic', 160, My21, setay21, Mp21, setap21, Mp21, tensetap21, My21ne, setay21ne, Mp21ne, setap21ne, Mp21ne, tensetap21ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap22 = 10*setap22
My22ne  = -1*My22
setay22ne  = -1*setay22
Mp22ne  = -1*Mp22
setap22ne  = -1*setap22
Mp22ne  = -1*Mp22
tensetap22ne = -1*tensetap22
op.uniaxialMaterial('Hysteretic', 161, My22, setay22, Mp22, setap22, Mp22, tensetap22, My22ne, setay22ne, Mp22ne, setap22ne, Mp22ne, tensetap22ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap23 = 10*setap23
My23ne  = -1*My23
setay23ne  = -1*setay23
Mp23ne  = -1*Mp23
setap23ne  = -1*setap23
Mp23ne  = -1*Mp23
tensetap23ne = -1*tensetap23
op.uniaxialMaterial('Hysteretic', 162, My23, setay23, Mp23, setap23, Mp23, tensetap23, My23ne, setay23ne, Mp23ne, setap23ne, Mp23ne, tensetap23ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap24 = 10*setap24
My24ne  = -1*My24
setay24ne  = -1*setay24
Mp24ne  = -1*Mp24
setap24ne  = -1*setap24
Mp24ne  = -1*Mp24
tensetap24ne = -1*tensetap24
op.uniaxialMaterial('Hysteretic', 163, My24, setay24, Mp24, setap24, Mp24, tensetap24, My24ne, setay24ne, Mp24ne, setap24ne, Mp24ne, tensetap24ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap25 = 10*setap25
My25ne  = -1*My25
setay25ne  = -1*setay25
Mp25ne  = -1*Mp25
setap25ne  = -1*setap25
Mp25ne  = -1*Mp25
tensetap25ne = -1*tensetap25
op.uniaxialMaterial('Hysteretic', 164, My25, setay25, Mp25, setap25, Mp25, tensetap25, My25ne, setay25ne, Mp25ne, setap25ne, Mp25ne, tensetap25ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap26 = 10*setap26
My26ne  = -1*My26
setay26ne  = -1*setay26
Mp26ne  = -1*Mp26
setap26ne  = -1*setap26
Mp26ne  = -1*Mp26
tensetap26ne = -1*tensetap26
op.uniaxialMaterial('Hysteretic', 165, My26, setay26, Mp26, setap26, Mp26, tensetap26, My26ne, setay26ne, Mp26ne, setap26ne, Mp26ne, tensetap26ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap27 = 10*setap27
My27ne  = -1*My27
setay27ne  = -1*setay27
Mp27ne  = -1*Mp27
setap27ne  = -1*setap27
Mp27ne  = -1*Mp27
tensetap27ne = -1*tensetap27
op.uniaxialMaterial('Hysteretic', 166, My27, setay27, Mp27, setap27, Mp27, tensetap27, My27ne, setay27ne, Mp27ne, setap27ne, Mp27ne, tensetap27ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap28 = 10*setap28
My28ne  = -1*My28
setay28ne  = -1*setay28
Mp28ne  = -1*Mp28
setap28ne  = -1*setap28
Mp28ne  = -1*Mp28
tensetap28ne = -1*tensetap28
op.uniaxialMaterial('Hysteretic', 167, My28, setay28, Mp28, setap28, Mp28, tensetap28, My28ne, setay28ne, Mp28ne, setap28ne, Mp28ne, tensetap28ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap29 = 10*setap29
My29ne  = -1*My29
setay29ne  = -1*setay29
Mp29ne  = -1*Mp29
setap29ne  = -1*setap29
Mp29ne  = -1*Mp29
tensetap29ne = -1*tensetap29
op.uniaxialMaterial('Hysteretic', 168, My29, setay29, Mp29, setap29, Mp29, tensetap29, My29ne, setay29ne, Mp29ne, setap29ne, Mp29ne, tensetap29ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap30 = 10*setap30
My30ne  = -1*My30
setay30ne  = -1*setay30
Mp30ne  = -1*Mp30
setap30ne  = -1*setap30
Mp30ne  = -1*Mp30
tensetap30ne = -1*tensetap30
op.uniaxialMaterial('Hysteretic', 169, My30, setay30, Mp30, setap30, Mp30, tensetap30, My30ne, setay30ne, Mp30ne, setap30ne, Mp30ne, tensetap30ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap31 = 10*setap31
My31ne  = -1*My31
setay31ne  = -1*setay31
Mp31ne  = -1*Mp31
setap31ne  = -1*setap31
Mp31ne  = -1*Mp31
tensetap31ne = -1*tensetap31
op.uniaxialMaterial('Hysteretic', 170, My31, setay31, Mp31, setap31, Mp31, tensetap31, My31ne, setay31ne, Mp31ne, setap31ne, Mp31ne, tensetap31ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap32 = 10*setap32
My32ne  = -1*My32
setay32ne  = -1*setay32
Mp32ne  = -1*Mp32
setap32ne  = -1*setap32
Mp32ne  = -1*Mp32
tensetap32ne = -1*tensetap32
op.uniaxialMaterial('Hysteretic', 171, My32, setay32, Mp32, setap32, Mp32, tensetap32, My32ne, setay32ne, Mp32ne, setap32ne, Mp32ne, tensetap32ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap33 = 10*setap33
My33ne  = -1*My33
setay33ne  = -1*setay33
Mp33ne  = -1*Mp33
setap33ne  = -1*setap33
Mp33ne  = -1*Mp33
tensetap33ne = -1*tensetap33
op.uniaxialMaterial('Hysteretic', 172, My33, setay33, Mp33, setap33, Mp33, tensetap33, My33ne, setay33ne, Mp33ne, setap33ne, Mp33ne, tensetap33ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap34 = 10*setap34
My34ne  = -1*My34
setay34ne  = -1*setay34
Mp34ne  = -1*Mp34
setap34ne  = -1*setap34
Mp34ne  = -1*Mp34
tensetap34ne = -1*tensetap34
op.uniaxialMaterial('Hysteretic', 173, My34, setay34, Mp34, setap34, Mp34, tensetap34, My34ne, setay34ne, Mp34ne, setap34ne, Mp34ne, tensetap34ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap35 = 10*setap35
My35ne  = -1*My35
setay35ne  = -1*setay35
Mp35ne  = -1*Mp35
setap35ne  = -1*setap35
Mp35ne  = -1*Mp35
tensetap35ne = -1*tensetap35
op.uniaxialMaterial('Hysteretic', 174, My35, setay35, Mp35, setap35, Mp35, tensetap35, My35ne, setay35ne, Mp35ne, setap35ne, Mp35ne, tensetap35ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap36 = 10*setap36
My36ne  = -1*My36
setay36ne  = -1*setay36
Mp36ne  = -1*Mp36
setap36ne  = -1*setap36
Mp36ne  = -1*Mp36
tensetap36ne = -1*tensetap36
op.uniaxialMaterial('Hysteretic', 175, My36, setay36, Mp36, setap36, Mp36, tensetap36, My36ne, setay36ne, Mp36ne, setap36ne, Mp36ne, tensetap36ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap37 = 10*setap37
My37ne  = -1*My37
setay37ne  = -1*setay37
Mp37ne  = -1*Mp37
setap37ne  = -1*setap37
Mp37ne  = -1*Mp37
tensetap37ne = -1*tensetap37
op.uniaxialMaterial('Hysteretic', 176, My37, setay37, Mp37, setap37, Mp37, tensetap37, My37ne, setay37ne, Mp37ne, setap37ne, Mp37ne, tensetap37ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap38 = 10*setap38
My38ne  = -1*My38
setay38ne  = -1*setay38
Mp38ne  = -1*Mp38
setap38ne  = -1*setap38
Mp38ne  = -1*Mp38
tensetap38ne = -1*tensetap38
op.uniaxialMaterial('Hysteretic', 177, My38, setay38, Mp38, setap38, Mp38, tensetap38, My38ne, setay38ne, Mp38ne, setap38ne, Mp38ne, tensetap38ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap39 = 10*setap39
My39ne  = -1*My39
setay39ne  = -1*setay39
Mp39ne  = -1*Mp39
setap39ne  = -1*setap39
Mp39ne  = -1*Mp39
tensetap39ne = -1*tensetap39
op.uniaxialMaterial('Hysteretic', 178, My39, setay39, Mp39, setap39, Mp39, tensetap39, My39ne, setay39ne, Mp39ne, setap39ne, Mp39ne, tensetap39ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap40 = 10*setap40
My40ne  = -1*My40
setay40ne  = -1*setay40
Mp40ne  = -1*Mp40
setap40ne  = -1*setap40
Mp40ne  = -1*Mp40
tensetap40ne = -1*tensetap40
op.uniaxialMaterial('Hysteretic', 179, My40, setay40, Mp40, setap40, Mp40, tensetap40, My40ne, setay40ne, Mp40ne, setap40ne, Mp40ne, tensetap40ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap41 = 10*setap41
My41ne  = -1*My41
setay41ne  = -1*setay41
Mp41ne  = -1*Mp41
setap41ne  = -1*setap41
Mp41ne  = -1*Mp41
tensetap41ne = -1*tensetap41
op.uniaxialMaterial('Hysteretic', 180, My41, setay41, Mp41, setap41, Mp41, tensetap41, My41ne, setay41ne, Mp41ne, setap41ne, Mp41ne, tensetap41ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap42 = 10*setap42
My42ne  = -1*My42
setay42ne  = -1*setay42
Mp42ne  = -1*Mp42
setap42ne  = -1*setap42
Mp42ne  = -1*Mp42
tensetap42ne = -1*tensetap42
op.uniaxialMaterial('Hysteretic', 181, My42, setay42, Mp42, setap42, Mp42, tensetap42, My42ne, setay42ne, Mp42ne, setap42ne, Mp42ne, tensetap42ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap43 = 10*setap43
My43ne  = -1*My43
setay43ne  = -1*setay43
Mp43ne  = -1*Mp43
setap43ne  = -1*setap43
Mp43ne  = -1*Mp43
tensetap43ne = -1*tensetap43
op.uniaxialMaterial('Hysteretic', 182, My43, setay43, Mp43, setap43, Mp43, tensetap43, My43ne, setay43ne, Mp43ne, setap43ne, Mp43ne, tensetap43ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap44 = 10*setap44
My44ne  = -1*My44
setay44ne  = -1*setay44
Mp44ne  = -1*Mp44
setap44ne  = -1*setap44
Mp44ne  = -1*Mp44
tensetap44ne = -1*tensetap44
op.uniaxialMaterial('Hysteretic', 183, My44, setay44, Mp44, setap44, Mp44, tensetap44, My44ne, setay44ne, Mp44ne, setap44ne, Mp44ne, tensetap44ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap45 = 10*setap45
My45ne  = -1*My45
setay45ne  = -1*setay45
Mp45ne  = -1*Mp45
setap45ne  = -1*setap45
Mp45ne  = -1*Mp45
tensetap45ne = -1*tensetap45
op.uniaxialMaterial('Hysteretic', 184, My45, setay45, Mp45, setap45, Mp45, tensetap45, My45ne, setay45ne, Mp45ne, setap45ne, Mp45ne, tensetap45ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap46 = 10*setap46
My46ne  = -1*My46
setay46ne  = -1*setay46
Mp46ne  = -1*Mp46
setap46ne  = -1*setap46
Mp46ne  = -1*Mp46
tensetap46ne = -1*tensetap46
op.uniaxialMaterial('Hysteretic', 185, My46, setay46, Mp46, setap46, Mp46, tensetap46, My46ne, setay46ne, Mp46ne, setap46ne, Mp46ne, tensetap46ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap47 = 10*setap47
My47ne  = -1*My47
setay47ne  = -1*setay47
Mp47ne  = -1*Mp47
setap47ne  = -1*setap47
Mp47ne  = -1*Mp47
tensetap47ne = -1*tensetap47
op.uniaxialMaterial('Hysteretic', 186, My47, setay47, Mp47, setap47, Mp47, tensetap47, My47ne, setay47ne, Mp47ne, setap47ne, Mp47ne, tensetap47ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap48 = 10*setap48
My48ne  = -1*My48
setay48ne  = -1*setay48
Mp48ne  = -1*Mp48
setap48ne  = -1*setap48
Mp48ne  = -1*Mp48
tensetap48ne = -1*tensetap48
op.uniaxialMaterial('Hysteretic', 187, My48, setay48, Mp48, setap48, Mp48, tensetap48, My48ne, setay48ne, Mp48ne, setap48ne, Mp48ne, tensetap48ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap49 = 10*setap49
My49ne  = -1*My49
setay49ne  = -1*setay49
Mp49ne  = -1*Mp49
setap49ne  = -1*setap49
Mp49ne  = -1*Mp49
tensetap49ne = -1*tensetap49
op.uniaxialMaterial('Hysteretic', 188, My49, setay49, Mp49, setap49, Mp49, tensetap49, My49ne, setay49ne, Mp49ne, setap49ne, Mp49ne, tensetap49ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap50 = 10*setap50
My50ne  = -1*My50
setay50ne  = -1*setay50
Mp50ne  = -1*Mp50
setap50ne  = -1*setap50
Mp50ne  = -1*Mp50
tensetap50ne = -1*tensetap50
op.uniaxialMaterial('Hysteretic', 189, My50, setay50, Mp50, setap50, Mp50, tensetap50, My50ne, setay50ne, Mp50ne, setap50ne, Mp50ne, tensetap50ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap51 = 10*setap51
My51ne  = -1*My51
setay51ne  = -1*setay51
Mp51ne  = -1*Mp51
setap51ne  = -1*setap51
Mp51ne  = -1*Mp51
tensetap51ne = -1*tensetap51
op.uniaxialMaterial('Hysteretic', 190, My51, setay51, Mp51, setap51, Mp51, tensetap51, My51ne, setay51ne, Mp51ne, setap51ne, Mp51ne, tensetap51ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap52 = 10*setap52
My52ne  = -1*My52
setay52ne  = -1*setay52
Mp52ne  = -1*Mp52
setap52ne  = -1*setap52
Mp52ne  = -1*Mp52
tensetap52ne = -1*tensetap52
op.uniaxialMaterial('Hysteretic', 191, My52, setay52, Mp52, setap52, Mp52, tensetap52, My52ne, setay52ne, Mp52ne, setap52ne, Mp52ne, tensetap52ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap53 = 10*setap53
My53ne  = -1*My53
setay53ne  = -1*setay53
Mp53ne  = -1*Mp53
setap53ne  = -1*setap53
Mp53ne  = -1*Mp53
tensetap53ne = -1*tensetap53
op.uniaxialMaterial('Hysteretic', 192, My53, setay53, Mp53, setap53, Mp53, tensetap53, My53ne, setay53ne, Mp53ne, setap53ne, Mp53ne, tensetap53ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap54 = 10*setap54
My54ne  = -1*My54
setay54ne  = -1*setay54
Mp54ne  = -1*Mp54
setap54ne  = -1*setap54
Mp54ne  = -1*Mp54
tensetap54ne = -1*tensetap54
op.uniaxialMaterial('Hysteretic', 193, My54, setay54, Mp54, setap54, Mp54, tensetap54, My54ne, setay54ne, Mp54ne, setap54ne, Mp54ne, tensetap54ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap55 = 10*setap55
My55ne  = -1*My55
setay55ne  = -1*setay55
Mp55ne  = -1*Mp55
setap55ne  = -1*setap55
Mp55ne  = -1*Mp55
tensetap55ne = -1*tensetap55
op.uniaxialMaterial('Hysteretic', 194, My55, setay55, Mp55, setap55, Mp55, tensetap55, My55ne, setay55ne, Mp55ne, setap55ne, Mp55ne, tensetap55ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap56 = 10*setap56
My56ne  = -1*My56
setay56ne  = -1*setay56
Mp56ne  = -1*Mp56
setap56ne  = -1*setap56
Mp56ne  = -1*Mp56
tensetap56ne = -1*tensetap56
op.uniaxialMaterial('Hysteretic', 195, My56, setay56, Mp56, setap56, Mp56, tensetap56, My56ne, setay56ne, Mp56ne, setap56ne, Mp56ne, tensetap56ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap57 = 10*setap57
My57ne  = -1*My57
setay57ne  = -1*setay57
Mp57ne  = -1*Mp57
setap57ne  = -1*setap57
Mp57ne  = -1*Mp57
tensetap57ne = -1*tensetap57
op.uniaxialMaterial('Hysteretic', 196, My57, setay57, Mp57, setap57, Mp57, tensetap57, My57ne, setay57ne, Mp57ne, setap57ne, Mp57ne, tensetap57ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap58 = 10*setap58
My58ne  = -1*My58
setay58ne  = -1*setay58
Mp58ne  = -1*Mp58
setap58ne  = -1*setap58
Mp58ne  = -1*Mp58
tensetap58ne = -1*tensetap58
op.uniaxialMaterial('Hysteretic', 197, My58, setay58, Mp58, setap58, Mp58, tensetap58, My58ne, setay58ne, Mp58ne, setap58ne, Mp58ne, tensetap58ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap59 = 10*setap59
My59ne  = -1*My59
setay59ne  = -1*setay59
Mp59ne  = -1*Mp59
setap59ne  = -1*setap59
Mp59ne  = -1*Mp59
tensetap59ne = -1*tensetap59
op.uniaxialMaterial('Hysteretic', 198, My59, setay59, Mp59, setap59, Mp59, tensetap59, My59ne, setay59ne, Mp59ne, setap59ne, Mp59ne, tensetap59ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap60 = 10*setap60
My60ne  = -1*My60
setay60ne  = -1*setay60
Mp60ne  = -1*Mp60
setap60ne  = -1*setap60
Mp60ne  = -1*Mp60
tensetap60ne = -1*tensetap60
op.uniaxialMaterial('Hysteretic', 199, My60, setay60, Mp60, setap60, Mp60, tensetap60, My60ne, setay60ne, Mp60ne, setap60ne, Mp60ne, tensetap60ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap61 = 10*setap61
My61ne  = -1*My61
setay61ne  = -1*setay61
Mp61ne  = -1*Mp61
setap61ne  = -1*setap61
Mp61ne  = -1*Mp61
tensetap61ne = -1*tensetap61
op.uniaxialMaterial('Hysteretic', 200, My61, setay61, Mp61, setap61, Mp61, tensetap61, My61ne, setay61ne, Mp61ne, setap61ne, Mp61ne, tensetap61ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap62 = 10*setap62
My62ne  = -1*My62
setay62ne  = -1*setay62
Mp62ne  = -1*Mp62
setap62ne  = -1*setap62
Mp62ne  = -1*Mp62
tensetap62ne = -1*tensetap62
op.uniaxialMaterial('Hysteretic', 201, My62, setay62, Mp62, setap62, Mp62, tensetap62, My62ne, setay62ne, Mp62ne, setap62ne, Mp62ne, tensetap62ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap63 = 10*setap63
My63ne  = -1*My63
setay63ne  = -1*setay63
Mp63ne  = -1*Mp63
setap63ne  = -1*setap63
Mp63ne  = -1*Mp63
tensetap63ne = -1*tensetap63
op.uniaxialMaterial('Hysteretic', 202, My63, setay63, Mp63, setap63, Mp63, tensetap63, My63ne, setay63ne, Mp63ne, setap63ne, Mp63ne, tensetap63ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap64 = 10*setap64
My64ne  = -1*My64
setay64ne  = -1*setay64
Mp64ne  = -1*Mp64
setap64ne  = -1*setap64
Mp64ne  = -1*Mp64
tensetap64ne = -1*tensetap64
op.uniaxialMaterial('Hysteretic', 203, My64, setay64, Mp64, setap64, Mp64, tensetap64, My64ne, setay64ne, Mp64ne, setap64ne, Mp64ne, tensetap64ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap65 = 10*setap65
My65ne  = -1*My65
setay65ne  = -1*setay65
Mp65ne  = -1*Mp65
setap65ne  = -1*setap65
Mp65ne  = -1*Mp65
tensetap65ne = -1*tensetap65
op.uniaxialMaterial('Hysteretic', 204, My65, setay65, Mp65, setap65, Mp65, tensetap65, My65ne, setay65ne, Mp65ne, setap65ne, Mp65ne, tensetap65ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap66 = 10*setap66
My66ne  = -1*My66
setay66ne  = -1*setay66
Mp66ne  = -1*Mp66
setap66ne  = -1*setap66
Mp66ne  = -1*Mp66
tensetap66ne = -1*tensetap66
op.uniaxialMaterial('Hysteretic', 205, My66, setay66, Mp66, setap66, Mp66, tensetap66, My66ne, setay66ne, Mp66ne, setap66ne, Mp66ne, tensetap66ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap67 = 10*setap67
My67ne  = -1*My67
setay67ne  = -1*setay67
Mp67ne  = -1*Mp67
setap67ne  = -1*setap67
Mp67ne  = -1*Mp67
tensetap67ne = -1*tensetap67
op.uniaxialMaterial('Hysteretic', 206, My67, setay67, Mp67, setap67, Mp67, tensetap67, My67ne, setay67ne, Mp67ne, setap67ne, Mp67ne, tensetap67ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap68 = 10*setap68
My68ne  = -1*My68
setay68ne  = -1*setay68
Mp68ne  = -1*Mp68
setap68ne  = -1*setap68
Mp68ne  = -1*Mp68
tensetap68ne = -1*tensetap68
op.uniaxialMaterial('Hysteretic', 207, My68, setay68, Mp68, setap68, Mp68, tensetap68, My68ne, setay68ne, Mp68ne, setap68ne, Mp68ne, tensetap68ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap69 = 10*setap69
My69ne  = -1*My69
setay69ne  = -1*setay69
Mp69ne  = -1*Mp69
setap69ne  = -1*setap69
Mp69ne  = -1*Mp69
tensetap69ne = -1*tensetap69
op.uniaxialMaterial('Hysteretic', 208, My69, setay69, Mp69, setap69, Mp69, tensetap69, My69ne, setay69ne, Mp69ne, setap69ne, Mp69ne, tensetap69ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap70 = 10*setap70
My70ne  = -1*My70
setay70ne  = -1*setay70
Mp70ne  = -1*Mp70
setap70ne  = -1*setap70
Mp70ne  = -1*Mp70
tensetap70ne = -1*tensetap70
op.uniaxialMaterial('Hysteretic', 209, My70, setay70, Mp70, setap70, Mp70, tensetap70, My70ne, setay70ne, Mp70ne, setap70ne, Mp70ne, tensetap70ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap71 = 10*setap71
My71ne  = -1*My71
setay71ne  = -1*setay71
Mp71ne  = -1*Mp71
setap71ne  = -1*setap71
Mp71ne  = -1*Mp71
tensetap71ne = -1*tensetap71
op.uniaxialMaterial('Hysteretic', 210, My71, setay71, Mp71, setap71, Mp71, tensetap71, My71ne, setay71ne, Mp71ne, setap71ne, Mp71ne, tensetap71ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap72 = 10*setap72
My72ne  = -1*My72
setay72ne  = -1*setay72
Mp72ne  = -1*Mp72
setap72ne  = -1*setap72
Mp72ne  = -1*Mp72
tensetap72ne = -1*tensetap72
op.uniaxialMaterial('Hysteretic', 211, My72, setay72, Mp72, setap72, Mp72, tensetap72, My72ne, setay72ne, Mp72ne, setap72ne, Mp72ne, tensetap72ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap73 = 10*setap73
My73ne  = -1*My73
setay73ne  = -1*setay73
Mp73ne  = -1*Mp73
setap73ne  = -1*setap73
Mp73ne  = -1*Mp73
tensetap73ne = -1*tensetap73
op.uniaxialMaterial('Hysteretic', 212, My73, setay73, Mp73, setap73, Mp73, tensetap73, My73ne, setay73ne, Mp73ne, setap73ne, Mp73ne, tensetap73ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap74 = 10*setap74
My74ne  = -1*My74
setay74ne  = -1*setay74
Mp74ne  = -1*Mp74
setap74ne  = -1*setap74
Mp74ne  = -1*Mp74
tensetap74ne = -1*tensetap74
op.uniaxialMaterial('Hysteretic', 213, My74, setay74, Mp74, setap74, Mp74, tensetap74, My74ne, setay74ne, Mp74ne, setap74ne, Mp74ne, tensetap74ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap75 = 10*setap75
My75ne  = -1*My75
setay75ne  = -1*setay75
Mp75ne  = -1*Mp75
setap75ne  = -1*setap75
Mp75ne  = -1*Mp75
tensetap75ne = -1*tensetap75
op.uniaxialMaterial('Hysteretic', 214, My75, setay75, Mp75, setap75, Mp75, tensetap75, My75ne, setay75ne, Mp75ne, setap75ne, Mp75ne, tensetap75ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap76 = 10*setap76
My76ne  = -1*My76
setay76ne  = -1*setay76
Mp76ne  = -1*Mp76
setap76ne  = -1*setap76
Mp76ne  = -1*Mp76
tensetap76ne = -1*tensetap76
op.uniaxialMaterial('Hysteretic', 215, My76, setay76, Mp76, setap76, Mp76, tensetap76, My76ne, setay76ne, Mp76ne, setap76ne, Mp76ne, tensetap76ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap77 = 10*setap77
My77ne  = -1*My77
setay77ne  = -1*setay77
Mp77ne  = -1*Mp77
setap77ne  = -1*setap77
Mp77ne  = -1*Mp77
tensetap77ne = -1*tensetap77
op.uniaxialMaterial('Hysteretic', 216, My77, setay77, Mp77, setap77, Mp77, tensetap77, My77ne, setay77ne, Mp77ne, setap77ne, Mp77ne, tensetap77ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap78 = 10*setap78
My78ne  = -1*My78
setay78ne  = -1*setay78
Mp78ne  = -1*Mp78
setap78ne  = -1*setap78
Mp78ne  = -1*Mp78
tensetap78ne = -1*tensetap78
op.uniaxialMaterial('Hysteretic', 217, My78, setay78, Mp78, setap78, Mp78, tensetap78, My78ne, setay78ne, Mp78ne, setap78ne, Mp78ne, tensetap78ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap79 = 10*setap79
My79ne  = -1*My79
setay79ne  = -1*setay79
Mp79ne  = -1*Mp79
setap79ne  = -1*setap79
Mp79ne  = -1*Mp79
tensetap79ne = -1*tensetap79
op.uniaxialMaterial('Hysteretic', 218, My79, setay79, Mp79, setap79, Mp79, tensetap79, My79ne, setay79ne, Mp79ne, setap79ne, Mp79ne, tensetap79ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap80 = 10*setap80
My80ne  = -1*My80
setay80ne  = -1*setay80
Mp80ne  = -1*Mp80
setap80ne  = -1*setap80
Mp80ne  = -1*Mp80
tensetap80ne = -1*tensetap80
op.uniaxialMaterial('Hysteretic', 219, My80, setay80, Mp80, setap80, Mp80, tensetap80, My80ne, setay80ne, Mp80ne, setap80ne, Mp80ne, tensetap80ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap81 = 10*setap81
My81ne  = -1*My81
setay81ne  = -1*setay81
Mp81ne  = -1*Mp81
setap81ne  = -1*setap81
Mp81ne  = -1*Mp81
tensetap81ne = -1*tensetap81
op.uniaxialMaterial('Hysteretic', 220, My81, setay81, Mp81, setap81, Mp81, tensetap81, My81ne, setay81ne, Mp81ne, setap81ne, Mp81ne, tensetap81ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap82 = 10*setap82
My82ne  = -1*My82
setay82ne  = -1*setay82
Mp82ne  = -1*Mp82
setap82ne  = -1*setap82
Mp82ne  = -1*Mp82
tensetap82ne = -1*tensetap82
op.uniaxialMaterial('Hysteretic', 221, My82, setay82, Mp82, setap82, Mp82, tensetap82, My82ne, setay82ne, Mp82ne, setap82ne, Mp82ne, tensetap82ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap83 = 10*setap83
My83ne  = -1*My83
setay83ne  = -1*setay83
Mp83ne  = -1*Mp83
setap83ne  = -1*setap83
Mp83ne  = -1*Mp83
tensetap83ne = -1*tensetap83
op.uniaxialMaterial('Hysteretic', 222, My83, setay83, Mp83, setap83, Mp83, tensetap83, My83ne, setay83ne, Mp83ne, setap83ne, Mp83ne, tensetap83ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap84 = 10*setap84
My84ne  = -1*My84
setay84ne  = -1*setay84
Mp84ne  = -1*Mp84
setap84ne  = -1*setap84
Mp84ne  = -1*Mp84
tensetap84ne = -1*tensetap84
op.uniaxialMaterial('Hysteretic', 223, My84, setay84, Mp84, setap84, Mp84, tensetap84, My84ne, setay84ne, Mp84ne, setap84ne, Mp84ne, tensetap84ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap85 = 10*setap85
My85ne  = -1*My85
setay85ne  = -1*setay85
Mp85ne  = -1*Mp85
setap85ne  = -1*setap85
Mp85ne  = -1*Mp85
tensetap85ne = -1*tensetap85
op.uniaxialMaterial('Hysteretic', 224, My85, setay85, Mp85, setap85, Mp85, tensetap85, My85ne, setay85ne, Mp85ne, setap85ne, Mp85ne, tensetap85ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap86 = 10*setap86
My86ne  = -1*My86
setay86ne  = -1*setay86
Mp86ne  = -1*Mp86
setap86ne  = -1*setap86
Mp86ne  = -1*Mp86
tensetap86ne = -1*tensetap86
op.uniaxialMaterial('Hysteretic', 225, My86, setay86, Mp86, setap86, Mp86, tensetap86, My86ne, setay86ne, Mp86ne, setap86ne, Mp86ne, tensetap86ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap87 = 10*setap87
My87ne  = -1*My87
setay87ne  = -1*setay87
Mp87ne  = -1*Mp87
setap87ne  = -1*setap87
Mp87ne  = -1*Mp87
tensetap87ne = -1*tensetap87
op.uniaxialMaterial('Hysteretic', 226, My87, setay87, Mp87, setap87, Mp87, tensetap87, My87ne, setay87ne, Mp87ne, setap87ne, Mp87ne, tensetap87ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap88 = 10*setap88
My88ne  = -1*My88
setay88ne  = -1*setay88
Mp88ne  = -1*Mp88
setap88ne  = -1*setap88
Mp88ne  = -1*Mp88
tensetap88ne = -1*tensetap88
op.uniaxialMaterial('Hysteretic', 227, My88, setay88, Mp88, setap88, Mp88, tensetap88, My88ne, setay88ne, Mp88ne, setap88ne, Mp88ne, tensetap88ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap89 = 10*setap89
My89ne  = -1*My89
setay89ne  = -1*setay89
Mp89ne  = -1*Mp89
setap89ne  = -1*setap89
Mp89ne  = -1*Mp89
tensetap89ne = -1*tensetap89
op.uniaxialMaterial('Hysteretic', 228, My89, setay89, Mp89, setap89, Mp89, tensetap89, My89ne, setay89ne, Mp89ne, setap89ne, Mp89ne, tensetap89ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap90 = 10*setap90
My90ne  = -1*My90
setay90ne  = -1*setay90
Mp90ne  = -1*Mp90
setap90ne  = -1*setap90
Mp90ne  = -1*Mp90
tensetap90ne = -1*tensetap90
op.uniaxialMaterial('Hysteretic', 229, My90, setay90, Mp90, setap90, Mp90, tensetap90, My90ne, setay90ne, Mp90ne, setap90ne, Mp90ne, tensetap90ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap91 = 10*setap91
My91ne  = -1*My91
setay91ne  = -1*setay91
Mp91ne  = -1*Mp91
setap91ne  = -1*setap91
Mp91ne  = -1*Mp91
tensetap91ne = -1*tensetap91
op.uniaxialMaterial('Hysteretic', 230, My91, setay91, Mp91, setap91, Mp91, tensetap91, My91ne, setay91ne, Mp91ne, setap91ne, Mp91ne, tensetap91ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap92 = 10*setap92
My92ne  = -1*My92
setay92ne  = -1*setay92
Mp92ne  = -1*Mp92
setap92ne  = -1*setap92
Mp92ne  = -1*Mp92
tensetap92ne = -1*tensetap92
op.uniaxialMaterial('Hysteretic', 231, My92, setay92, Mp92, setap92, Mp92, tensetap92, My92ne, setay92ne, Mp92ne, setap92ne, Mp92ne, tensetap92ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap93 = 10*setap93
My93ne  = -1*My93
setay93ne  = -1*setay93
Mp93ne  = -1*Mp93
setap93ne  = -1*setap93
Mp93ne  = -1*Mp93
tensetap93ne = -1*tensetap93
op.uniaxialMaterial('Hysteretic', 232, My93, setay93, Mp93, setap93, Mp93, tensetap93, My93ne, setay93ne, Mp93ne, setap93ne, Mp93ne, tensetap93ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap94 = 10*setap94
My94ne  = -1*My94
setay94ne  = -1*setay94
Mp94ne  = -1*Mp94
setap94ne  = -1*setap94
Mp94ne  = -1*Mp94
tensetap94ne = -1*tensetap94
op.uniaxialMaterial('Hysteretic', 233, My94, setay94, Mp94, setap94, Mp94, tensetap94, My94ne, setay94ne, Mp94ne, setap94ne, Mp94ne, tensetap94ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap95 = 10*setap95
My95ne  = -1*My95
setay95ne  = -1*setay95
Mp95ne  = -1*Mp95
setap95ne  = -1*setap95
Mp95ne  = -1*Mp95
tensetap95ne = -1*tensetap95
op.uniaxialMaterial('Hysteretic', 234, My95, setay95, Mp95, setap95, Mp95, tensetap95, My95ne, setay95ne, Mp95ne, setap95ne, Mp95ne, tensetap95ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap96 = 10*setap96
My96ne  = -1*My96
setay96ne  = -1*setay96
Mp96ne  = -1*Mp96
setap96ne  = -1*setap96
Mp96ne  = -1*Mp96
tensetap96ne = -1*tensetap96
op.uniaxialMaterial('Hysteretic', 235, My96, setay96, Mp96, setap96, Mp96, tensetap96, My96ne, setay96ne, Mp96ne, setap96ne, Mp96ne, tensetap96ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap97 = 10*setap97
My97ne  = -1*My97
setay97ne  = -1*setay97
Mp97ne  = -1*Mp97
setap97ne  = -1*setap97
Mp97ne  = -1*Mp97
tensetap97ne = -1*tensetap97
op.uniaxialMaterial('Hysteretic', 236, My97, setay97, Mp97, setap97, Mp97, tensetap97, My97ne, setay97ne, Mp97ne, setap97ne, Mp97ne, tensetap97ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap98 = 10*setap98
My98ne  = -1*My98
setay98ne  = -1*setay98
Mp98ne  = -1*Mp98
setap98ne  = -1*setap98
Mp98ne  = -1*Mp98
tensetap98ne = -1*tensetap98
op.uniaxialMaterial('Hysteretic', 237, My98, setay98, Mp98, setap98, Mp98, tensetap98, My98ne, setay98ne, Mp98ne, setap98ne, Mp98ne, tensetap98ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap99 = 10*setap99
My99ne  = -1*My99
setay99ne  = -1*setay99
Mp99ne  = -1*Mp99
setap99ne  = -1*setap99
Mp99ne  = -1*Mp99
tensetap99ne = -1*tensetap99
op.uniaxialMaterial('Hysteretic', 238, My99, setay99, Mp99, setap99, Mp99, tensetap99, My99ne, setay99ne, Mp99ne, setap99ne, Mp99ne, tensetap99ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap100 = 10*setap100
My100ne  = -1*My100
setay100ne  = -1*setay100
Mp100ne  = -1*Mp100
setap100ne  = -1*setap100
Mp100ne  = -1*Mp100
tensetap100ne = -1*tensetap100
op.uniaxialMaterial('Hysteretic', 239, My100, setay100, Mp100, setap100, Mp100, tensetap100, My100ne, setay100ne, Mp100ne, setap100ne, Mp100ne, tensetap100ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap101 = 10*setap101
My101ne  = -1*My101
setay101ne  = -1*setay101
Mp101ne  = -1*Mp101
setap101ne  = -1*setap101
Mp101ne  = -1*Mp101
tensetap101ne = -1*tensetap101
op.uniaxialMaterial('Hysteretic', 240, My101, setay101, Mp101, setap101, Mp101, tensetap101, My101ne, setay101ne, Mp101ne, setap101ne, Mp101ne, tensetap101ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap102 = 10*setap102
My102ne  = -1*My102
setay102ne  = -1*setay102
Mp102ne  = -1*Mp102
setap102ne  = -1*setap102
Mp102ne  = -1*Mp102
tensetap102ne = -1*tensetap102
op.uniaxialMaterial('Hysteretic', 241, My102, setay102, Mp102, setap102, Mp102, tensetap102, My102ne, setay102ne, Mp102ne, setap102ne, Mp102ne, tensetap102ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap103 = 10*setap103
My103ne  = -1*My103
setay103ne  = -1*setay103
Mp103ne  = -1*Mp103
setap103ne  = -1*setap103
Mp103ne  = -1*Mp103
tensetap103ne = -1*tensetap103
op.uniaxialMaterial('Hysteretic', 242, My103, setay103, Mp103, setap103, Mp103, tensetap103, My103ne, setay103ne, Mp103ne, setap103ne, Mp103ne, tensetap103ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap104 = 10*setap104
My104ne  = -1*My104
setay104ne  = -1*setay104
Mp104ne  = -1*Mp104
setap104ne  = -1*setap104
Mp104ne  = -1*Mp104
tensetap104ne = -1*tensetap104
op.uniaxialMaterial('Hysteretic', 243, My104, setay104, Mp104, setap104, Mp104, tensetap104, My104ne, setay104ne, Mp104ne, setap104ne, Mp104ne, tensetap104ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap105 = 10*setap105
My105ne  = -1*My105
setay105ne  = -1*setay105
Mp105ne  = -1*Mp105
setap105ne  = -1*setap105
Mp105ne  = -1*Mp105
tensetap105ne = -1*tensetap105
op.uniaxialMaterial('Hysteretic', 244, My105, setay105, Mp105, setap105, Mp105, tensetap105, My105ne, setay105ne, Mp105ne, setap105ne, Mp105ne, tensetap105ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap106 = 10*setap106
My106ne  = -1*My106
setay106ne  = -1*setay106
Mp106ne  = -1*Mp106
setap106ne  = -1*setap106
Mp106ne  = -1*Mp106
tensetap106ne = -1*tensetap106
op.uniaxialMaterial('Hysteretic', 245, My106, setay106, Mp106, setap106, Mp106, tensetap106, My106ne, setay106ne, Mp106ne, setap106ne, Mp106ne, tensetap106ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap107 = 10*setap107
My107ne  = -1*My107
setay107ne  = -1*setay107
Mp107ne  = -1*Mp107
setap107ne  = -1*setap107
Mp107ne  = -1*Mp107
tensetap107ne = -1*tensetap107
op.uniaxialMaterial('Hysteretic', 246, My107, setay107, Mp107, setap107, Mp107, tensetap107, My107ne, setay107ne, Mp107ne, setap107ne, Mp107ne, tensetap107ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap108 = 10*setap108
My108ne  = -1*My108
setay108ne  = -1*setay108
Mp108ne  = -1*Mp108
setap108ne  = -1*setap108
Mp108ne  = -1*Mp108
tensetap108ne = -1*tensetap108
op.uniaxialMaterial('Hysteretic', 247, My108, setay108, Mp108, setap108, Mp108, tensetap108, My108ne, setay108ne, Mp108ne, setap108ne, Mp108ne, tensetap108ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap109 = 10*setap109
My109ne  = -1*My109
setay109ne  = -1*setay109
Mp109ne  = -1*Mp109
setap109ne  = -1*setap109
Mp109ne  = -1*Mp109
tensetap109ne = -1*tensetap109
op.uniaxialMaterial('Hysteretic', 248, My109, setay109, Mp109, setap109, Mp109, tensetap109, My109ne, setay109ne, Mp109ne, setap109ne, Mp109ne, tensetap109ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap110 = 10*setap110
My110ne  = -1*My110
setay110ne  = -1*setay110
Mp110ne  = -1*Mp110
setap110ne  = -1*setap110
Mp110ne  = -1*Mp110
tensetap110ne = -1*tensetap110
op.uniaxialMaterial('Hysteretic', 249, My110, setay110, Mp110, setap110, Mp110, tensetap110, My110ne, setay110ne, Mp110ne, setap110ne, Mp110ne, tensetap110ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap111 = 10*setap111
My111ne  = -1*My111
setay111ne  = -1*setay111
Mp111ne  = -1*Mp111
setap111ne  = -1*setap111
Mp111ne  = -1*Mp111
tensetap111ne = -1*tensetap111
op.uniaxialMaterial('Hysteretic', 250, My111, setay111, Mp111, setap111, Mp111, tensetap111, My111ne, setay111ne, Mp111ne, setap111ne, Mp111ne, tensetap111ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap112 = 10*setap112
My112ne  = -1*My112
setay112ne  = -1*setay112
Mp112ne  = -1*Mp112
setap112ne  = -1*setap112
Mp112ne  = -1*Mp112
tensetap112ne = -1*tensetap112
op.uniaxialMaterial('Hysteretic', 251, My112, setay112, Mp112, setap112, Mp112, tensetap112, My112ne, setay112ne, Mp112ne, setap112ne, Mp112ne, tensetap112ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap113 = 10*setap113
My113ne  = -1*My113
setay113ne  = -1*setay113
Mp113ne  = -1*Mp113
setap113ne  = -1*setap113
Mp113ne  = -1*Mp113
tensetap113ne = -1*tensetap113
op.uniaxialMaterial('Hysteretic', 252, My113, setay113, Mp113, setap113, Mp113, tensetap113, My113ne, setay113ne, Mp113ne, setap113ne, Mp113ne, tensetap113ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap114 = 10*setap114
My114ne  = -1*My114
setay114ne  = -1*setay114
Mp114ne  = -1*Mp114
setap114ne  = -1*setap114
Mp114ne  = -1*Mp114
tensetap114ne = -1*tensetap114
op.uniaxialMaterial('Hysteretic', 253, My114, setay114, Mp114, setap114, Mp114, tensetap114, My114ne, setay114ne, Mp114ne, setap114ne, Mp114ne, tensetap114ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap115 = 10*setap115
My115ne  = -1*My115
setay115ne  = -1*setay115
Mp115ne  = -1*Mp115
setap115ne  = -1*setap115
Mp115ne  = -1*Mp115
tensetap115ne = -1*tensetap115
op.uniaxialMaterial('Hysteretic', 254, My115, setay115, Mp115, setap115, Mp115, tensetap115, My115ne, setay115ne, Mp115ne, setap115ne, Mp115ne, tensetap115ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap116 = 10*setap116
My116ne  = -1*My116
setay116ne  = -1*setay116
Mp116ne  = -1*Mp116
setap116ne  = -1*setap116
Mp116ne  = -1*Mp116
tensetap116ne = -1*tensetap116
op.uniaxialMaterial('Hysteretic', 255, My116, setay116, Mp116, setap116, Mp116, tensetap116, My116ne, setay116ne, Mp116ne, setap116ne, Mp116ne, tensetap116ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap117 = 10*setap117
My117ne  = -1*My117
setay117ne  = -1*setay117
Mp117ne  = -1*Mp117
setap117ne  = -1*setap117
Mp117ne  = -1*Mp117
tensetap117ne = -1*tensetap117
op.uniaxialMaterial('Hysteretic', 256, My117, setay117, Mp117, setap117, Mp117, tensetap117, My117ne, setay117ne, Mp117ne, setap117ne, Mp117ne, tensetap117ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap118 = 10*setap118
My118ne  = -1*My118
setay118ne  = -1*setay118
Mp118ne  = -1*Mp118
setap118ne  = -1*setap118
Mp118ne  = -1*Mp118
tensetap118ne = -1*tensetap118
op.uniaxialMaterial('Hysteretic', 257, My118, setay118, Mp118, setap118, Mp118, tensetap118, My118ne, setay118ne, Mp118ne, setap118ne, Mp118ne, tensetap118ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap119 = 10*setap119
My119ne  = -1*My119
setay119ne  = -1*setay119
Mp119ne  = -1*Mp119
setap119ne  = -1*setap119
Mp119ne  = -1*Mp119
tensetap119ne = -1*tensetap119
op.uniaxialMaterial('Hysteretic', 258, My119, setay119, Mp119, setap119, Mp119, tensetap119, My119ne, setay119ne, Mp119ne, setap119ne, Mp119ne, tensetap119ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap120 = 10*setap120
My120ne  = -1*My120
setay120ne  = -1*setay120
Mp120ne  = -1*Mp120
setap120ne  = -1*setap120
Mp120ne  = -1*Mp120
tensetap120ne = -1*tensetap120
op.uniaxialMaterial('Hysteretic', 259, My120, setay120, Mp120, setap120, Mp120, tensetap120, My120ne, setay120ne, Mp120ne, setap120ne, Mp120ne, tensetap120ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap121 = 10*setap121
My121ne  = -1*My121
setay121ne  = -1*setay121
Mp121ne  = -1*Mp121
setap121ne  = -1*setap121
Mp121ne  = -1*Mp121
tensetap121ne = -1*tensetap121
op.uniaxialMaterial('Hysteretic', 260, My121, setay121, Mp121, setap121, Mp121, tensetap121, My121ne, setay121ne, Mp121ne, setap121ne, Mp121ne, tensetap121ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap122 = 10*setap122
My122ne  = -1*My122
setay122ne  = -1*setay122
Mp122ne  = -1*Mp122
setap122ne  = -1*setap122
Mp122ne  = -1*Mp122
tensetap122ne = -1*tensetap122
op.uniaxialMaterial('Hysteretic', 261, My122, setay122, Mp122, setap122, Mp122, tensetap122, My122ne, setay122ne, Mp122ne, setap122ne, Mp122ne, tensetap122ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap123 = 10*setap123
My123ne  = -1*My123
setay123ne  = -1*setay123
Mp123ne  = -1*Mp123
setap123ne  = -1*setap123
Mp123ne  = -1*Mp123
tensetap123ne = -1*tensetap123
op.uniaxialMaterial('Hysteretic', 262, My123, setay123, Mp123, setap123, Mp123, tensetap123, My123ne, setay123ne, Mp123ne, setap123ne, Mp123ne, tensetap123ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap124 = 10*setap124
My124ne  = -1*My124
setay124ne  = -1*setay124
Mp124ne  = -1*Mp124
setap124ne  = -1*setap124
Mp124ne  = -1*Mp124
tensetap124ne = -1*tensetap124
op.uniaxialMaterial('Hysteretic', 263, My124, setay124, Mp124, setap124, Mp124, tensetap124, My124ne, setay124ne, Mp124ne, setap124ne, Mp124ne, tensetap124ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap125 = 10*setap125
My125ne  = -1*My125
setay125ne  = -1*setay125
Mp125ne  = -1*Mp125
setap125ne  = -1*setap125
Mp125ne  = -1*Mp125
tensetap125ne = -1*tensetap125
op.uniaxialMaterial('Hysteretic', 264, My125, setay125, Mp125, setap125, Mp125, tensetap125, My125ne, setay125ne, Mp125ne, setap125ne, Mp125ne, tensetap125ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap126 = 10*setap126
My126ne  = -1*My126
setay126ne  = -1*setay126
Mp126ne  = -1*Mp126
setap126ne  = -1*setap126
Mp126ne  = -1*Mp126
tensetap126ne = -1*tensetap126
op.uniaxialMaterial('Hysteretic', 265, My126, setay126, Mp126, setap126, Mp126, tensetap126, My126ne, setay126ne, Mp126ne, setap126ne, Mp126ne, tensetap126ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap127 = 10*setap127
My127ne  = -1*My127
setay127ne  = -1*setay127
Mp127ne  = -1*Mp127
setap127ne  = -1*setap127
Mp127ne  = -1*Mp127
tensetap127ne = -1*tensetap127
op.uniaxialMaterial('Hysteretic', 266, My127, setay127, Mp127, setap127, Mp127, tensetap127, My127ne, setay127ne, Mp127ne, setap127ne, Mp127ne, tensetap127ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap128 = 10*setap128
My128ne  = -1*My128
setay128ne  = -1*setay128
Mp128ne  = -1*Mp128
setap128ne  = -1*setap128
Mp128ne  = -1*Mp128
tensetap128ne = -1*tensetap128
op.uniaxialMaterial('Hysteretic', 267, My128, setay128, Mp128, setap128, Mp128, tensetap128, My128ne, setay128ne, Mp128ne, setap128ne, Mp128ne, tensetap128ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap129 = 10*setap129
My129ne  = -1*My129
setay129ne  = -1*setay129
Mp129ne  = -1*Mp129
setap129ne  = -1*setap129
Mp129ne  = -1*Mp129
tensetap129ne = -1*tensetap129
op.uniaxialMaterial('Hysteretic', 268, My129, setay129, Mp129, setap129, Mp129, tensetap129, My129ne, setay129ne, Mp129ne, setap129ne, Mp129ne, tensetap129ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap130 = 10*setap130
My130ne  = -1*My130
setay130ne  = -1*setay130
Mp130ne  = -1*Mp130
setap130ne  = -1*setap130
Mp130ne  = -1*Mp130
tensetap130ne = -1*tensetap130
op.uniaxialMaterial('Hysteretic', 269, My130, setay130, Mp130, setap130, Mp130, tensetap130, My130ne, setay130ne, Mp130ne, setap130ne, Mp130ne, tensetap130ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap131 = 10*setap131
My131ne  = -1*My131
setay131ne  = -1*setay131
Mp131ne  = -1*Mp131
setap131ne  = -1*setap131
Mp131ne  = -1*Mp131
tensetap131ne = -1*tensetap131
op.uniaxialMaterial('Hysteretic', 270, My131, setay131, Mp131, setap131, Mp131, tensetap131, My131ne, setay131ne, Mp131ne, setap131ne, Mp131ne, tensetap131ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap132 = 10*setap132
My132ne  = -1*My132
setay132ne  = -1*setay132
Mp132ne  = -1*Mp132
setap132ne  = -1*setap132
Mp132ne  = -1*Mp132
tensetap132ne = -1*tensetap132
op.uniaxialMaterial('Hysteretic', 271, My132, setay132, Mp132, setap132, Mp132, tensetap132, My132ne, setay132ne, Mp132ne, setap132ne, Mp132ne, tensetap132ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap133 = 10*setap133
My133ne  = -1*My133
setay133ne  = -1*setay133
Mp133ne  = -1*Mp133
setap133ne  = -1*setap133
Mp133ne  = -1*Mp133
tensetap133ne = -1*tensetap133
op.uniaxialMaterial('Hysteretic', 272, My133, setay133, Mp133, setap133, Mp133, tensetap133, My133ne, setay133ne, Mp133ne, setap133ne, Mp133ne, tensetap133ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap134 = 10*setap134
My134ne  = -1*My134
setay134ne  = -1*setay134
Mp134ne  = -1*Mp134
setap134ne  = -1*setap134
Mp134ne  = -1*Mp134
tensetap134ne = -1*tensetap134
op.uniaxialMaterial('Hysteretic', 273, My134, setay134, Mp134, setap134, Mp134, tensetap134, My134ne, setay134ne, Mp134ne, setap134ne, Mp134ne, tensetap134ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap135 = 10*setap135
My135ne  = -1*My135
setay135ne  = -1*setay135
Mp135ne  = -1*Mp135
setap135ne  = -1*setap135
Mp135ne  = -1*Mp135
tensetap135ne = -1*tensetap135
op.uniaxialMaterial('Hysteretic', 274, My135, setay135, Mp135, setap135, Mp135, tensetap135, My135ne, setay135ne, Mp135ne, setap135ne, Mp135ne, tensetap135ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap136 = 10*setap136
My136ne  = -1*My136
setay136ne  = -1*setay136
Mp136ne  = -1*Mp136
setap136ne  = -1*setap136
Mp136ne  = -1*Mp136
tensetap136ne = -1*tensetap136
op.uniaxialMaterial('Hysteretic', 275, My136, setay136, Mp136, setap136, Mp136, tensetap136, My136ne, setay136ne, Mp136ne, setap136ne, Mp136ne, tensetap136ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap137 = 10*setap137
My137ne  = -1*My137
setay137ne  = -1*setay137
Mp137ne  = -1*Mp137
setap137ne  = -1*setap137
Mp137ne  = -1*Mp137
tensetap137ne = -1*tensetap137
op.uniaxialMaterial('Hysteretic', 276, My137, setay137, Mp137, setap137, Mp137, tensetap137, My137ne, setay137ne, Mp137ne, setap137ne, Mp137ne, tensetap137ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap138 = 10*setap138
My138ne  = -1*My138
setay138ne  = -1*setay138
Mp138ne  = -1*Mp138
setap138ne  = -1*setap138
Mp138ne  = -1*Mp138
tensetap138ne = -1*tensetap138
op.uniaxialMaterial('Hysteretic', 277, My138, setay138, Mp138, setap138, Mp138, tensetap138, My138ne, setay138ne, Mp138ne, setap138ne, Mp138ne, tensetap138ne, 1.0, 1.0, 0.0, 0.0) 
 
tensetap139 = 10*setap139
My139ne  = -1*My139
setay139ne  = -1*setay139
Mp139ne  = -1*Mp139
setap139ne  = -1*setap139
Mp139ne  = -1*Mp139
tensetap139ne = -1*tensetap139
op.uniaxialMaterial('Hysteretic', 278, My139, setay139, Mp139, setap139, Mp139, tensetap139, My139ne, setay139ne, Mp139ne, setap139ne, Mp139ne, tensetap139ne, 1.0, 1.0, 0.0, 0.0) 
 
 
# Define bing spring elements
op.element('twoNodeLink', 2221, 10, 11, '-mat', 11111, 11111, 140, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2222, 11, 12, '-mat', 11111, 11111, 141, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2223, 12, 13, '-mat', 11111, 11111, 142, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2224, 13, 14, '-mat', 11111, 11111, 143, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2225, 14, 15, '-mat', 11111, 11111, 144, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2226, 15, 16, '-mat', 11111, 11111, 145, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2227, 16, 17, '-mat', 11111, 11111, 146, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2228, 17, 18, '-mat', 11111, 11111, 147, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 2229, 18, 19, '-mat', 11111, 11111, 148, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22210, 19, 110, '-mat', 11111, 11111, 149, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22211, 110, 111, '-mat', 11111, 11111, 150, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22212, 111, 112, '-mat', 11111, 11111, 151, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22213, 112, 113, '-mat', 11111, 11111, 152, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22214, 113, 114, '-mat', 11111, 11111, 153, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22215, 114, 115, '-mat', 11111, 11111, 154, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22216, 115, 116, '-mat', 11111, 11111, 155, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22217, 116, 117, '-mat', 11111, 11111, 156, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22218, 117, 118, '-mat', 11111, 11111, 157, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22219, 118, 119, '-mat', 11111, 11111, 158, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22220, 119, 120, '-mat', 11111, 11111, 159, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22221, 120, 121, '-mat', 11111, 11111, 160, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22222, 121, 122, '-mat', 11111, 11111, 161, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22223, 122, 123, '-mat', 11111, 11111, 162, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22224, 123, 124, '-mat', 11111, 11111, 163, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22225, 124, 125, '-mat', 11111, 11111, 164, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22226, 125, 126, '-mat', 11111, 11111, 165, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22227, 126, 127, '-mat', 11111, 11111, 166, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22228, 127, 128, '-mat', 11111, 11111, 167, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22229, 128, 129, '-mat', 11111, 11111, 168, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22230, 129, 130, '-mat', 11111, 11111, 169, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22231, 130, 131, '-mat', 11111, 11111, 170, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22232, 131, 132, '-mat', 11111, 11111, 171, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22233, 132, 133, '-mat', 11111, 11111, 172, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22234, 133, 134, '-mat', 11111, 11111, 173, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22235, 134, 135, '-mat', 11111, 11111, 174, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22236, 135, 136, '-mat', 11111, 11111, 175, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22237, 136, 137, '-mat', 11111, 11111, 176, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22238, 137, 138, '-mat', 11111, 11111, 177, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22239, 138, 139, '-mat', 11111, 11111, 178, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22240, 139, 140, '-mat', 11111, 11111, 179, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22241, 140, 141, '-mat', 11111, 11111, 180, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22242, 141, 142, '-mat', 11111, 11111, 181, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22243, 142, 143, '-mat', 11111, 11111, 182, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22244, 143, 144, '-mat', 11111, 11111, 183, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22245, 144, 145, '-mat', 11111, 11111, 184, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22246, 145, 146, '-mat', 11111, 11111, 185, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22247, 146, 147, '-mat', 11111, 11111, 186, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22248, 147, 148, '-mat', 11111, 11111, 187, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22249, 148, 149, '-mat', 11111, 11111, 188, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22250, 149, 150, '-mat', 11111, 11111, 189, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22251, 150, 151, '-mat', 11111, 11111, 190, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22252, 151, 152, '-mat', 11111, 11111, 191, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22253, 152, 153, '-mat', 11111, 11111, 192, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22254, 153, 154, '-mat', 11111, 11111, 193, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22255, 154, 155, '-mat', 11111, 11111, 194, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22256, 155, 156, '-mat', 11111, 11111, 195, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22257, 156, 157, '-mat', 11111, 11111, 196, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22258, 157, 158, '-mat', 11111, 11111, 197, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22259, 158, 159, '-mat', 11111, 11111, 198, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22260, 159, 160, '-mat', 11111, 11111, 199, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22261, 160, 161, '-mat', 11111, 11111, 200, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22262, 161, 162, '-mat', 11111, 11111, 201, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22263, 162, 163, '-mat', 11111, 11111, 202, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22264, 163, 164, '-mat', 11111, 11111, 203, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22265, 164, 165, '-mat', 11111, 11111, 204, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22266, 165, 166, '-mat', 11111, 11111, 205, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22267, 166, 167, '-mat', 11111, 11111, 206, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22268, 167, 168, '-mat', 11111, 11111, 207, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22269, 168, 169, '-mat', 11111, 11111, 208, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22270, 169, 170, '-mat', 11111, 11111, 209, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22271, 170, 171, '-mat', 11111, 11111, 210, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22272, 171, 172, '-mat', 11111, 11111, 211, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22273, 172, 173, '-mat', 11111, 11111, 212, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22274, 173, 174, '-mat', 11111, 11111, 213, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22275, 174, 175, '-mat', 11111, 11111, 214, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22276, 175, 176, '-mat', 11111, 11111, 215, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22277, 176, 177, '-mat', 11111, 11111, 216, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22278, 177, 178, '-mat', 11111, 11111, 217, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22279, 178, 179, '-mat', 11111, 11111, 218, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22280, 179, 180, '-mat', 11111, 11111, 219, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22281, 180, 181, '-mat', 11111, 11111, 220, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22282, 181, 182, '-mat', 11111, 11111, 221, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22283, 182, 183, '-mat', 11111, 11111, 222, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22284, 183, 184, '-mat', 11111, 11111, 223, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22285, 184, 185, '-mat', 11111, 11111, 224, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22286, 185, 186, '-mat', 11111, 11111, 225, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22287, 186, 187, '-mat', 11111, 11111, 226, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22288, 187, 188, '-mat', 11111, 11111, 227, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22289, 188, 189, '-mat', 11111, 11111, 228, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22290, 189, 190, '-mat', 11111, 11111, 229, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22291, 190, 191, '-mat', 11111, 11111, 230, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22292, 191, 192, '-mat', 11111, 11111, 231, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22293, 192, 193, '-mat', 11111, 11111, 232, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22294, 193, 194, '-mat', 11111, 11111, 233, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22295, 194, 195, '-mat', 11111, 11111, 234, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22296, 195, 196, '-mat', 11111, 11111, 235, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22297, 196, 197, '-mat', 11111, 11111, 236, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22298, 197, 198, '-mat', 11111, 11111, 237, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 22299, 198, 199, '-mat', 11111, 11111, 238, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222100, 199, 1100, '-mat', 11111, 11111, 239, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222101, 1100, 1101, '-mat', 11111, 11111, 240, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222102, 1101, 1102, '-mat', 11111, 11111, 241, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222103, 1102, 1103, '-mat', 11111, 11111, 242, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222104, 1103, 1104, '-mat', 11111, 11111, 243, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222105, 1104, 1105, '-mat', 11111, 11111, 244, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222106, 1105, 1106, '-mat', 11111, 11111, 245, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222107, 1106, 1107, '-mat', 11111, 11111, 246, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222108, 1107, 1108, '-mat', 11111, 11111, 247, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222109, 1108, 1109, '-mat', 11111, 11111, 248, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222110, 1109, 1110, '-mat', 11111, 11111, 249, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222111, 1110, 1111, '-mat', 11111, 11111, 250, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222112, 1111, 1112, '-mat', 11111, 11111, 251, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222113, 1112, 1113, '-mat', 11111, 11111, 252, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222114, 1113, 1114, '-mat', 11111, 11111, 253, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222115, 1114, 1115, '-mat', 11111, 11111, 254, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222116, 1115, 1116, '-mat', 11111, 11111, 255, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222117, 1116, 1117, '-mat', 11111, 11111, 256, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222118, 1117, 1118, '-mat', 11111, 11111, 257, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222119, 1118, 1119, '-mat', 11111, 11111, 258, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222120, 1119, 1120, '-mat', 11111, 11111, 259, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222121, 1120, 1121, '-mat', 11111, 11111, 260, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222122, 1121, 1122, '-mat', 11111, 11111, 261, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222123, 1122, 1123, '-mat', 11111, 11111, 262, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222124, 1123, 1124, '-mat', 11111, 11111, 263, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222125, 1124, 1125, '-mat', 11111, 11111, 264, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222126, 1125, 1126, '-mat', 11111, 11111, 265, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222127, 1126, 1127, '-mat', 11111, 11111, 266, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222128, 1127, 1128, '-mat', 11111, 11111, 267, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222129, 1128, 1129, '-mat', 11111, 11111, 268, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222130, 1129, 1130, '-mat', 11111, 11111, 269, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222131, 1130, 1131, '-mat', 11111, 11111, 270, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222132, 1131, 1132, '-mat', 11111, 11111, 271, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222133, 1132, 1133, '-mat', 11111, 11111, 272, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222134, 1133, 1134, '-mat', 11111, 11111, 273, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222135, 1134, 1135, '-mat', 11111, 11111, 274, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222136, 1135, 1136, '-mat', 11111, 11111, 275, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222137, 1136, 1137, '-mat', 11111, 11111, 276, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222138, 1137, 1138, '-mat', 11111, 11111, 277, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
op.element('twoNodeLink', 222139, 1138, 1139, '-mat', 11111, 11111, 278, '-dir', 1, 2, 3, '-pDelta', 0.5, 0.5, '-doRayleigh', 1)
 