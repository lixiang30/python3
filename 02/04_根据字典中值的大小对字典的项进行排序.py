
"""
如何根据字典中值的大小,对字典中的项进行排序?
实际案例:某班成绩{"zhangsan":80,"lisi":90,"yangmi":87...},根据分数进行排名
"""

## 使用内置函数sorted
## 利用zip将字典数据转化为元组
## 传递sorted函数的key参数

from random import randint

stu = {x:randint(60,100) for x in "ABCDEF"}
print(stu)
print(sorted(stu))
print(stu.keys())
print(stu.values())
print(zip(stu.values(),stu.keys()))
print(sorted(zip(stu.values(),stu.keys())))

print(stu.items())
print(sorted(stu.items(),key=lambda x:x[1]))