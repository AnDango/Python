import numpy as np
from pandas import Series,DataFrame
import pandas as pd

s1 = Series([11,22,33,-11,-22,-33])
print(s1)
print(s1.values)
print(s1.index)

# 自定义索引
s2 = Series([1,3,6,-1,2,8] , index = ['a','c','d','e','b','g'])
print(s2)
print(s2['c'])
print(s2[['a','c','d']])

# 简洁的运算
print(s2[s2 > 1])
print(s2 * 10)
