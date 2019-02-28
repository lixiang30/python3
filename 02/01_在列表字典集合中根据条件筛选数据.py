
# 如何在字典、列表、集合中根据条件筛选数据

"""
实际情况:
A.过滤列表[3,9,-1,10,20,-2...]中的负数
B.筛选出字典{"LiWei":79,"Jim":88,"Lucy":92...}中高于90的项
C.筛选出集合{77,89,32,20...}中能被３整除的数
"""

# 通用做法,通过循环迭代(遍历)
data = [1,5,-3,-2,6,0,9]

res = []
for x in data:
    if x >= 0:
        res.append(x)
print(res)

######################################################
#列表:filter函数   filter(lambda x:x>=0,data)
#列表:列表解析式   [x for x in data if x>=0]
#字典:字典解析　　{k:v for k,v in d.iteriterms() if v>90}
#集合:集合解析  {x for x in s if x % 3 ==0}

from random import randint
data = [randint(-10,10) for _ in range(10)]
data_filter = filter(lambda x:x>=0,data)
print(data,list(data_filter))

data_list = [x for x in data if x >=0]
print(data_list)

# timeit用法?
import timeit
# t1 = timeit(filter(lambda x:x>=0,data))
# t2 = timeit([x for x in data if x >=0])

score_student = {x:randint(60,100) for x in range(1,21)}
score_student2 = {k:v for k,v in score_student.items() if v >=90}
print(score_student)
print(score_student2)

s = set(data)
s_f = {x for x in s if x % 3 == 0}
print(s)
print(s_f)