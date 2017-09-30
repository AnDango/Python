import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']   ### 显示中文
plt.rcParams['axes.unicode_minus'] = False  ## 防止坐标轴上的-号变为方块
x = np.linspace(0 , 10 , 100)
y = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

# 绘制一个图，长为12，宽为6（默认值是每个单位80像素）
plt.figure(figsize = (12 , 7))

# 在图列中自动显示$间内容
# plt.plot(x , y , label = "$sin(x)$" , color = "red" , linewidth = 2)
plt.plot(x , y , "r" , label = "$sin(x)$" , linewidth = 2)
plt.plot(x , y1 , "b" , label = "$cos(x)$")    # b表示blue，--表示线形为虚线
plt.plot(x , y2 , "y" , label = "$tan(x)$")
plt.xlabel(u"X值：弧度制角度值")       ##X坐标名称，u表示unicode编码
plt.ylabel(u"Y值：三角函数值")
plt.title(u"三角函数图像")   ##t图名称
plt.ylim(-1.2 , 1.2)   ##y上的max、min值
plt.legend()       ##显示图例
plt.savefig('fig01.png')   ##保持到当前目录
plt.show()
