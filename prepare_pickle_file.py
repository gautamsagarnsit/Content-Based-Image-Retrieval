import os
import pickle
from utils import *


path=os.path.join(os.getcwd(),"data")

if not os.path.exists(path):
    os.mkdir(path)

pkl_path_train=os.path.join(path,"train_data.pickle")
pkl_path_val=os.path.join(path,"val_data.pickle")
InvIndex_path=os.path.join(path,"CBIR_InvIndex.pickle")
ImageBB_path=os.path.join(path,"CBIR_ImageBB.pickle")
InvIndex_final_path=os.path.join(path,"InvIndex_final_version.pickle")

if not os.path.exists(pkl_path_train):
    train_dataset,_=make_train_val_pickle(path,train=1,val=0)

if not os.path.exists(pkl_path_val):
    _,val_dataset=make_train_val_pickle(path,train=0,val=1)

if not (os.path.exists(InvIndex_path) or os.path.exists(ImageBB_path)):
    InvIndex,ImageBB=make_index_pickle(InvIndex_path,ImageBB_path,train_dataset)

if not os.path.exists(InvIndex_final_path):
    InvIndex_final_version=make_final_index_pickle(InvIndex_final_path,train_dataset)


