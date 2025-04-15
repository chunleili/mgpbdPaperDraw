import re
import os
from glob import glob
cwd = os.getcwd()
# thisDir = (os.path.dirname(os.path.abspath(__file__)))
os.chdir(cwd+"/data")

# 确保processed目录存在
if not os.path.exists('processed'):
    os.makedirs('processed')


def process(input_file, output_file):
    # 读取数据
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # 跳过表头，解析数据
    data = []
    for line in lines[1:]:  # 从第二行开始读取
        if line.strip():  # 跳过空行
            values = line.strip().split()
            data.append([float(values[0]), float(values[1])])
    
    # 获取第一个残差值
    first_residual = data[0][1]
    
    # 归一化处理
    normalized_data = [[x[0], x[1]/first_residual] for x in data]
    
    # 写入处理后的数据
    with open(output_file, 'w') as f:
        f.write("Iteration Residual\n")  # 使用原始表头
        for x, y in normalized_data:
            f.write(f"{int(x)} {y:.6e}\n")  # 将x转换为整数


# 获取所有raw目录下的txt文件
input_files = glob('raw/*nullspace*.txt')
print(input_files)

for input_file in input_files:
    filename = os.path.basename(input_file)
    output_file = os.path.join('processed', filename)
    
    process(input_file,output_file)
