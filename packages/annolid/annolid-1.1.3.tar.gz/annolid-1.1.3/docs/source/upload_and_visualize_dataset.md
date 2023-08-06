---
size: 1080p
transition: crossfade 0.2
theme: light
subtitles: embed
---

![](upload_and_visulization_dataset.mp4)

In this video, we'll show you how to upload and visualize your dataset in Google Colab.

First, please install and run Detectron2 in Colab. 


You can choose to download an example dataset or you can upload your own dataset by run the upload labeled dataset cell. 

(pause: 10)

When the upload is done, run the cells to unzip the dataset.

Please select one image and type the image name to check an image in the dataset. 

(pause: 5)

Then, we create a Detectron2 config and a Detectron2 DefaultPredictor to run inference on this image.

You can check that the default predictor with pretrained weights from COCO dataset does not work well
for this example image. 

(pause: 5)

In order to train on a custom dataset, we need to register the dataset to Detectron2. 

Then, you can check the dataset distributions of instances after running the dataset dicts cell. 

To verify the dataset loading is correct, you can check visualization of the random selected annotations samples in the training set. 
 


