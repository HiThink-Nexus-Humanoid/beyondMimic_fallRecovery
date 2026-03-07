import numpy as np

# 替换为你的NPZ文件路径
# npz_file = "fall_recovery.npz"
npz_file = "motion.npz"

# 加载NPZ文件
data = np.load(npz_file)

# 查看文件中包含的所有数组名称
print("Available keys in the npz file:")
for key in data.keys():
    print(f"- {key}")

# 查看每个数组的形状和部分数据
print("\nArray details:")
for key in data.keys():
    array = data[key]
    print(f"\n{key}:")
    print(f"  Shape: {array.shape}")
    print(f"  Data type: {array.dtype}")
    # print(f"  First few elements: {array[0] if array.size > 0 else 'empty'}")
    print(f"  First few elements: {array}")

print("data = ", data)

# # 特别查看关键信息
# if 'fps' in data:
#     print(f"\nFPS: {data['fps'][0]}")
    
# if 'body_pos_w' in data:
#     print(f"Body positions shape: {data['body_pos_w'].shape}")
#     print(f"First body position: {data['body_pos_w'][0]}")
    
# if 'body_quat_w' in data:
#     print(f"Body orientations shape: {data['body_quat_w'].shape}")
#     print(f"First body orientation (quaternion): {data['body_quat_w'][0]}")