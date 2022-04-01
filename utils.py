import tarfile
from gluoncv.utils import download, makedirs
import os
import shutil
import pickle
from gluoncv.data import VOCDetection

def download_voc(path, overwrite=False):
    _DOWNLOAD_URLS = [
                      ('http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar',
         '34ed68851bce2a36e2a223fa52c661d592c66b3c'),
        ('http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar',
         '41a8d6e12baa5ab18ee7f8f8029b9e11805b4ef1'),
        ('http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar',
         '4e443f8a2eca6b1dac8a6c57641b67dd40621a49')]
    makedirs(path)
    for url, checksum in _DOWNLOAD_URLS:
        filename = download(url, path=path, overwrite=overwrite, sha1_hash=checksum)
        # extract
        with tarfile.open(filename) as tar:
            tar.extractall(path=path)

def make_train_val_pickle(path,train=1,val=1):
    if not (os.path.exists(os.path.join(path, 'VOC2007')) or os.path.exists(os.path.join(path, 'VOC2012'))):
        #Datset Not available, download it
        os.mkdir(path)
        download_voc(path)
        shutil.move(os.path.join(path, 'VOCdevkit', 'VOC2007'), os.path.join(path, 'VOC2007'))
        shutil.move(os.path.join(path, 'VOCdevkit', 'VOC2012'), os.path.join(path, 'VOC2012'))
        shutil.rmtree(os.path.join(path, 'VOCdevkit'))

    # typically we use 2007+2012 trainval splits for training data
    out=[]
    if train==1:
        train_dataset = VOCDetection(root=path,splits=[(2007, 'trainval'), (2012, 'trainval')])
        print('Training images:', len(train_dataset))
        pkl_path_train=os.path.join(path,"train_data.pickle")
        with open(pkl_path_train, 'wb') as handle:
            pickle.dump(train_dataset, handle, protocol=pickle.HIGHEST_PROTOCOL)
        out.append(train_dataset)
    # and use 2007 test as validation data
    if val==1:
        val_dataset = VOCDetection(root=path,splits=[(2007, 'test')])
        print('Validation images:', len(val_dataset))
        pkl_path_val=os.path.join(path,"val_data.pickle")
        with open(pkl_path_val, 'wb') as handle:
            pickle.dump(val_dataset, handle, protocol=pickle.HIGHEST_PROTOCOL)
        out.append(val_dataset)

    return out

def make_index_pickle(InvIndex_path,ImageBB_path,train_dataset):
    InvIndex={}
    ImageBB=[]
    for i in range(len(train_dataset)):
        if i%400==0:
            print(i)
        train_image, train_label = train_dataset[i]
        bboxes = train_label[:, :4]
        cids = train_label[:, 4:5]
        ImageBB.append(bboxes)
        for idx,classID in enumerate(cids):
            if int(classID.item()) in InvIndex:
                if i not in InvIndex[int(classID.item())]:
                    InvIndex[int(classID.item())].append([i,bboxes[idx]])
                else:
                    InvIndex[int(classID.item())]=[[i,bboxes[idx]]]
    with open(InvIndex_path, 'wb') as handle:
        pickle.dump(InvIndex, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open(ImageBB_path, 'wb') as handle:
        pickle.dump(ImageBB, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    return InvIndex,ImageBB

def make_final_index_pickle(InvIndex_final_path,train_dataset):
    InvIndex_final_version={}
    for i in range(len(train_dataset)):
        if i%400==0:
            print(i)
        train_image, train_label = train_dataset[i]
        bboxes = train_label[:, :4]
        cids = train_label[:, 4:5]
        lis=[]
        for j in cids:
            lis.append(int(j[0]))
        # print(cids)
        # print(lis)
        InvIndex_final_version[int(i)]= return_vector(lis)
    with open(InvIndex_final_path, 'wb') as handle:
        pickle.dump(InvIndex_final_version, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return InvIndex_final_version

def reverse_count(l):
  d1={}
  # A dictionary of Image Id : count
  d2={}
  for i in l:
    if(i in d1.keys()):
      d1[i]=d1[i]+1
    else:
      d1[i]=1

  for k,v in d1.items():
    if(v in d2.keys()):
      d2[v].append(k)
    else:
      d2[v]=[]
      d2[v].append(k)
  return d2

def return_vector(a):
  l=[]
  d={}
  for i in a:
    if(i in d.keys()):
      d[i]=d[i]+1
    else:
      d[i]=1
  for i in range(20):
    if(i in d.keys()):
      l.append(d[i])
    else:
      l.append(0)
  return l