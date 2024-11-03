import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取三个 CSV 文件
df1 = pd.read_csv('target_mse.csv', header=None)
df2 = pd.read_csv('two_step_mse.csv', header=None)
df3 = pd.read_csv('one_step_mse.csv', header=None)

# 横坐标为行数
x =  range(20, 51, 10)

colors = ['r', 'g', 'b']
labels = ['target', 'two_step', 'one_step']
for i, df in enumerate([df1, df2,df3]):
    plt.plot(x, df.iloc[:, 0], label=labels[i], color=colors[i])

# 设置坐标轴范围
plt.xlim(20, 50)
plt.xticks(np.arange(min(x), max(x)+1, 10))
plt.ylim(0, 5e-5)

# 设置坐标轴标签和标题
plt.xlabel('num of UE')
plt.ylabel('average MSE')
plt.title('Comparison of Three Methods')

# 添加图例
plt.legend()

# 添加方格线
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 添加图例
plt.legend()
# plt.xticks([i for i in range(len(df1))])
# 显示图形
plt.show()