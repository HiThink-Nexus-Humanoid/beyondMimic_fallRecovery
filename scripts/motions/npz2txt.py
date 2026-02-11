import numpy as np

# 替换为你的NPZ文件路径
npz_file = "fall_recovery.npz"

# 加载NPZ文件
data = np.load(npz_file)

# 创建输出txt文件
output_file = "npz_data_analysis.txt"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write(f"NPZ文件数据详细分析: {npz_file}\n")
    f.write("=" * 80 + "\n\n")
    
    # 获取所有数组名称
    keys = list(data.keys())
    f.write(f"1. 文件基本信息:\n")
    f.write("-" * 40 + "\n")
    f.write(f"包含 {len(keys)} 个数组\n")
    f.write(f"数组名称: {keys}\n\n")
    
    f.write(f"2. 详细数据内容:\n")
    f.write("-" * 40 + "\n")
    
    # 遍历每个数组
    for i, key in enumerate(keys):
        array = data[key]
        
        f.write(f"\n[{i+1}] 数组名称: {key}\n")
        f.write(f"   形状: {array.shape}\n")
        f.write(f"   维度: {array.ndim}\n")
        f.write(f"   数据类型: {array.dtype}\n")
        f.write(f"   总元素数: {array.size}\n")
        f.write(f"   内存占用: {array.nbytes} 字节 ({array.nbytes/1024/1024:.2f} MB)\n")
        
        # 统计信息（仅适用于数值类型）
        if np.issubdtype(array.dtype, np.number) and array.size > 0:
            f.write(f"   统计信息:\n")
            f.write(f"     最小值: {array.min():.6e}\n")
            f.write(f"     最大值: {array.max():.6e}\n")
            f.write(f"     均值: {array.mean():.6e}\n")
            f.write(f"     标准差: {array.std():.6e}\n")
            f.write(f"     中位数: {np.median(array):.6e}\n")
            
            # 检查NaN和Inf
            if np.isnan(array).any():
                nan_count = np.isnan(array).sum()
                f.write(f"     NaN数量: {nan_count} ({nan_count/array.size*100:.2f}%)\n")
            if np.isinf(array).any():
                inf_count = np.isinf(array).sum()
                f.write(f"     Inf数量: {inf_count} ({inf_count/array.size*100:.2f}%)\n")
        
        f.write(f"\n   数据内容:\n")
        f.write("-" * 20 + "\n")
        
        # 根据数组维度以不同方式保存数据
        if array.ndim == 0:  # 标量
            f.write(f"    {array}\n")
            
        elif array.ndim == 1:  # 一维数组
            # 如果数组太大，只保存前1000个和后1000个元素
            if array.size <= 2000:
                np.savetxt(f, array.reshape(-1, 1), fmt='%.6e', delimiter='\n')
            else:
                f.write(f"    (数组太大，只显示前1000个和后1000个元素，共{array.size}个元素)\n")
                np.savetxt(f, array[:1000].reshape(-1, 1), fmt='%.6e', delimiter='\n')
                f.write(f"    ... 省略 {array.size-2000} 个元素 ...\n")
                np.savetxt(f, array[-1000:].reshape(-1, 1), fmt='%.6e', delimiter='\n')
                
        elif array.ndim == 2:  # 二维数组
            # 如果数组太大，只保存前100行和前10列
            rows_to_save = min(100, array.shape[0])
            cols_to_save = min(10, array.shape[1])
            
            if array.shape[0] > 100 or array.shape[1] > 10:
                f.write(f"    (数组太大，只显示前{rows_to_save}行和前{cols_to_save}列，完整形状: {array.shape})\n")
                np.savetxt(f, array[:rows_to_save, :cols_to_save], fmt='%.6e', delimiter='\t')
                f.write(f"\n    完整大小: {array.shape[0]} 行 × {array.shape[1]} 列\n")
            else:
                np.savetxt(f, array, fmt='%.6e', delimiter='\t')
                
        elif array.ndim == 3:  # 三维数组
            f.write(f"    三维数组，形状: {array.shape}\n")
            f.write(f"    显示每个2D切片的第一个元素:\n")
            
            # 只显示前几个切片
            slices_to_show = min(5, array.shape[0])
            for s in range(slices_to_show):
                f.write(f"\n    切片 [{s}] 形状: {array[s].shape}\n")
                np.savetxt(f, array[s][:10, :5], fmt='%.6e', delimiter='\t')
                if array.shape[1] > 10 or array.shape[2] > 5:
                    f.write(f"    ... (显示10×5，完整切片: {array[s].shape})\n")
                    
        elif array.ndim > 3:  # 更高维数组
            f.write(f"    {array.ndim}维数组，形状: {array.shape}\n")
            f.write(f"    将数组展平后显示前1000个元素:\n")
            flat_array = array.flatten()
            elements_to_show = min(1000, flat_array.size)
            np.savetxt(f, flat_array[:elements_to_show].reshape(-1, 1), 
                      fmt='%.6e', delimiter='\n')
            if flat_array.size > 1000:
                f.write(f"    ... 省略 {flat_array.size-1000} 个元素 ...\n")
        
        f.write("\n" + "=" * 60 + "\n")
    
    # 文件摘要
    f.write(f"\n3. 文件摘要:\n")
    f.write("-" * 40 + "\n")
    
    total_elements = 0
    total_memory = 0
    
    for key in keys:
        array = data[key]
        total_elements += array.size
        total_memory += array.nbytes
    
    f.write(f"总数组数量: {len(keys)}\n")
    f.write(f"总元素数量: {total_elements:,}\n")
    f.write(f"总内存占用: {total_memory:,} 字节 ({total_memory/1024/1024:.2f} MB)\n")
    
    f.write(f"\n4. 数组详细信息表:\n")
    f.write("-" * 80 + "\n")
    f.write(f"{'数组名':<20} {'形状':<25} {'数据类型':<15} {'元素数':<15} {'内存(MB)':<15}\n")
    f.write("-" * 80 + "\n")
    
    for key in keys:
        array = data[key]
        memory_mb = array.nbytes / 1024 / 1024
        f.write(f"{key:<20} {str(array.shape):<25} {str(array.dtype):<15} {array.size:<15,} {memory_mb:<15.2f}\n")
    
    f.write("\n" + "=" * 80 + "\n")
    f.write("数据导出完成\n")

# 关闭npz文件
data.close()

print(f"数据已保存到: {output_file}")