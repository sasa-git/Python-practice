import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png')

px = img[100,100]
print(px)

# accessing only blue pixel
# b:0 g:1 r:2
blue = img[100,100,0]
print(f'blue is {blue}')

img[180, 220] = [255,255,255]
print(f'180x220 is {img[180, 220]}')
# この直接各画素の要素を取得・変更をしていくのは処理に時間がかかる。上は配列の領域を選択するのに使う

# 各画素へのアクセスに関してはNumpyの配列を扱う array.item() と array.itemset() を使うと良い↓
# accessing RED value
print(img.item(100,100,2))

img.itemset((100,100,2),100)
print(img.item(100,100,2))

# 画像の属性情報の取得
print(img.shape)
# サイズの取得
print(img.size)
# データ型
print(img.dtype)

# 画像中の注目領域(ROI)

b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
# y,xの順で適用される
face = img2[100:300,200:400]
img2[0:200,0:200] = face
plt.subplot(231);plt.imshow(b)
plt.subplot(232);plt.imshow(g)
plt.subplot(233);plt.imshow(r)
plt.subplot(234);plt.imshow(img2)
plt.subplot(235);plt.imshow(face)
plt.show()
