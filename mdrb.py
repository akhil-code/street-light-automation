import cv2,urllib,sys,math
import numpy as np

#CLASSES
class Blob:
    area = 0
    width = height = 0
    currentContour = 0
    currentBoundingRect = 0
    centerPositions = []
    dblCurrentDiagonalSize = 0.0
    dblCurrentAspectRatio = 0.0
    blnCurrentMatchFoundOrNewBlob = False
    blnStillBeingTracked = False
    intNumOfConsecutiveFramesWithoutAMatch = 0
    predictedNextPosition = 0


    #functions
    # def __del__(self):
        # del self.centerPositions[:]

    def __init__(self, _contour):
        self.currentContour = _contour
        self.currentBoundingRect = cv2.boundingRect(self.currentContour)  #x,y,w,h
        x = (self.currentBoundingRect[0] + self.currentBoundingRect[0] + self.currentBoundingRect[2])/2
        y = (self.currentBoundingRect[1] + self.currentBoundingRect[1] + self.currentBoundingRect[3]) / 2
        currentCenter = (x,y)
        self.width = self.currentBoundingRect[2]
        self.height =  self.currentBoundingRect[3]
        self.area = self.currentBoundingRect[2] * self.currentBoundingRect[3]

        self.centerPositions.append(currentCenter)

        self.dblCurrentDiagonalSize = math.sqrt(math.pow(self.currentBoundingRect[2], 2) + math.pow(self.currentBoundingRect[3], 2));
        self.dblCurrentAspectRatio = float(self.currentBoundingRect[2])/float(self.currentBoundingRect[3])

        blnStillBeingTracked = True;
        blnCurrentMatchFoundOrNewBlob = True;

        intNumOfConsecutiveFramesWithoutAMatch = 0;

    def printInfo(self):
        print 'area: '+str(self.area)+' h: '+ str(self.height)+' w: ' \
        +str(self.width)+' Pos: '+str(self.centerPositions)+' ratio: ' \
        +str(self.dblCurrentAspectRatio)

    def predictNextPosition(self):
        numPositions = int(self.self.centerPositions.size())

        if (numPositions == 1):
            predictedNextPosition[0] = self.self.centerPositions[-1][0]
            predictedNextPosition[1] = self.centerPositions[-1][1]

        elif (numPositions == 2):
            deltaX = self.centerPositions[1][0] - self.centerPositions[0][0]
            deltaY = self.centerPositions[1][1] - self.centerPositions[0][1]

            predictedNextPosition[0] = self.centerPositions[-1][0] + deltaX
            predictedNextPosition[1] = self.centerPositions[-1][1] + deltaY

        elif (numPositions == 3):
            sumOfXChanges = ((self.centerPositions[2][0] - self.centerPositions[1][1]) * 2) + \
            ((self.centerPositions[1][0] - self.centerPositions[0][0]) * 1)

            deltaX = int(round(float(sumOfXChanges)/3.0))

            sumOfYChanges = ((self.centerPositions[2][1] - self.centerPositions[1][1]) * 2) + \
            ((self.centerPositions[1][1] - self.centerPositions[0][1]) * 1)

            deltaY = int(round(float(sumOfYChanges) / 3.0))

            predictedNextPosition[0] = self.centerPositions[-1][0] + deltaX
            predictedNextPosition[1] = self.centerPositions[-1][1] + deltaY

        elif (numPositions == 4) :
            sumOfXChanges = ((self.centerPositions[3][0] - self.centerPositions[2][0]) * 3) + \
            ((self.centerPositions[2][0] - self.centerPositions[1][0]) * 2) + \
            ((self.centerPositions[1][0] - self.centerPositions[0][0]) * 1)

            deltaX = int(round(float(sumOfXChanges) / 6.0))

            sumOfYChanges = ((self.centerPositions[3][1] - self.centerPositions[2][1]) * 3) + \
            ((self.centerPositions[2][1] - self.centerPositions[1][1]) * 2) + \
            ((self.centerPositions[1][1] - self.centerPositions[0][1]) * 1)

            deltaY = int(round(float(sumOfYChanges) / 6.0))

            predictedNextPosition[0] = self.centerPositions[-1][0] + deltaX;
            predictedNextPosition[1] = self.centerPositions[-1][1] + deltaY;

        elif (numPositions >= 5):
            sumOfXChanges = ((self.centerPositions[numPositions - 1][0] - self.centerPositions[numPositions - 2][0]) * 4) + \
            ((self.centerPositions[numPositions - 2][0] - self.centerPositions[numPositions - 3][0]) * 3) + \
            ((self.centerPositions[numPositions - 3][0] - self.centerPositions[numPositions - 4][0]) * 2) + \
            ((self.centerPositions[numPositions - 4][0] - self.centerPositions[numPositions - 5][0]) * 1)

            deltaX = int(round(float(sumOfXChanges) / 10.0));

            sumOfYChanges = ((self.centerPositions[numPositions - 1][1] - self.centerPositions[numPositions - 2][1]) * 4) + \
            ((self.centerPositions[numPositions - 2][1] - self.centerPositions[numPositions - 3][1]) * 3) + \
            ((self.centerPositions[numPositions - 3][1] - self.centerPositions[numPositions - 4][1]) * 2) + \
            ((self.centerPositions[numPositions - 4][1] - self.centerPositions[numPositions - 5][1]) * 1)

            deltaY = int(round(float(sumOfYChanges) / 10.0))

            predictedNextPosition[0] = self.centerPositions[-1][0] + deltaX;
            predictedNextPosition[1] = self.centerPositions[-1][1] + deltaY;

        else:
            #should never get here
            pass

    def matchCurrentFrameBlobsToExistingBlobs(self):
        pass
    def addBlobToExistingBlobs(self):
        pass
    def addNewBlob(self):
        pass
    def distanceBetweenPoints(self):
        pass


