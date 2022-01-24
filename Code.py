import cv2
import numpy as np
from google.colab import drive
drive.mount("/content/drive", force_remount=True)

#reading the image
image1 = cv2.imread('/content/drive/My Drive/Colab Notebooks/Image-Similarity/Images/image1.jpg')
image2 = cv2.imread('/content/drive/My Drive/Colab Notebooks/Image-Similarity/Images/image2.jpg')

#resizing the image
resized_image1 = cv2.resize(image1,(500,500))
resized_image2 = cv2.resize(image2,(500,500))

#calculating difference between the images
difference = cv2.subtract(resized_image1,resized_image2)
b,g,r = cv2.split(difference)

if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
  print("Similar")
else:
  print("Not Similar")
