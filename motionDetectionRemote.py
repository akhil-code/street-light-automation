import cv2,time,urllib,sys
import numpy as np

#functions
def camread(host):
    stream=urllib.urlopen(host)
    bytes=''
    while True:
        bytes+=stream.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),-1)
            return i


#main code
host = "192.168.43.1:8080"
if len(sys.argv)>1:
    host = sys.argv[1]
host = 'http://' + host + '/video'
print 'Streaming ' + host

#source image
simg = 0
#first instant of source image
for x in range(10):
    simg = camread(host)
    cv2.waitKey(10)

timeBegin = time.time()
while True:
    if time.time()-timeBegin > 3:
        timeBegin = time.time()
        simg = camread(host)
        cv2.waitKey(10)

    img = camread(host)

    sgray=cv2.cvtColor(simg,cv2.COLOR_BGR2GRAY)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    d = cv2.absdiff(sgray,gray)
    ret,l=cv2.threshold(d,25,255,cv2.THRESH_BINARY)

    l = cv2.erode(l,None,iterations=2)

    cnts, h = cv2.findContours(l.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        if cv2.contourArea(c)<400 :
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,200,0),2)

    cv2.imshow('img',img)
    cv2.waitKey(10)


cv2.destroyAllWindows()
