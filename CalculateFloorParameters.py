# This code is for floor parameter calculation

import os
import xlrd
import math
import pickle
import numpy as np
from numpy import linalg as LA

global StoryNumber

pi = math.pi
g = 9.8

FileDir = os.getcwd()

# Building information input
DataDir = FileDir+''+'/BuildingInformation/ZJXCbuildingsAndInformation.xlsx'
xl = xlrd.open_workbook(r'D:\1HQY\Model2D\Model_Python_OpenSeespy\OpenseespyCode\BuildingInformation\ZJXCbuildingsAndInformation.xls')
sheet1 = xl.sheet_by_index(0)

StoryNumberlist = sheet1.col_values(1)
Arealist = sheet1.col_values(2)
Perimeterlist = sheet1.col_values(3)
bound_htlist = sheet1.col_values(4)
bound_wtlist = sheet1.col_values(5)

BuildingID = pickle.load(open("BuildingID.dat", "rb"))

StoryNumber = StoryNumberlist[BuildingID-1]
StoryNumber = int(StoryNumber)
f = open('StoryNumber.dat','wb')
pickle.dump(StoryNumber, f)
f.close()
f = open('StoryNumber.dat','wb')
pickle.dump(StoryNumber, f)
f.close()
Area = Arealist[BuildingID-1]
Perimeter = Perimeterlist[BuildingID-1]
bound_ht = bound_htlist[BuildingID-1]
bound_wt = bound_wtlist[BuildingID-1]

StoryHDir = FileDir+''+'/BuildingInformation/Story_height.txt'
f = open(StoryHDir,'r')
StoryH = f.read()
StoryH = float(StoryH)

H = float(StoryH)*StoryNumber
B = min(bound_ht,bound_wt)
L = max(bound_ht,bound_wt)

if StoryNumber<9 : #Check the type of structure
    
    #Calculate the mass matrix and stiffness matrix of the structure
    m1 = 1200
    m = m1*Area
    M = np.mat(m*np.eye(StoryNumber))
    if L/B<2 :
        T1 = 0.05*StoryNumber
    else:
        T1 = 0.25+0.00053*(math.pow(H, 2))/(math.pow(B, 1/3))
        
    seta = np.mat('1 2.62 5.05 8.29 12.34 17.21 22.88 29.37')
    SK0 = 4*math.pow(pi, 2)*m*seta[0,StoryNumber-1]/(math.pow(T1, 2))
    global K
    K = np.zeros((StoryNumber,StoryNumber))
    for ii in range(1,StoryNumber) :
        K[ii-1,ii-1] = 2*SK0
        K[ii,ii-1] = -SK0
        K[ii-1,ii] = -SK0
    
    K[StoryNumber-1,StoryNumber-1] = SK0
    
    #Eigenvalue calculation
    w0,phi0 = LA.eig(M.I*K)
    w0 = np.array(w0)
    d = np.argsort(w0,0)
    w2 = w0[d]
    phi = phi0[:,d]
    w = np.sqrt(np.mat(w2))
    
    #Equivalent base shear method
    Live = 2.5*1000
    alphamaxDir = FileDir+''+'/BuildingInformation/alphamax.txt'
    f = open(alphamaxDir,'r')
    alphamax = f.read()
    alphamax = float(alphamax)
    if StoryNumber == 1:
        Geq = (m*g+Area*Live)*StoryNumber
    else:
        Geq = 0.85*(m*g+Area*Live)*StoryNumber
    ksiDir = FileDir+''+'/BuildingInformation/ksi.txt'
    f = open(ksiDir,'r')
    ksi = f.read()
    ksi = float(ksi) 
    a1 = 0.9+(0.05-ksi)/(0.3+6*ksi)
    a2 = 0.02+(0.05-ksi)/(4+32*ksi)
    if a2<0:
        a2 = 0
    a3 = 1+(0.05-ksi)/(0.08+1.6*ksi)
    if a3<0.55:
        a3=0.55
    Tg = 0.40
    T = 2*pi/w[0,0]
    if T>=0 and T<0.1:
        alpha = (a3-0.45)*alphamax/0.1*T+0.45*alphamax
    elif T>=0.1 and T<Tg:
        alpha = a3*alphamax
    elif T>=Tg and T<5*Tg:
        alpha = (Tg/T)**a1*a3*alphamax
    else:
        alpha =(a3*0.2**a1-a2*(T-5*Tg))*alphamax
    Fek = alpha*Geq

      
    # Additional seismic action on the top
    if T <= 1.4*Tg:
        detan = 0
    else:
        if Tg<=0.35:
            detan = 0.08*T+0.07
        elif Tg>0.55:
            detan = 0.08*T-0.02
        else:
            detan = 0.08*T+0.01
    
    Fi = np.zeros((1,StoryNumber))
    for ii in range(1,StoryNumber+1):
        Fii = 2*ii/(StoryNumber*(1+StoryNumber))*(1-detan)*Fek
        Fi[0,ii-1] = Fii
    detaFn = detan*Fek
    Vd = np.zeros((1,StoryNumber))
    Vi = 0
    for ii in range(1,StoryNumber+1):
        Vi = Vi+Fi[0,StoryNumber-ii]
        Vd[0,StoryNumber-ii] = Vi
    Vd[0,StoryNumber-1] = Vd[0,StoryNumber-1]+detaFn
    
    #Calculated the stiffness coefficient after yield
    eta = 0.25
    k2 = eta*SK0
    
    #Calculate the parameters of the frame line of the spring model
    Omegay = 1.10
    Omegap = 2.50
    Vy = Omegay*Vd.T
    Vp = Omegap*Vy
    uy = Vy/SK0
    up = (Vp-Vy)/k2+Vy/SK0
    
