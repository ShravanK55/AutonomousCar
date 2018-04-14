#!/bin/sh
<<<<<<< HEAD
=======
echo "**************************************"
echo "*     Author: Kiran r                *"
echo "*     Dependencies installer         *"
echo "**************************************"
echo ""
echo ""
sleep 3
>>>>>>> Training
echo "***************************************"
echo "python installation"
echo "***************************************"
sleep 3
sudo apt-get install python
echo "***************************************"
echo "python-dev installation"
echo "***************************************"
sleep 3
sudo apt-get install python-dev
echo "***************************************"
echo "python pip installation"
echo "***************************************"
sleep 3
sudo apt-get install python-pip
echo "***************************************"
echo "python pip update"
echo "***************************************"
sleep 3
sudo pip install --upgrade pip
echo "***************************************"
echo "numpy installation"
echo "***************************************"
sleep 3
sudo pip install numpy
echo "***************************************"
echo "opencv installation"
echo "***************************************"
sleep 3
sudo apt-get install python-opencv
echo "***************************************"
echo "argparser installation"
echo "***************************************"
sleep 3
wget https://pypi.python.org/packages/f2/94/3af39d34be01a24a6e65433d19e107099374224905f1e0cc6bbe1fd22a2f/argparse-1.4.0-py2.py3-none-any.whl#md5=c37216a954c8669054e2b2c54853dd49
sudo pip install argparse-1.4.0-py2.py3-none-any.whl
sudo rm argparse-1.4.0-py2.py3-none-any.whl
echo "***************************************"
echo "setuptools installation"
echo "***************************************"
sleep 3
sudo pip install setuptools
echo "***************************************"
echo "imutils installation"
echo "***************************************"
sleep 3
sudo pip install imutils
echo "***************************************"
echo "python-xlib installation"
echo "***************************************"
sleep 3
sudo apt-get install  python-xlib
echo "***************************************"
echo "pyautogui installation"
echo "***************************************"
sleep 3
sudo pip install pyautogui
echo "***************************************"
echo "msvcrt installtion"
echo "***************************************"
sleep 3
wget https://pypi.python.org/packages/56/f7/cde35f44d267df7122005c40f1a15cf5e3c60ffc83a2ab00d11d99e9d8c4/getch-1.0-python2.tar.gz#md5=586ea0f1f16aa094ff6a30736ba03c50
tar xvzf getch-1.0-python2.tar.gz
cd getch-1.0
sudo python setup.py build
sudo python setup.py install
cd ..
rm -rf getch-1.0
rm getch-1.0-python2.tar.gz
echo "***************************************"
echo "TKinter installtion"
echo "***************************************"
sleep 3
sudo apt-get install python-tk
echo "***************************************"
echo "opencv for dnn installtion"
echo "***************************************"
sleep 3
sudo pip install opencv_python
