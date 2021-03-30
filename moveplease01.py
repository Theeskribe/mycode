#!/usr/bin/env python3

import shutil
import os

# Prep folder/files for OS file move/rename tests
mkdir -p ~/mycode/ceph_storage
touch ~/mycode/ceph_storage/kerrigan.obj
touch ~/mycode/raynor.obj

# Switch to the mycode folder
os.chdir('/home/student/mycode/')

# Move raynor.obj file to the subfolder
shutil.move('raynor.obj', 'ceph_storage/')


# The following lines will ask for a new name and then rename the kerrigan.obj file to it
xname = input('What is the new name for kerrigan.obj')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
