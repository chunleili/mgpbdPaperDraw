import re
import os
from glob import glob

thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(thisDir+"/data")

# 确保processed目录存在
if not os.path.exists('processed'):
    os.makedirs('processed')

def process_energy_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        f_out.write("Iter Energy\n")  # 写入表头
        lines = f_in.readlines()
        # 获取初始能量值
        first_energy = None
        for line in lines:
            match = re.match(r"Frame:\d+ Iter:(\d+) Energy:([\d.]+e[+-]\d+)", line)
            if match and first_energy is None:
                first_energy = float(match.group(2))
                break
        
        # 处理所有数据，转换为相对值
        for line in lines:
            match = re.match(r"Frame:\d+ Iter:(\d+) Energy:([\d.]+e[+-]\d+)", line)
            if match:
                iter_num = int(match.group(1))
                energy = float(match.group(2))
                relative_energy = energy / first_energy  # 计算相对能量
                f_out.write(f"{iter_num} {relative_energy}\n")

def process_residual_file(input_file, output_file):
    output_time_file = output_file.replace('.txt', '_time.txt')
    
    with open(input_file, 'r') as f_in, \
         open(output_file, 'w') as f_out, \
         open(output_time_file, 'w') as f_time_out:
        
        f_out.write("Iter Residual\n")
        f_time_out.write("Iter Residual Time\n")
        
        base_time = None
        for line in f_in:
            match = re.match(r"Frame:99 Iter:(\d+) Residual:[\d.]+e[+-]\d+ Relative:([\d.]+e[+-]\d+).*FramePastTime:([\d.]+)ms", line)
            if match:
                iter_num = int(match.group(1))
                relative_residual = match.group(2)
                current_time = float(match.group(3))
                
                if iter_num == 1 and base_time is None:
                    base_time = current_time
                
                relative_time = current_time - base_time if base_time is not None else 0
                
                # 分别处理residual和time数据的迭代限制
                if iter_num <= 500:  # residual数据只取前500次迭代
                    f_out.write(f"{iter_num} {relative_residual}\n")
                if iter_num <= 10000:  # time数据取前10000次迭代
                    if 'xpbd' in input_file.lower():  # XPBD数据每100次写入一次
                        if iter_num % 100 == 0:
                            f_time_out.write(f"{iter_num} {relative_residual} {relative_time}\n")
                    else:  # AMG数据正常写入
                        f_time_out.write(f"{iter_num} {relative_residual} {relative_time}\n")



# 获取所有raw目录下的txt文件
input_files = glob('raw/residual_interval*.txt')
print(input_files)

for input_file in input_files:
    filename = os.path.basename(input_file)
    output_file = os.path.join('processed', filename)
    
    # 根据文件名判断是处理energy还是residual
    if 'energy' in filename.lower():
        process_energy_file(input_file, output_file)
    elif 'residual' in filename.lower():
        process_residual_file(input_file, output_file)
