import pickle
from gluoncv import model_zoo,data, utils
from matplotlib import pyplot as plt
import pickle
import numpy as np
import os
from matplotlib import pyplot as plt
from gluoncv.utils import viz
from utils import *



with open('/content/drive/MyDrive/CBIR_InvIndex.pickle', 'rb') as handle:
    testing_load = pickle.load(handle)

with open('/content/drive/MyDrive/CBIR_ImageBB.pickle', 'rb') as handle:
    t = pickle.load(handle)

with open('/content/drive/MyDrive/train_data.pickle', 'rb') as handle:
    train_data = pickle.load(handle)
print("Total images in training set =",len(train_data))

with open('/content/drive/MyDrive/val_data.pickle', 'rb') as handle:
    val_data = pickle.load(handle)
print("Total images in validation set =",len(val_data))

with open('/content/drive/MyDrive/InvIndex_final_version.pickle', 'rb') as handle:
    InvIndex_final_version = pickle.load(handle)



for k,v in testing_load.items():
  lis_images=[]
  for i in range(len(v)):
    lis_images.append(v[i][0])
  testing_load[k]=reverse_count(lis_images)

'''
idx=int(input('Provide an integer between 0 and 4951\t'))
val_image, val_label = val_data[idx]
bboxes = val_label[:, :4]
cids_Q = val_label[:, 4:5]
ax = viz.plot_bbox(
    val_image.asnumpy(),
    bboxes,
    labels=cids_Q,
    class_names=train_data.classes)
plt.show()
'''
#Pretrained Model
net = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)

threshold=0.5
idx=int(input('Provide an integer between 0 and 4951\t'))
val_image, _ = val_data[idx]
x, img = data.transforms.presets.ssd.transform_test(val_image,short=512)
cids_Q, scores, bboxes = net(x)
n=int(sum(scores[0]>0.5).max().asnumpy()[0])

if n<3:
  n+=1
  threshold=0

cids_Q=cids_Q[0][:n]
bboxes=bboxes[0][:n]
scores=scores[0][:n]
ax = utils.viz.plot_bbox(img, bboxes, scores,cids_Q, thresh=threshold,class_names=net.classes)
#ax = utils.viz.plot_bbox(img, bboxes[0], scores[0],cids[0], class_names=net.clas
plt.show()

cids_Q=cids_Q.asnumpy()

lis_Query=[]
for i in cids_Q:
  lis_Query.append(int(i[0]))
cid_dict={}
for i in lis_Query:
  if(i in cid_dict.keys()):
    cid_dict[i]=cid_dict[i]+1
  else:
    cid_dict[i]=1

imagesIDs=[]
for classID,count in cid_dict.items():
  imagesIDs=imagesIDs+testing_load[classID][count] 

imagesIDs_dict=reverse_count(imagesIDs)
intermediate_ans=imagesIDs_dict[max(list(imagesIDs_dict.keys()))]



Query_vector=[]
for i in cids_Q:
  Query_vector.append(int(i[0]))
Query_vector=return_vector(Query_vector)

similarity=[]
b=np.array(Query_vector)
for i in intermediate_ans:
  a=np.array(InvIndex_final_version[i])
  similarity.append((i,np.linalg.norm(a-b)))
  
similarity.sort(key=lambda x:x[1])

l=10
if(l>len(similarity)):
  l=len(similarity)
for i in range(0,l+1):
  train_image, train_label = train_data[similarity[i][0]]
  bboxes = train_label[:, :4]
  cids = train_label[:, 4:5]
  print('image:', train_image.shape)
  print('bboxes:', bboxes.shape, 'class ids:', cids.shape)
  ax = viz.plot_bbox(
      train_image.asnumpy(),
      bboxes,
      labels=cids,
      class_names=train_data.classes)
  plt.show()