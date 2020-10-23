import pyrealsense2 as rs
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
# import cv2

def show_img(img, dep_img):
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))

    for axe, image in zip(axes, [img, dep_img]):
        axe.imshow(image)
    plt.show()
    plt.close()

# ストリーム(Depth/Color)の設定
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
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

        img = np.array(color_frame.get_data())
        dep_img = np.array(depth_frame.get_data())

        # 取得画像の表示
        # show_img(img, dep_img)
        # print("choose command:")
        # command = input()
        # if command == 'q':
        #     exit()
        # else:
        #     continue
        

finally:
    # ストリーミング停止
    pipeline.stop()