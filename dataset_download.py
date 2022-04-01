"""Prepare PASCAL VOC datasets"""
import os
import shutil
from utils import *


# Download and xtract VOC datasets into ``path``
path=os.path.join(os.getcwd(),"data")

path=os.path.join(os.getcwd(),"data")
if not os.path.exists(path):
    os.mkdir(path)
    
download_voc(path)
shutil.move(os.path.join(path, 'VOCdevkit', 'VOC2007'), os.path.join(path, 'VOC2007'))
shutil.move(os.path.join(path, 'VOCdevkit', 'VOC2012'), os.path.join(path, 'VOC2012'))
shutil.rmtree(os.path.join(path, 'VOCdevkit'))