#FUNCTIONS
def drawBlobInfoOnImage(blobs,imgFrame2Copy):
    for i in range(len(blobs)):
        # if (blobs[i].blnStillBeingTracked == True):
        rect_corner1 = (blobs[i].currentBoundingRect[0],blobs[i].currentBoundingRect[1])
        rect_corner2 = (blobs[i].currentBoundingRect[0]+blobs[i].width, blobs[i].currentBoundingRect[1]+blobs[i].height)
        imgFrame2Copy = cv2.rectangle(imgFrame2Copy, rect_corner1,rect_corner2, (0,0,255))

        intFontFace = cv2.FONT_HERSHEY_SIMPLEX;
        dblFontScale = blobs[i].dblCurrentDiagonalSize / 60.0
        intFontThickness = int(round(dblFontScale * 1.0))
        # print len(blobs[i].centerPositions)
        cv2.putText(imgFrame2Copy,str(i), blobs[i].centerPositions[-1], intFontFace, dblFontScale, (0,255,0), intFontThickness);

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

def drawAndShowContours(imageSize,contours,strImageName):
    image = np.zeros(imageSize, dtype=np.uint8)
    cv2.drawContours(image, contours, -1,(255,255,255), -1)
    cv2.imshow(strImageName, image);






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

    # cv2.imshow("imgThresh",imgThresh)

    #applying morphological operations dilation and erosion
    kernel = np.ones((5,5),np.uint8)
    imgThresh = cv2.dilate(imgThresh,kernel,iterations = 1)
    imgThresh = cv2.dilate(imgThresh,kernel,iterations = 1)
    imgThresh = cv2.erode(imgThresh,kernel,iterations = 1)


    #finding contours of the thresholded image
    contours, hierarchy = cv2.findContours(imgThresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #drawing contours
    # drawAndShowContours(imgThresh.shape,contours,"contours")

    # cv2.imshow("imgContours",imgContours)

    #finding and drawing convex hulls
    hulls = []  #used to store hulls
    for cnt in contours:
        hulls.append(cv2.convexHull(cnt))

    drawAndShowContours(imgThresh.shape,hulls,"convexHulls")

    #Blob validation
    currentFrameBlobs = []
    blobs = []
    for hull in hulls:
        possibleBlob = Blob(hull)

        if (possibleBlob.area > 100 and \
        possibleBlob.dblCurrentAspectRatio >= 0.2 and \
        possibleBlob.dblCurrentAspectRatio <= 1.75 and \
        possibleBlob.width > 20 and \
        possibleBlob.height > 20 and \
        possibleBlob.dblCurrentDiagonalSize > 30.0 and \
        (cv2.contourArea(possibleBlob.currentContour) / float(possibleBlob.area)) > 0.40):
            currentFrameBlobs.append(hull)
            blobs.append(possibleBlob)

        del possibleBlob

    imgFrame1 = imgFrame2.copy()

    # print len(currentFrameBlobs)
    if(len(currentFrameBlobs) > 0):
        drawAndShowContours(imgThresh.shape,contours,"convexHulls")
        drawBlobInfoOnImage(blobs,imgFrame2)

    cv2.imshow("output",imgFrame2)
    cv2.waitKey(10)
    del blobs[:]
    del currentFrameBlobs[:]
