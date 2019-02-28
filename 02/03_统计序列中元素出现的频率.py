
"""
如何统计序列中元素出现的频率
实际案例:
1.某随机序列[12,5,6,4,6,5,5,7...]中，找到出现次数最高的３个元素,他们出现的次数是多少？
2.对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，他们出现的次数是多少?
"""
from random import randint

data = [randint(0,20) for _ in range(20)]
print(data)
c = dict.fromkeys(data,0)
print(c)
for x in data:
    c[x] += 1
print(c)

## 将序列传入Counter的构造器,得到Counter对象是元素频度的字典
## Counter.most_common(n)方法得到频度最高的n个元素的列表

from collections import Counter
c3= Counter(data)
print(c3)
print(c3.most_common(3))