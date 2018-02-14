import cv2
import numpy as np
import pyautogui as pyag
from PIL import ImageGrab
from msvcrt import getch
import os
import time

class ScreenShot:
 
    def __init__(self,point1x,point1y,point2x,point2y,saveOption):
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


    def Init(self):
        while(cv2.waitKey(1) != 27):
            old_time = time.time()
            img = ImageGrab.grab(bbox=(self.x1,self.y1,self.x2, self.y2))
            img_np = np.array(img)
            self.frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            cv2.imshow("Screen", self.detectEdge(self.frame))
            if(self.save):
                if(self.resizeFlag):
                    self.frame = cv2.resize(self.frame,(self.resizeX,self.resizeY))
                self.saveimage(self.frame)
                self.count = self.count + 1
            if(self.fct):
                print("Took "+str(time.time() - old_time)+" Sec")

        cv2.destroyAllWindows()
