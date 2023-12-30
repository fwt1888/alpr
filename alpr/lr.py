import matplotlib.pyplot as plt
import os
import numpy as np
import re

fi_1 = open('G:/Codes/ALPR/pytorch-YOLOv4/log/log_2023-12-19_20-57-25.txt', 'r')
iters_num = 0  # 初始化为0

lines = fi_1.readlines()

list_lr = []

for line in lines:
    if 'loss :' in line:
        iters_num += 1  # 每得到一个损失值，+1
        # print(line)
        pattern = re.compile(r'lr : (\d+\.\d+)')
        match = pattern.search(line)
        if match:
            list_lr.append(float(match.group(1)))
        # print(line)
        # break
print(len(list_lr))

plt.rc('font', family='Times New Roman', size=13)  # 全局中英文为字体“罗马字体”
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

iters_num *= 20  # 乘以10是对应txt中每20步输出一次
x = np.arange(0, iters_num, 20)  ################################ 自己估计下坐标轴x,这里10是源代码默认iter=10输出一次loss
plt.plot(x, list_lr, label="lr")

plt.grid(True)
plt.xlabel("Steps")
plt.ylabel("lr")
# plt.ylim(2.0, 10.0)
plt.legend(loc="upper right")
# plt.annotate("Loss", (-2,10), xycoords='data',xytext=(-2,10),fontsize=15)
plt.show()
