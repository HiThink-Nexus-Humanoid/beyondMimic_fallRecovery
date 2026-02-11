import numpy as np

# 1. 加载.npz文件
data = np.load('fall_recovery.npz')

# 2. 查看文件中的数组名称
print("=" * 50)
print("文件中的数组名称:")
print("=" * 50)
for i, key in enumerate(data.files):
    print(f"[{i}] {key}")

# 3. 查看每个数组的详细信息
print("\n" + "=" * 50)
print("每个数组的详细信息:")
print("=" * 50)
for key in data.files:
    array = data[key]
    print(f"\n数组名称: {key}")
    print(f"  形状: {array.shape}")
    print(f"  数据类型: {array.dtype}")
    print(f"  维度: {array.ndim}")
    print(f"  总元素数: {array.size}")
    
    # 统计信息
    if array.ndim > 0:  # 非标量
        print(f"  最小值: {array.min():.6f}")
        print(f"  最大值: {array.max():.6f}")
        print(f"  均值: {array.mean():.6f}")
        print(f"  标准差: {array.std():.6f}")
        print(f"  中位数: {np.median(array):.6f}")
        
        # 检查是否有NaN或Inf
        if np.isnan(array).any():
            nan_count = np.isnan(array).sum()
            print(f"  NaN数量: {nan_count} ({nan_count/array.size*100:.2f}%)")
        if np.isinf(array).any():
            inf_count = np.isinf(array).sum()
            print(f"  Inf数量: {inf_count}")
    
    # 查看前几个元素
    if array.ndim == 1:  # 一维数组
        print(f"  前5个元素: {array[:5]}")
    elif array.ndim == 2:  # 二维数组
        print(f"  形状示例: {array.shape}")
        if array.shape[0] > 0 and array.shape[1] > 0:
            print(f"  前3行前3列:")
            for i in range(min(3, array.shape[0])):
                print(f"    行{i}: {array[i, :min(3, array.shape[1])]}")
    elif array.ndim == 3:  # 三维数组
        print(f"  形状: {array.shape}")
        if array.shape[0] > 0 and array.shape[1] > 0 and array.shape[2] > 0:
            print(f"  [0,0,:]的前5个元素: {array[0, 0, :5]}")
    
    # 内存使用
    print(f"  内存大小: {array.nbytes:,} 字节 ({array.nbytes/1024/1024:.2f} MB)")

# 4. 保存为文本文件以便后续查看
with open('npz_analysis.txt', 'w', encoding='utf-8') as f:
    f.write("NPZ文件分析报告\n")
    f.write("=" * 50 + "\n\n")
    
    for key in data.files:
        array = data[key]
        f.write(f"数组名称: {key}\n")
        f.write(f"  形状: {array.shape}\n")
        f.write(f"  数据类型: {array.dtype}\n")
        f.write(f"  总元素数: {array.size}\n")
        
        if array.ndim > 0:
            f.write(f"  统计信息:\n")
            f.write(f"    最小值: {array.min():.6f}\n")
            f.write(f"    最大值: {array.max():.6f}\n")
            f.write(f"    均值: {array.mean():.6f}\n")
            f.write(f"    标准差: {array.std():.6f}\n")
        
        f.write("\n")

print(f"\n分析报告已保存到: npz_analysis.txt")

# 5. 关闭文件
data.close()