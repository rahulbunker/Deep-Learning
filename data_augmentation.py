# -*- coding: utf-8 -*-
"""Data Augmentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_kFd-WQ2jqMB6tDyDK9vnnad4biolwV4
"""

## Data Augmentation

# Data Augmentation is a technique to artificially increase your dataset size by creating modified versions of existing images, like:

# Rotating

# Flipping

# Zooming

# Cropping

# Changing brightness, etc.

# Benefits of Data Augmentation
# Prevents Overfitting

# Adds variety to training data, so the model doesn’t memorize it.

# Increases Dataset Size

# Generates more training examples from limited original images.

# Improves Generalization

# Helps the model perform better on unseen/test data.

# Enhances Model Robustness

# Makes the model more resistant to real-world changes like:

# Rotation

# Lighting

# Zoom

# Flipping

# Saves Time and Cost

# Reduces the need for collecting large datasets manually.

# Improves Accuracy

# With more diverse data, models learn better and often give higher accuracy.

# Reduces Sensitivity to Noise

# Augmented images act like noisy data, training the model to ignore irrelevant variations.

# Improves Feature Learning

# Encourages the model to focus on important features, not image position or angle.

# Works in Real-Time Training

# Augmented images can be generated on the fly during training.

# Essential for Small Datasets

# Especially helpful when only a few hundred or thousand images are available.



from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

img=image.load_img('cat.jpg',target_size=(200,200))

img

type(img)

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
)

img=image.img_to_array(img)

type(img)

img.shape

input_batch = img.reshape(1,200,200,3)

i=0
for output in datagen.flow(input_batch,batch_size=1,save_to_dir="aug"):

  i=i+1

  if i==10:
    break

input_batch.shape

