import numpy as np
import open3d as o3d

if __name__ == "__main__":

    mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(
        size=0.6, origin=[0, 0, -0.5])

    # 線の描画
    print("Let's draw a cubic using o3d.geometry.LineSet.")
    points = [
        [0, 0, -0.5],
        [0.5, 0, -0.5],
        [0, 0.5, -0.5],
        [0.5, 0.5, -0.5],
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


    # ROWデータ表示
    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud("./TestData/output.ply")
    print(pcd)
    print(np.asarray(pcd.points))
    o3d.visualization.draw_geometries([pcd, mesh_frame, line_set])

    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    # print(np.asarray(downpcd.points))
    # print(downpcd.points)

    print("test")
    # pcd.pointsで点群データをlistで取得
    ary1 = np.asanyarray(downpcd.points)
    print(ary1)

    print("reduce")
    # z軸(2列目)が-0.4以上の物だけを抽出
    # それぞれの結果を行または列のインデックス参照[行, 列](=[:,2]の部分)に与えると所望の行・列が抽出される。[行, :]の場合、末尾の, :は省略できる。
    # https://note.nkmk.me/python-numpy-condition/
    result1 = ary1[ary1[:,2] > -0.5]
    print(result1)

    # Convert float64 numpy array of shape (n, 3) to Open3D format.
    downpcd.points = o3d.utility.Vector3dVector(result1)


    ary2 = np.asanyarray(pcd.points)
    # z軸が-0.4以上の物だけを抽出
    result2 = ary2[ary2[:,2] > -0.6]

    # Convert float64 numpy array of shape (n, 3) to Open3D format.
    pcd.points = o3d.utility.Vector3dVector(result2)

    # for point, index in np.asanyarray(downpcd.points):
    #     if point[2] > -0.5:
    #         np.delete()


    print("downpcd filtered")
    o3d.visualization.draw_geometries([downpcd, mesh_frame])
    print("pcd filtered")
    # 法線の再計算
    pcd.estimate_normals()
    o3d.visualization.draw_geometries([pcd, line_set])

    # print("Recompute the normal of the downsampled point cloud")
    # downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
    #     radius=0.1, max_nn=30))
    # o3d.visualization.draw_geometries([downpcd])
    # print(np.asarray(downpcd.points))

    # print("Print a normal vector of the 0th point")
    # print(downpcd.normals[0])
    # print("Print the normal vectors of the first 10 points")
    # print(np.asarray(downpcd.normals)[:10, :])
    # print("")

    # print("Load a polygon volume and use it to crop the original point cloud")
    # vol = o3d.visualization.read_selection_polygon_volume(
    #     "../../TestData/Crop/cropped.json")
    # chair = vol.crop_point_cloud(pcd)
    # o3d.visualization.draw_geometries([chair])
    # print("")

    # print("Paint chair")
    # chair.paint_uniform_color([1, 0.706, 0])
    # o3d.visualization.draw_geometries([chair])
    # print("")