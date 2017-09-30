from pandas import Series , DataFrame
import numpy as np
import pandas as pd

# count	统计非NA的数量
# describe	统计列的汇总信息
# min、max	计算最小值和最大值
# sum	求总和
# mean	求平均数
# var	样本的方差
# std	样本的标准差

inputfile = './stud_score.csv'
data = pd.read_csv(inputfile)
# 其他参数，
### header=None 表示无标题,此时缺省列名为整数；如果设为0，表示第0行为标题
### names，encoding，skiprows等

# 读取excel文件，可用 read_excel
df = DataFrame(data)

print("\n")
# 显示前三行
print("显示前三行")
print(df.head(3))

print("\n")
# 统计数量
print("统计数量")
print(df.count())

print("\n")
# 统计列的汇总信息
print("统计列的汇总信息")
print(df['sub_score'].describe())

print("\n")
# 求样本标准差
print("求样本标准差")
print(df['sub_score'].std())