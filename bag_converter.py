import os
import rosbag
import cv2
import numpy as np
from cv_bridge import CvBridge
from donkeycar.parts.tub_v2 import TubWriter

# --- 配置区域 ---
# 每次转换前，只需修改 BAG_FILE 和 OUTPUT_DIR
BAG_FILE = 'newdata_2025-03-10-10-19-21.bag' # <--- 修改为当前要转换的包名
OUTPUT_DIR = 'data_bag_2' # <--- 修改为该包对应的输出文件夹名
# ----------------

IMAGE_TOPIC = '/usb_cam/image_raw'
CMD_TOPIC = '/cmd_vel'

# 清理旧数据（如果存在）
if os.path.exists(OUTPUT_DIR):
    import shutil
    shutil.rmtree(OUTPUT_DIR)
    print(f"清除了旧的 '{OUTPUT_DIR}' 文件夹。")

# 初始化 Donkeycar TubWriter
inputs = ['cam/image_array', 'user/angle', 'user/throttle', 'user/mode']
types = ['image_array', 'float', 'float', 'str']
tub = TubWriter(base_path=OUTPUT_DIR, inputs=inputs, types=types)

print(f"正在直接将 '{BAG_FILE}' 转换为 Tub V2 (新版) 格式，输出到 '{OUTPUT_DIR}'...")

bag = rosbag.Bag(BAG_FILE)
count = 0
last_steering = 0.0
last_throttle = 0.0

for topic, msg, t in bag.read_messages(topics=[IMAGE_TOPIC, CMD_TOPIC]):
    if topic == CMD_TOPIC:
        last_steering = msg.angular.z
        last_throttle = msg.linear.x
        
    elif topic == IMAGE_TOPIC:
        try:
            img_arr = np.frombuffer(msg.data, dtype=np.uint8)
            current_img = img_arr.reshape(msg.height, msg.width, -1)
            
            if msg.encoding == 'rgb8':
                current_img = cv2.cvtColor(current_img, cv2.COLOR_RGB2BGR)
                
            current_img = cv2.resize(current_img, (160, 120))
            
            tub.run(current_img, last_steering, last_throttle, "user")
            
            count += 1
            if count % 100 == 0:
                print(f"已转换 {count} 帧...")
                
        except Exception as e:
            print(f"跳过坏帧: {e}")

bag.close()
tub.close()
print(f"✅ 转换完成！有效数据: {count} 帧。")
print(f"数据存放位置: {OUTPUT_DIR}")
