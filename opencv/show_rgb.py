import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
# 121→1行2列で1番目の領域に描画
# https://stats.biopapyrus.jp/python/subplot.html
plt.subplot(131);plt.imshow(r) # expects distorted color
plt.subplot(132);plt.imshow(g) # expect true color
plt.subplot(133);plt.imshow(b) # expect true color
plt.show()
