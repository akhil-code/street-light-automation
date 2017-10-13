import cv2,urllib,sys
import numpy as np

#CLASSES
class Blob:
    currentContour = 0
    currentBoundingRect = 0
    centerPositions = 0
    dblCurrentDiagonalSize = 0
    dblCurrentAspectRatio = 0
    blnCurrentMatchFoundOrNewBlob = 0
    blnStillBeingTracked = 0
    intNumOfConsecutiveFramesWithoutAMatch = 0
    predictedNextPosition = 0

    #functions
    def __init__(self, _contour):
        currentContour = _contour
        currentBoundingRect = cv2.boundingRect(currentContour)
        pass
    def predictNextPosition(self):
        pass
    def matchCurrentFrameBlobsToExistingBlobs(self):
        pass
    def addBlobToExistingBlobs(self):
        pass
    def addNewBlob(self):
        pass
    def distanceBetweenPoints(self):
        pass
    def drawAndShowContours(self):
        pass
    def drawBlobInfoOnImage(self):
        pass

#FUNCTIONS
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










#MAIN CODE

#control parameters associated with IP camera
host = "192.168.43.1:8080"
if len(sys.argv)>1:
    host = sys.argv[1]
host = 'http://' + host + '/video'
print 'Streaming ' + host

imgFrame1 = camread(host)

while True:
    #capturing two reference frames
    imgFrame2 = camread(host)

    #making duplicates of the above frames
    imgFrame1Copy = imgFrame1.copy()
    imgFrame2Copy = imgFrame2.copy()

    #changing the colorspace to grayscale
    imgFrame1Copy = cv2.cvtColor(imgFrame1Copy,cv2.COLOR_BGR2GRAY)
    imgFrame2Copy = cv2.cvtColor(imgFrame2Copy,cv2.COLOR_BGR2GRAY)

    #applying gaussianblur
    imgFrame1Copy = cv2.GaussianBlur(imgFrame1Copy,(5,5),0)
    imgFrame2Copy = cv2.GaussianBlur(imgFrame2Copy,(5,5),0)

    #finding the difference of the two frames and thresholding the diff
    imgDifference = cv2.absdiff(imgFrame1Copy,imgFrame2Copy)
    _,imgThresh = cv2.threshold(imgDifference,30,255,cv2.THRESH_BINARY)

    cv2.imshow("imgThresh",imgThresh)

    #applying morphological operations dilation and erosion
    kernel = np.ones((5,5),np.uint8)
    imgThresh = cv2.dilate(imgThresh,kernel,iterations = 1)
    imgThresh = cv2.dilate(imgThresh,kernel,iterations = 1)
    imgThresh = cv2.erode(imgThresh,kernel,iterations = 1)

    #making duplicate of the thresholded image
    imgThreshCopy = imgThresh.copy()

    #finding contours of the thresholded image
    contours, hierarchy = cv2.findContours(imgThreshCopy,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #drawing contours
    imgContours = imgThresh.copy()
    cv2.drawContours(imgContours,contours,-1,(0,255,0),3)
    cv2.imshow("imgContours",imgContours)

    #used to store convex hulls
    hulls = []
    for cnt in contours:
        hulls.append(cv2.convexHull(cnt))

    #drawing Convex hulls
    imgHulls = imgThresh.copy()
    cv2.drawContours(imgHulls,hulls,-1,(0,255,0),3)
    cv2.imshow("convexHulls",imgHulls)

    cv2.waitKey(10)
    imgFrame1 = imgFrame2.copy()
