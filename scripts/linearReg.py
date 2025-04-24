import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 数据准备
X = np.array([12e3, 50e3, 100e3, 270e3, 558e3, 850e3]).reshape(-1, 1)
y_time = np.array([3731, 8277, 9497, 15089, 24359, 182271])
y_iter_time = np.array([67.84, 121.72, 153.18, 255.75, 451.09, 637.31])
y_iter = np.array([55, 68, 62, 59, 54, 286])

# 创建并拟合线性回归模型
model_time = LinearRegression()
model_time.fit(X, y_time)

model_iter_time = LinearRegression()
model_iter_time.fit(X, y_iter_time)

model_iter = LinearRegression()
model_iter.fit(X, y_iter)

# 打印结果
print("总时间线性回归：")
print(f"斜率: {model_time.coef_[0]:.4e}")
print(f"截距: {model_time.intercept_:.4e}")
print(f"R²分数: {model_time.score(X, y_time):.4e}")

print("\n每迭代时间线性回归：")
print(f"斜率: {model_iter_time.coef_[0]:.4e}")
print(f"截距: {model_iter_time.intercept_:.4e}")
print(f"R²分数: {model_iter_time.score(X, y_iter_time):.4e}")

print("\n迭代次数线性回归：")
print(f"斜率: {model_iter.coef_[0]:.4e}")
print(f"截距: {model_iter.intercept_:.4e}")
print(f"R²分数: {model_iter.score(X, y_iter):.4e}")