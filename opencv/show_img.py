import numpy as np
import cv2

# imread(filename, var) varは以下ごとに設定できる
# 1 : cv2.IMREAD_COLOR : カラー画像として読み込む．画像の透明度は無視される．デフォルト値
# 0 : cv2.IMREAD_GRAYSCALE : グレースケール画像として読み込む
# -1: cv2.IMREAD_UNCHANGED : アルファチャンネルも含めた画像として読み込む

# Load an color image in grayscale
img = cv2.imread('image.png',0)

cv2.imshow('img', img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()