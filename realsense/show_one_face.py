import open3d as o3d
import numpy as np
import sys

path = sys.argv[1]
pcd = o3d.io.read_point_cloud(path)
o3d.visualization.draw_geometries([pcd])