---
size: 1080p
transition: crossfade 0.2
theme: light
subtitles: embed
---

![](train_mask_rcnn_network.mp4)

In this video, we'll show you how to fine-ture a COCO-pretrained Mask R-CNN model in Google Colab.

First, please run the check GPU cell and check the GPU info. 


It takes about 2 hours to train 3000 iterations on Colab's K80 GPU.


Please check and adjust hyperparameters based on your needs. For example, the default max iter is 6000. 
You can try with the default values and change them to improve the model's performances. 

Then please run the tensorboard cell and trainer cell. 
You can check that the default predictor with pretrained weights from COCO dataset does not work well
for this example image. 

(pause: 5)

The train engire will start from iteration 0. 


(pause: 10)

Then, you can check the tensorboard for monitering the training process. 

(pause: 50)

(pause: 20)

To verify that the training process is in good progress, the estimated time and losses are inline with your expectations. 
 


