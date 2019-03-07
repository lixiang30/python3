

# 如何快速找到多个字典中的公共键
"""
西班牙足球甲级联赛,每轮球员进球统计:
第一轮:{"苏亚雷斯":1,"梅西":2,"本泽马":1,"C罗":3...}
第二轮:{"苏亚雷斯":1,"C罗":1,"格里兹曼":2,"贝尔":1...}
第三轮:{"苏亚雷斯":1,"托雷斯":2,"贝尔":1,"内马尔":1...}
...
统计出前N轮,每场比赛都有的球员.
"""
from random import randint,sample

str = sample("abcdefg",randint(3,6))
print(str)
s1 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}
s2 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}
s3 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}
print(s1)
print(s2)
print(s3)

# 方式一:通过迭代字典key的方式和in来判断是否共享key
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

print(res)

# 方法二 :键集合交集
dict3 = s1.keys()&s2.keys()&s3.keys()
print(dict3)

# 方法３:使用map获得keys集合，然后去所有集合的交集
# 即使用reduce函数,取所有字典的keys的集合的交集
dict2 = map(dict.keys,[s1,s2,s3]) #求得字典的viewkeys集合

# lambda a,b:a & b,map(dict.viewkeys,[s1,s2,s3])
from functools import reduce
dict2 = reduce(lambda a,b:a & b,map(dict.keys,[s1,s2,s3])) # 通过求交集的方式求得公共键
print(dict2)