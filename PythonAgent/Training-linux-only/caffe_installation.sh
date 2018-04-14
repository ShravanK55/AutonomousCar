
sudo apt install caffe-cpu
sudo apt build-dep caffe-cpu
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev




cd ~
mkdir deep-learning
cd deep-learning
# General Dependencies
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev

sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y build-essential cmake git pkg-config


# BLAS -- for better CPU performance
sudo apt-get install libatlas-base-dev

# Python -- It comes preinstalled on Ubuntu 14.04
# Required if you want to use Python wrappers for Caffe
sudo apt-get install the python-dev

# Remaining dependencies
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
sudo apt-get install libopenblas-dev

cd ~/deep-learning
git clone http://github.com/BVLC/caffe.git
cd caffe

cp Makefile.config.example Makefile.config