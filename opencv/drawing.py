import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
# 線の太さを-1pxにすることで、内側を塗りつぶせる
# rectangle...左上と右下の角の座標
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# circle...中心座標と半径
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

# 楕円の中心座標(x,y)，軸の長さ(長径, 短径)，第3引数 angle は楕円の偏角を反時計回りで指定
# startAngle(0) と endAngle(90) は楕円を描画する始角と終角を長径から時計回りの方向で指定
img = cv2.ellipse(img,(256,256),(100,50),0,0,90,(0,255,255),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# -1とした次元の長さは他の次元の指定値から推測されて自動的に決定される。サイズの大きい配列の形状を変換するときに便利
pts = pts.reshape((-1,1,2))
# 第3引数が False の時，閉包図形ではなく全ての点をつなぐ線を描画
img = cv2.polylines(img,[pts],True,(255,255,0))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('draw', img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()