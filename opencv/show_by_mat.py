# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread('image.png',0)

# interpolationの設定で描画方法を変えられる
# https://imagingsolution.blog.fc2.com/blog-entry-142.html
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

#
# matplotlibとcvでは読み込み方式が違う
#

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
# 121→1行2列で1番目の領域に描画
# https://stats.biopapyrus.jp/python/subplot.html
plt.subplot(121);plt.imshow(img) # expects distorted color
# plt.xticks([]), plt.yticks([]) # hide axis
plt.subplot(122);plt.imshow(img2) # expect true color
# plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()