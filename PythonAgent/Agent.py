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
from tkinter import Tk, Label, Button
#from ConvolutionalNetwork.screencaptureLinux import ScreenShot as LinuxScreenShot
from ConvolutionalNetwork.screencaptureWindows import ScreenShot as WinScreenShot

#linux_sc = LinuxScreenShot(100,100,700,700,False,"/ConvolutionalNetwork/models/MobileNetSSD_deploy.prototxt","/ConvolutionalNetwork/models/MobileNetSSD_deploy.caffemodel")
#linux_sc.run()

Win_sc = WinScreenShot(100,100,700,700,False,"/ConvolutionalNetwork/models/MobileNetSSD_deploy.prototxt","/ConvolutionalNetwork/models/MobileNetSSD_deploy.caffemodel")
Win_sc.run()

