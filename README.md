# Food_Classification
 Basic classifing model using vanilla convolutional neural networks
# Image Classifier using CNN
# what is a CNN?
what is CNN – as we know its a machine learning algorithm for machines to understand the features of the image with foresight and remember the features to guess whether the name of the new image fed to the machine.

This model is used to classify images of food of about 20 different classes.

# About the dataset

A Food database of 20 most consumed Indian foods. The dataset consists of 2,000 Indian food images and has approximately a minimum of around 100 sample images for each
food item class. The acquired images have resolutions in the range of a minimum of 200x150 to 5760x3840 pixels per image. 

The data has been collected from real-world images and is subject to distortions and improper illuminations of certain regions.



# About the model

The model is a vanilla CNN model. The feature extraction part of the model contains 9 layers with a Pretrained model called MobileNet and 1 Globalmaxpooling layer. We also haave the last layer containing the soft max layer.Then comes The optimiser we use is adam, as it offers more accuracy and is best suited for classification models. 

Another technique used was Data augmentation.Data augmentation in data analysis are techniques used to increase the amount of data by adding slightly modified copies of already existing data or newly created synthetic data from existing data.

# Why MobileNet?
As a lightweight deep neural network, MobileNet has fewer parameters and higher classification accuracy. In order to further reduce the number of network parameters and improve the classification accuracy, dense blocks that are proposed in DenseNets are introduced into MobileNet.

# Members:

Charvi Bannur:https://github.com/charvibannur

Gagan Goutham:https://github.com/GaganGoutham

Amitram Achunala:https://github.com/Amit-ram1103
