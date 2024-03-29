import cv2
import numpy as np
import pyautogui as pyag
from PIL import ImageGrab
from msvcrt import getch
import argparse
import imutils
import os
import time
import threading

class ScreenShot (threading.Thread):
    def __init__(self,point1x,point1y,point2x,point2y,saveOption,proto_text,caffe_model):
        threading.Thread.__init__(self)
        self.save = saveOption
        self.count = 0
        self.x1 = point1x
        self.x2 = point2x
        self.y1 = point1y
        self.y2 = point2y
        self.location = os.getcwd()+"\\Training\\Images\\"
        self.fileName = "Images"
        if os.path.isdir(os.getcwd()+"\\Training\\Images") != True:
            os.mkdir(os.getcwd()+"\\Training\\Images")
        self.fct = False
        self.resizeX = 0
        self.resizeY = 0
        self.resizeFlag = False
        self.CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	        "sofa", "train", "tvmonitor","watch"]
        self.net = cv2.dnn.readNetFromCaffe(os.getcwd()+proto_text, os.getcwd()+caffe_model)
        self.guicheck = True

    def run(self):
        self.Init()

    def showFrameCaptureTime(self,Enable):
        self.fct = Enable

    def setSaveLocation(self,fName,loc):
        if os.path.isdir(os.getcwd()+loc) != True :
            os.mkdir(os.getcwd()+loc)
        self.location = os.getcwd()+loc
        self.fileName = fName
        
    def resizeImage(self,x,y,Enable):
        self.resizeX = x
        self.resizeY = y
        self.resizeFlag = Enable

    def saveimage(self,image):
        cv2.imwrite(self.location+self.fileName+str(self.count)+".jpg", image)
        #print(self.location+self.fileName+str(self.count)+".jpg")
    
    def odprocessing(self,frame):
        
        COLORS = np.random.uniform(0, 255, size=(len(self.CLASSES), 3))

        

        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
            0.007843, (300, 300), 127.5)
    
        # pass the blob through the self.network and obtain the detections and
        # predictions
        self.net.setInput(blob)
        detections = self.net.forward()

            # loop over the detections
        for i in np.arange(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with
            # the prediction
            confidence = detections[0, 0, i, 2]
    
            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > 0.2:
                # extract the index of the class label from the
                # `detections`, then compute the (x, y)-coordinates of
                # the bounding box for the object
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
    
                # draw the prediction on the frame
                label = "{}: {:.2f}%".format(self.CLASSES[idx],
                    confidence * 100)
                cv2.rectangle(frame, (startX, startY), (endX, endY),
                    COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
        return frame

    def killwindow(self):
        self.guicheck = False

    def Init(self):
        while(cv2.waitKey(1) & 0xFF != ord('q')):
            old_time = time.time()
            img = ImageGrab.grab(bbox=(self.x1, self.y1, self.x2, self.y2))
            img_np = np.array(img)
            self.frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            if(self.save):
                if(self.resizeFlag):
                    self.frame = cv2.resize(
                        self.frame, (self.resizeX, self.resizeY))
                self.saveimage(self.frame)
                self.count = self.count + 1
            cv2.imshow("Screen", self.odprocessing(self.frame))
            if(self.fct):
                print("Took "+str(time.time() - old_time)+" Sec")
		
        cv2.destroyAllWindows()