else:   #Check the type of structure
    
    #Calculate the mass matrix and stiffness matrix of the structure
    m1 = 1400
    m = m1*Area
    I = m*math.pow(StoryH, 2)
    M = np.mat(m*np.eye(2*StoryNumber))
    for ii in range(1,StoryNumber+1):
        M[2*ii-1,2*ii-1] = I
    if H<=100:
        T1 = 0.25+0.00053*math.pow(H, 2)/(math.pow(B, 1/3))
        T2 = 0.27*T1
    elif H<150:
        T1 = 0.5*(0.2+0.35)*math.pow(H, 0.5)
    elif H<250:
        T1 = 0.5*(0.25+0.4)*math.pow(H, 0.5)
    else:
        T1 = 0.4*math.pow(H, 0.5)
        
    alpha0 = 4.0458
    gamma1 = 1.9057
    RK0 = 4*math.pow(pi, 2)*m*StoryNumber*math.pow(H, 3)/(math.pow(T1, 2)*math.pow(gamma1, 2)*(math.pow(gamma1, 2)+math.pow(alpha0, 2))) #Bending stiffness parameter(V)
    SK0 = math.pow(alpha0, 2)*RK0/math.pow(H, 2) #Shear stiffness parameter(K)
    K = np.zeros((2*StoryNumber,2*StoryNumber))
    for ii in range(1,StoryNumber):
        K[2*ii-2,2*ii-2] =  2*SK0
        K[2*ii-2,2*ii-1] = -2*SK0*StoryH
        K[2*ii-2,2*ii] = -SK0
        K[2*ii-2,2*ii+1] = SK0*StoryH
        K[2*ii-1,2*ii-2] = -2*SK0*StoryH
        K[2*ii,2*ii-2] = -SK0
        K[2*ii+1,2*ii-2] = SK0*StoryH
        K[2*ii-1,2*ii-1] = 2*RK0+2*SK0*math.pow(StoryH, 2)
        K[2*ii-1,2*ii] = SK0*StoryH
        K[2*ii-1,2*ii+1] = -RK0-SK0*math.pow(StoryH, 2)
        K[2*ii,2*ii-1] = SK0*StoryH
        K[2*ii+1,2*ii-1] = -RK0-SK0*math.pow(StoryH, 2)

    K[2*StoryNumber-2,2*StoryNumber-2] = SK0
    K[2*StoryNumber-1,2*StoryNumber-2] = -SK0*StoryH
    K[2*StoryNumber-2,2*StoryNumber-1] = -SK0*StoryH
    K[2*StoryNumber-1,2*StoryNumber-1] = RK0+SK0*math.pow(StoryH, 2)
    
    #Eigenvalue calculation
    w0,phi0 = LA.eig(M.I*K)
    w0 = np.array(w0)
    d = np.argsort(w0,0)
    w2 = w0[d]
    phi = phi0[:,d]
    w = np.sqrt(np.mat(w2))
    
    #Calculate modal participation factors
    Gamma = np.zeros((1,2*StoryNumber))
    for ii in range(1,2*StoryNumber+1):
        phi = np.array(phi)
        Gamma0 = np.sum(phi[:,ii-1])/np.sum(phi[:,ii-1]**2)
        Gamma[0,ii-1] = Gamma0

    #Calculate designed response spectrum
    Live = 2.5*1000
    alphamax = 0.08
    Geq = 0.85*(m*g+Area*Live)*StoryNumber
    ksi = 0.05 #The damping ratio is set as 0.05
    b = 0.9+(0.05-ksi)/(0.3+6*ksi)
    a1 = 0.02+(0.05-ksi)/(4+32*ksi)
    if a1<0:
        a1 = 0

    a2 = 1+(0.05-ksi)/(0.08+1.6*ksi)
    if a2<0.55:
        a2=0.55

    T = 2*pi/w
    T = T.T
    Tg = 0.40
    Alpha = np.zeros((1,2*StoryNumber))
    for ii in range(1,2*StoryNumber+1):
        if T[ii-1,0]>=0 and T[ii-1,0]<0.1:
            alpha0 = (a2-0.45)*alphamax/0.1*T[ii-1,0]+0.45*alphamax
        elif T[ii-1,0]>=0.1 and T[ii-1,0]<Tg:
            alpha0 = a2*alphamax
        elif T[ii-1,0]>=Tg and T[ii-1,0]<5*Tg:
            alpha0 = (np.array(Tg/T[ii-1,0]))**b*a2*alphamax
        else:
            alpha0 =(a2*math.pow(0.2, b)-a1*(T[ii-1,0]-5*Tg))*alphamax
        Alpha[0,ii-1] = alpha0

    # Calculate spectrum displacement
    Sa = (Alpha*g).T
    T = np.array(T)
    Sd = np.multiply((T**2)/4/pi/pi,Sa) 
    
    #Calculate shear spring design shear force and bending spring design bending moment
    U = np.zeros((2*StoryNumber,2*StoryNumber))
    for ii in range(1,2*StoryNumber+1):
        Ui = Gamma[0,ii-1]*phi[:,ii-1]*Sd[ii-1,0]
        U[:,ii-1] = Ui

    uk = np.zeros((StoryNumber,2*StoryNumber))
    setak = np.zeros((StoryNumber,2*StoryNumber))
    for ii in range(1,StoryNumber+1):
        setak[ii-1,:] = U[2*ii-1,:]
        uk[ii-1,:] = U[2*ii-2,:]

    detauk = np.zeros((StoryNumber,2*StoryNumber))
    detasetak = np.zeros((StoryNumber,2*StoryNumber))
    detauk[0,:] = uk[0,:]
    detasetak[0,:] = setak[0,:]
    for ii in range(2,StoryNumber+1):
        detauk[ii-1,:] = uk[ii-1,:]-uk[ii-2,:]
        detasetak[ii-1,:] = setak[ii-1,:]-setak[ii-2,:]

    Vk = detauk*SK0/StoryH
    Mk = detasetak*RK0/StoryH
    Vk = np.array(Vk)
    Mk = np.array(Mk)
    Va = np.sqrt(np.mat(np.sum(np.multiply(Vk,Vk), axis=1))) 
    Va = Va.T
    Ma = np.sqrt(np.mat(np.sum(np.multiply(Mk,Mk), axis=1)))
    Ma = Ma.T
    Md = 1.2*Ma
    Vbase = np.sum(Va)
    Vd = np.zeros((StoryNumber,1))
    for ii in range(1,StoryNumber+1):
        Vd[ii-1,0] = max(Va[ii-1,0],0.2*Vbase)

    #Calculate the parameters of the frame line of the spring model
    Omegay = 1.57
    Omegap = 2.23
    Vy = Omegay*Vd
    My = Omegay*Md
    Vp = Omegap*Vy
    Mp = Omegap*My
    
    #Calculated the stiffness coefficient after yield
    eta = 0.25
    Pai2 = eta*RK0
    Psi2 = eta*SK0
    
#Calculate the structure shear weight ratio
lamda = Vy[0,0]/m/g/StoryNumber
    

        
        
        
        
        
        
        
        
        
        
        
        







