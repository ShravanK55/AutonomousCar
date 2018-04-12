#****************************************************#
#		Agent Version 1.0
#
#	This is the main File to be executed for
#	training and running the agent and conf-
#	iguring agent.
#
#****************************************************#
import os
import tkinter
import platform
from tkinter import Tk, Label, Button

sc=""





class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.pos_x = 100
        self.pos_y = 100
        self.screen_x = 700
        self.screen_y = 700

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.startD_button = Button(master, text="Start Image Detection", command=self.objectDetectionLaunch)
        self.startD_button.pack()

        self.scanbutton = Button(master, text="Set Scan Area", command=self.getScanArea)
        self.scanbutton.pack()
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
   
    def objectDetectionLaunch(self):
        if(platform.system()=="Linux"):
            from ConvolutionalNetwork.screencaptureLinux import ScreenShot as LinuxScreenShot
            sc = LinuxScreenShot(self.pos_x,self.pos_y,self.pos_x+self.screen_x,self.pos_y+self.screen_y,False,"/ConvolutionalNetwork/models/MobileNetSSD_deploy.prototxt","/ConvolutionalNetwork/models/MobileNetSSD_deploy.caffemodel")
        if(platform.system()=="Windows"):
            from ConvolutionalNetwork.screencaptureWindows import ScreenShot as WinScreenShot
            sc = WinScreenShot(self.pos_x,self.pos_y,self.pos_x+self.screen_x,self.pos_y+self.screen_y,False,"/ConvolutionalNetwork/models/MobileNetSSD_deploy.prototxt","/ConvolutionalNetwork/models/MobileNetSSD_deploy.caffemodel")
        print(root.winfo_geometry())
        self.scanbutton['state'] = "normal"
        sc.run()


    def getScanArea(self):
        gemo = root.winfo_geometry()
        screen,self.pos_x,self.pos_y = gemo.split('+')
        self.screen_x,self.screen_y = screen.split('x')
        self.pos_x = int(self.pos_x)
        self.pos_y = int(self.pos_y)
        self.screen_x =int(self.screen_x)
        self.screen_y = int(self.screen_y)
        self.scanbutton['state'] = "disabled"
        self.resetwindow()

    def resetwindow(self,width=300, height=200):
        # get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))

def center_window(width=300, height=200):
        # get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = Tk()
center_window()
my_gui = MyFirstGUI(root)
root.mainloop()
