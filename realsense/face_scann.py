import pyrealsense2 as rs
import numpy as np
import open3d as o3d
import cv2

# read Classfier models
face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_down_sample(ind)
    outlier_cloud = cloud.select_down_sample(ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])


# ストリーム(Depth/Color)の設定
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# ストリーミング開始
pipeline = rs.pipeline()
profile = pipeline.start(config)

# Alignオブジェクト生成
align_to = rs.stream.color
align = rs.align(align_to)

try:
    while True:
        # フレーム待ち(Color & Depth)
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        color_frame = aligned_frames.get_color_frame()
        depth_frame = aligned_frames.get_depth_frame()

        if not depth_frame or not color_frame:
            continue

        # color_image = o3d.geometry.Image(np.asanyarray(color_frame.get_data()))
        # depth_image = o3d.geometry.Image(np.asanyarray(depth_frame.get_data()))

        img = np.asanyarray(color_frame.get_data())
        dep_img = np.asanyarray(depth_frame.get_data())

        # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # print(faces)
        # for (x,y,w,h) in faces:
        #     img = img[y-100:y+h+100, x-100:x+w+100]
        #     dep_img = dep_img[y-100:y+h+100, x-100:x+w+100]

        color_image = o3d.geometry.Image(img)
        depth_image = o3d.geometry.Image(dep_img)

        rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_image, depth_image)

        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image,
                                                                o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
        print(pcd)

        # 回転する
        pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

        # 法線計算
        pcd.estimate_normals()

        # 指定したvoxelサイズでダウンサンプリング
        voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.01)

        distances = voxel_down_pcd.compute_nearest_neighbor_distance()
        avg_dist = np.mean(distances)
        radius = 1.5 * avg_dist

        print(voxel_down_pcd)
        # help(voxel_down_pcd)


        print("Statistical oulier removal")
        cl, ind = voxel_down_pcd.remove_radius_outlier(nb_points=16, radius=0.05)
        # display_inlier_outlier(voxel_down_pcd, ind)

        

        # メッシュ化
        radii = [radius, radius * 2]
        mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(voxel_down_pcd, o3d.utility.DoubleVector(radii))

        # 再度法線計算
        mesh.compute_vertex_normals()

        # # 一応データ保存
        # name = input('Put name of output:')
        # name += ".ply"
        # o3d.io.write_triangle_mesh(name, mesh)

        # メッシュデータの表示
        mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(
        size=0.6, origin=[0, 0, -0.5])
        cv2.imshow("img", img)
        cv2.imshow("img2", dep_img)
        o3d.visualization.draw_geometries([voxel_down_pcd, mesh_frame])

finally:
    # ストリーミング停止
    pipeline.stop()