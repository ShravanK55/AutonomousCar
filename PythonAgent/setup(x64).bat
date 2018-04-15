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

bitsadmin /transfer "Python PIL setup" https://github.com/lightkeeper/lswindows-lib/blob/master/amd64/python/PIL-1.1.7.win-amd64-py2.7.exe?raw=true  %CD%\PIL-1.1.7.win32-py2.7.exe
start /wait %CD%\PIL-1.1.7.win32-py2.7.exe
del %CD%\PIL-1.1.7.win32-py2.7.exe

bitsadmin /transfer "cmake setup" https://cmake.org/files/v3.11/cmake-3.11.0-win64-x64.msi %CD%\cmake-3.11.0-win64-x64.msi
start /wait %CD%\cmake-3.11.0-win64-x64.msi
del %CD%\cmake-3.11.0-win64-x64.msi
python %CD%\SetupFiles\get-pip.py
echo Installing Dependecies.
python -m pip install opencv-python
python -m pip install numpy
python -m pip install setuptools
python -m pip install imutils
python -m pip install pyautogui
python -m pip install argparse
Pause