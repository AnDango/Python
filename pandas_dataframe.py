import numpy as np
from pandas import Series,DataFrame
import pandas as pd

# 自动生成一个3行4列的DataFrame，并定义其索引（如果不指定，缺省为整数索引）及列名
print("自动生成一个3行4列的DataFrame，并定义其索引（如果不指定，缺省为整数索引）及列名")
d1 = DataFrame(np.arange(12).reshape((3,4)),
               index=['a','b','c'],
               columns=['a1','a2','a3','a4'])
print(d1)
print(d1.index)
print(d1.columns)
print(d1.values)

print("\n")
# 生成DataFrame
print("生成DataFrame")
data = {'name':['zhanghua','liuting','gaofei','hedong'],
      'age':[40,45,50,46],
      'addr':['jianxi','pudong','beijing','xian']}
d2 = DataFrame(data)
d3 = DataFrame(data,
               columns=['name','age','addr'],
               index=['a','b','c','d'])
print(d2)
print(d3)

print("\n")
# 根据列或索引进行过滤
print("根据列或索引进行过滤")
print(d3[['name','age']])
print(d3['a':'c'])
print(d3[1:3])
print(d3[d3['age'] > 40])

print("\n")
# 根据列和索引同时进行过滤
print("根据列和索引同时进行过滤")
print(d3.ix[['a' , 'c'] , ['name' , 'age']])
print(d3.ix['a' : 'c' , ['name' , 'age']])
print(d3.ix[0 : 3 , ['name' , 'age']])

print("\n")
# 删除数据
print("删除数据")
print(d3.drop('d' , axis = 0))   ### 删除行，如果欲删除列，使axis=1即可
print(d3) # 是从副本中删除，原数据没有变化

print("\n")
# 增加数据
print("增加数据")
d4 = d3.append({'name':'wangkuan',
                'age':38,
                'addr':'henan'},
               ignore_index=True)   # 注意需要ignore_index=True，否则会报错
print(d4)
d4.index = ['a' , 'b' , 'c' , 'd' , 'e']
d4.ix['e' , 'age'] = 39
print(d4)