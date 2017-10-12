import cv2

cam=cv2.VideoCapture(0)
s=False
img=0
while s==False:
    s,simg=cam.read()

while s:
    s,img=cam.read()
    sgray=cv2.cvtColor(simg,cv2.COLOR_BGR2GRAY)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    d=cv2.absdiff(sgray,gray)
    ret,l=cv2.threshold(d,25,255,cv2.THRESH_BINARY)

    l = cv2.erode(l,None,iterations=2)
    cnts,h = cv2.findContours(l.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        if cv2.contourArea(c)<5500 :
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,200,0),2)
    cv2.imshow('img',img)
    key=cv2.waitKey(10)
    if key==27:
        cv2.destroyAllWindows()
        break
print 1
