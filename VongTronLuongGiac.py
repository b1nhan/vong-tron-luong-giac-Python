import cv2
from math import *

win=cv2.imread('background.png')
Tam=int(512/2)
BanKinh=int(202)
CountColor=0
Color=[(240,121,77),(150,101,240),(53,186,240),(78,239,63)]
clone = win.copy()
PosX=[]
PosY=[]
count = 0

def CircleDraw():
    cv2.circle(win,(Tam,Tam),(BanKinh),(32,32,32),3)    #ĐườngTròn
    cv2.line(win,(56,Tam),(456,Tam),(64,64,64),3)       #TrụcX
    cv2.circle(win,(Tam,Tam),5,(0,0,255),-1)            #Tâm

def tinhtoan(x,y):
    global BanKinh,Tam
    dodai=((x-Tam)**2+(y-Tam)**2)**(1/2)
    k=BanKinh/dodai
    if x>Tam:           #Tìm tọa độ x
        m=k*(x-Tam)+Tam
    elif x<Tam:
        m=Tam-k*(Tam-x)
    if y>Tam:           #Tìm tọa độ y
        n=k*(y-Tam)+Tam
    elif y<Tam:
        n=Tam-k*(Tam-y)
    if (m%1)>=0.5:      #Đổi thành int
        m=ceil(m)
    else:
        m=floor(m)
    if (n%1)>=0.5:
        n=ceil(n)
    else:
        n=floor(n)
        
    return m,n

def Tm(x,y):
    global BanKinh,Tam
    dodai=((x-Tam)**2+(y-Tam)**2)**(1/2)
    k=BanKinh/dodai
    if x>Tam:           #Tìm tọa độ x
        m=k*(x-Tam)+Tam
    elif x<Tam:
        m=Tam-k*(Tam-x)
    if (m%1)>=0.5:      #Đổi thành int
        m=ceil(m)
    else:
        m=floor(m)
    return m
def Tn(x,y):
    global BanKinh,Tam
    dodai=((x-Tam)**2+(y-Tam)**2)**(1/2)
    k=BanKinh/dodai
    if y>Tam:           #Tìm tọa độ y
        n=k*(y-Tam)+Tam
    elif y<Tam:
        n=Tam-k*(Tam-y)
    if (n%1)>=0.5:
        n=ceil(n)
    else:
        n=floor(n)    
    return n

def Draw(event,x,y,flags,param):
    global PosX,PosY,count,win,Tam,CountColor,Color
    if(event == cv2.EVENT_LBUTTONDOWN):
        if CountColor >= 3:
            CountColor=0
        else:
            CountColor=CountColor+1
        PosX.append(Tm(x,y))
        PosY.append(Tn(x,y))
        cv2.line(win,(Tam,Tam),(Tm(x,y),Tn(x,y)),(Color[CountColor]),3)
        cv2.line(win,(Tm(x,y),Tam),(Tm(x,y),Tn(x,y)),(204,204,204),2)
        CircleDraw()
        cv2.circle(win,((Tm(x,y)),Tam),5,(Color[CountColor]),-1)            
        count = count + 1
          
    elif event == cv2.EVENT_RBUTTONDOWN:
        win = clone.copy()
        PosX.remove(PosX[count-1])
        PosY.remove(PosY[count-1])
        count = count - 1
        CountColor=0
        for i in range (0, count):
            if CountColor >= 3:
                CountColor=0
            else:
                CountColor=CountColor+1   
            cv2.line(win, (Tam,Tam),((PosX[i]),(PosY[i])), (Color[CountColor]), 3)
            cv2.line(win,((PosX[i]),Tam),((PosX[i]),(PosY[i])),(204,204,204),2)
            CircleDraw()
            cv2.circle(win,(PosX[i],Tam),5,(Color[CountColor]),-1)            

        
    elif event== cv2.EVENT_MBUTTONDOWN:
        win=clone.copy()
        PosX=[]
        PosY=[]
        count=0
        CountColor=0
        CircleDraw()
        
cv2.namedWindow('SieuCapVipPro')
CircleDraw()
cv2.setMouseCallback('SieuCapVipPro',Draw)                   #Vẽ
while(1):
    cv2.imshow('SieuCapVipPro',win) 
    if cv2.waitKey(20) & 0xFF == 27:
        break  
cv2.destroyAllWindows()
