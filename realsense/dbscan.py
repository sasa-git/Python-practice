import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

def main():
    pcd = o3d.io.read_point_cloud("./TestData/output.ply")
    print(pcd)
    labels = np.array(pcd.cluster_dbscan(eps=0.02, min_points=10, print_progress=True))
    print(f"pcd.points.shape(): {np.array(pcd.points).shape}")
    print(f"labels.shape(): {labels.shape}")

    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")
    print("First 5 labels:",labels[:10])
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    # o3d.visualization.draw_geometries([pcd])

    for label in np.unique(labels):
        mask = labels == label
        
        part_of_pcd = o3d.geometry.PointCloud()
        part_of_pcd.points = o3d.utility.Vector3dVector(np.array(pcd.points)[mask])
        o3d.visualization.draw_geometries([part_of_pcd])

if __name__ == "__main__":
    main()