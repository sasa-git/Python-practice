# memo

## create_from_rgbd_image

http://www.open3d.org/docs/0.9.0/python_api/open3d.geometry.PointCloud.html?highlight=normalize#open3d.geometry.PointCloud.create_from_rgbd_image

（u、v）画像座標での深度値dが与えられると、対応する3dポイントは次のようになります。

- z = d / depth_scale

- x =（u-cx）* z / fx

- y =（v-cy）* z / fy

ここでは、デフォルトのカメラ・パラメータとしてPinholeCameraIntrinsic.prime_sense_defaultを使用する。 画像の解像度は640x480、焦点距離（fx、fy）=（525.0,525.0）、光学中心（cx、cy）=（319.5,239.5）である。 恒等行列（単位行列）がデフォルトの外部パラメータとして使用される。

[create_from_depth_image](http://www.open3d.org/docs/0.9.0/python_api/open3d.geometry.PointCloud.html?highlight=normalize#open3d.geometry.PointCloud.create_from_depth_image) というのもある