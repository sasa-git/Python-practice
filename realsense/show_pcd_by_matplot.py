import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


print("Testing IO for point cloud ...")
pcd = o3d.io.read_point_cloud("TestData/test_face.pcd")
points = np.array(pcd.points)
print(pcd)
print(f"shape: {points.shape}")
print(f"point clouds:\n{points}")
o3d.visualization.draw_geometries([pcd])

print("print by plt")

X = points[:, 0]
Y = points[:, 1]
Z = points[:, 2]

#グラフの枠を作っていく
fig = plt.figure()
ax = Axes3D(fig)

#軸にラベルを付けたいときは書く
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

#.plotで描画
#linestyle='None'にしないと初期値では線が引かれるが、3次元の散布図だと大抵ジャマになる
#markerは無難に丸
ax.plot(X,Y,Z,marker="o",linestyle='None', markersize=1)

#最後に.show()を書いてグラフ表示
plt.show()