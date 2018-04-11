@echo off
echo *********************************************
echo *          Environment Setup V1             *
echo *            Author:Kiran.R                 *
echo *                                           *
echo * Please Do not Edit this Script.           *
echo * Any issues with the script Contact me.    *
echo *********************************************
bitsadmin /transfer "python Setup"  https://www.python.org/ftp/python/2.7.14/python-2.7.14.amd64.msi   %CD%\python-2.7.14.amd64.msi
echo just press next do not modify the path of the upcoming setup..(if you read this please press enter to continue)
start /wait %CD%\python-2.7.14.amd64.msi
del %CD%\python-2.7.14.amd64.msi
setx PATH C:\Python27

bitsadmin /transfer "Python PIL setup" http://effbot.org/media/downloads/PIL-1.1.7.win32-py2.7.exe  %CD%\PIL-1.1.7.win32-py2.7.exe
start /wait %CD%\PIL-1.1.7.win32-py2.7.exe
del %CD%\PIL-1.1.7.win32-py2.7.exe

python %CD%\SetupFiles\get-pip.py
echo Installing Dependecies.
python -m pip install opencv-python

Pause