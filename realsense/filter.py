import numpy as np
import open3d as o3d

def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_down_sample(ind)
    outlier_cloud = cloud.select_down_sample(ind, invert=True)

    # 基準線の描画
    points = [
        [0, -0.1, -0.35],
        [0.5, -0.1, -0.35],
        [0, 0.06, -0.35],
        [0.5, 0.06, -0.35],
    ]
    lines = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3],
    ]
    colors = [[1, 0, 0] for i in range(len(lines))]
    line_set = o3d.geometry.LineSet(
        points=o3d.utility.Vector3dVector(points),
        lines=o3d.utility.Vector2iVector(lines),
    )
    line_set.colors = o3d.utility.Vector3dVector(colors)

    print("Showing outliers (red) and inliers (gray): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud, line_set])

if __name__ == "__main__":

    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud("./TestData/output.ply")
    o3d.visualization.draw_geometries([pcd])
    ary1 = np.asanyarray(pcd.points)
    face_points = ary1[(ary1[:,2] > -0.35)&(ary1[:,1] > -0.1)&(ary1[:,1]<0.06)]
    pcd.points = o3d.utility.Vector3dVector(face_points)
    pcd.estimate_normals()

    print("Statistical oulier removal")
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=20,
                                                        std_ratio=2.0)
    display_inlier_outlier(pcd, ind)
    o3d.visualization.draw_geometries([cl])

    print("Radius oulier removal")
    cl, ind = pcd.remove_radius_outlier(nb_points=30, radius=0.05)
    display_inlier_outlier(pcd, ind)

    # use two filterd
    cl, ind = pcd.remove_radius_outlier(nb_points=30, radius=0.05)
    o3d.visualization.draw_geometries([cl])
    cl2, ind2 = cl.remove_statistical_outlier(nb_neighbors=20,std_ratio=2.0)
    o3d.visualization.draw_geometries([cl2])
    display_inlier_outlier(cl, ind2)

    # x,y,z = 0の点群に修正
    print("Fix points to x=0")
    ary = np.asanyarray(cl2.points)
    ary[:, 0] = 0.0
    print(ary)
    cl2.points = o3d.utility.Vector3dVector(ary)
    cl2.estimate_normals()
    display_inlier_outlier(cl2, ind2)