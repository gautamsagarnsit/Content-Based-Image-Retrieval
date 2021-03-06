# Content-Based-Image-Retrieval
Term Project for the Course Information Retrieval (CS60092)<br>
Colab File: https://colab.research.google.com/drive/1f5NHByVGZMyIv5zo2YK9CiWcEpn8lXST?usp=sharing
## How to Use
1. Best way to use it is through the jupyter notebook file "CBIR_MAIN.ipynb"
2. Although the jupyter notebook is self contained, but it is advisable to keep the following pickle files in the right directory. Otherwise it may take around 5-7 hours for inital setup. The links of the pickle files are given below<br>
  (i) VOC 2012 dataset: https://drive.google.com/drive/folders/1HeM-Rz5yugfBc5pBU6JrNwjPjI-IHWQe?usp=sharing<br>
  (ii) VOC 2007 dataset: https://drive.google.com/drive/folders/1-1DLwF1I4c53Cd537eITmhzUD0CvFslb?usp=sharing<br>
  (iii) https://drive.google.com/file/d/1T5ohMmAkySodhT89JxYxZp0ECEvKv8aQ/view?usp=sharing<br>
  (iv) https://drive.google.com/file/d/1lbhF4eIDU8gmLgaw7UECJkseR71cq4GB/view?usp=sharing<br>
  (v) https://drive.google.com/file/d/1XnM333EO_xwkX1aRuPVf6Yn-Ue1wE99Y/view?usp=sharing<br>
  (vi) https://drive.google.com/file/d/1BJoQ5_xUSENxFQaNclLdCocYWnH5XVYq/view?usp=sharing<br>
  (vii) https://drive.google.com/file/d/1LhnKcsJjq_Z2LU9oELsJo-Dj9yDujybg/view?usp=sharing<br>
  (viii) https://drive.google.com/file/d/1TKVm2x12w6SouD3vkBFUNf4_gPOYFGp5/view?usp=sharing<br>
<br>
Make Sure to put all these files/folders in the directory path ="/content/drive/MyDrive". This is same as if you add these files in your google drive using the given links and mount the drive in google colab. <br>
Make sure the following path exists after you add these files in your google drive:<br>
  (i) "/content/drive/MyDrive/VOC2007"<br>
  (ii) "/content/drive/MyDrive/VOC2012"<br>
  (iii) "/content/drive/MyDrive/train_data.pickle"<br>
  (iv) "/content/drive/MyDrive/val_data.pickle"<br>
  (v) "/content/drive/MyDrive/CBIR_InvIndex.pickle"<br>
  (vi) "/content/drive/MyDrive/CBIR_ImageBB.pickle"<br>
  (vii) "/content/drive/MyDrive/InvIndex_final_version"<br>
  <br>
3. If step is completed then you can easily reach the cell after the heading "Taking User Input". Here taking image from user as the query image is simulated by taking an index between 0 to 4591 as input. Because there are 4592 images in the validation split of VOC dataset, thus a user can give any index between 0 to 4591 as input.
There are two cells for taking user input. These cells are identical except that in the first cell the input images as well as their bounding boxes are taken directly from the validation set which does not represent a real world case where we do not have bounding boxes and class information for an image. So for a more real world experience user can use the second cell for giving the input. The input image is passed through a SSD network to predict the bounding box location and the class associated with the bounding boxes.<br>
4. After Giving the input just run all the cells after it. Top-10 similar images will be shown as well as saved in the google drive.
