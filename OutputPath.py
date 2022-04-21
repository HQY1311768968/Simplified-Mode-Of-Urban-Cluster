
#  This code is for define the output path of analysis results
 
import os
import openseespy.opensees as op
import pickle
 
# Create a folder for analysis results
baseDir = os.getcwd()
dataDir = baseDir+''+'\Model-Dynamic-Output'
if not os.path.exists(dataDir):
    os.mkdir(dataDir)
EQDir = pickle.load(open('groundMotionID.dat', 'rb'))
if not os.path.exists(dataDir+''+'/755/'):
    os.mkdir(dataDir+''+'/755/')
if not os.path.exists(dataDir+''+'/755/'+''+EQDir):
    os.mkdir(dataDir+''+'/755/'+''+EQDir)
scale = pickle.load(open("scale.dat", "rb"))
scalestr = str(scale)
if not os.path.exists(dataDir+''+'/755/'+''+EQDir+''+'/'+''+scalestr):
    os.mkdir(dataDir+''+'/755/'+''+EQDir+''+'/'+''+scalestr)
# Define the output path
pathToOutFile = dataDir+''+'/755/'+''+EQDir+''+'/'+''+scalestr
 
# record natural period of vibration
periodpath = dataDir+''+'/755'
T1 = pickle.load(open("T1.dat", "rb"))
T2 = pickle.load(open("T2.dat", "rb"))
period_file = open(periodpath+''+'/Periods.txt','w')
period_file.write(str(T1)+''+'      '+''+str(T2))
period_file.close()
 
# record floor displacements	
op.recorder('Node', '-file', pathToOutFile+''+'/Disp-Story.out', '-time', '-node', 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, '-dof', 1, 'disp')
 
# record floor acceleration
GMfile = baseDir+''+'/GroundMotionAccel/'+''+EQDir+''+'.txt'
dt = pickle.load(open("groundMotiondt.dat", "rb"))
groundMotionSF = pickle.load(open("groundMotionSF.dat", "rb")) 
g = 9.8
Scalefact = float(groundMotionSF)*g
op.timeSeries('Path', 1, '-dt', float(dt), '-filePath', GMfile, '-factor', Scalefact)
op.recorder('EnvelopeNode', '-file', pathToOutFile+''+'/Accel-Story.out', '-timeSeries', 1, '-time', '-node', 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, '-dof', 1, 'accel')
 
# record floor velocity
op.recorder('EnvelopeNode', '-file', pathToOutFile+''+'/Vel-Story.out', '-time', '-node', 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, '-dof', 1, 'vel')
 