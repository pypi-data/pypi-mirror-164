# DataAugmentation
It is a model for augmentation of image dataset. Augmentation of image is carried out by the process of resize, scale, rotate, translation, transpose, blurring, and by adding noise to the image. Dataset(X_train) can be augmented to 10x of its original size while saving y_train data for each image.

**::Test code::**
```
from ImageAugmentation import *
imgaug = ImageAugmentation('X_train', [0,1,1])
final_lst = imgaug.dataAugmentation(directory = "modified_X_train", parent_dir = "XXXXXX",
                          resize='150x150', rotate=[90, 180, 270], scale=[1, 1.5, 1], noiseAmt=0.2,
                          noiseSaltvsPepper=0.004, transformavalue=[0.09,0.43,0.56,0.85,0.99,0.32,0.32,0.99], flip=[0,1],
                          kernel=(5,5),translation=[[1, 0, 25], [0, 1, 50]])

imgaug.showImg(final_lst)
imgaug.getY_trainValue()
```
