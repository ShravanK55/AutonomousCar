#****************************************************#
#		Agent Version 1.0
#
#	This is the main File to be executed for
#	training and running the agent and conf-
#	iguring agent.
#
#****************************************************#
import os
import Tkinter
from ConvolutionalNetwork.screencaptureLinux import ScreenShot

sc = ScreenShot(100,100,700,700,False,"/ConvolutionalNetwork/models/MobileNetSSD_deploy.prototxt","/ConvolutionalNetwork/models/MobileNetSSD_deploy.caffemodel")
sc.run()


