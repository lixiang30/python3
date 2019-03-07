
# 如何让字典保持有序
"""
某编程竞赛系统,对参赛选手编程题进行计时,选手完成题目后，把该选手解题用时记录到字典中,以便赛后按选手排名查询成绩.
(答题用时越短,成绩越优．)
{"Liwei":(2,43),"HanMeimei":(5,52),"JIM":(1,39)...}
比赛结束后,需按排名顺序依次打印选手成绩,如何实现
"""


# d = {}
#
# d["JIM"] = (1,35)
# d["Leo"] = (2,37)
# d["Bob"] = (3,40)
#
# for k in d:
#     print(k)
#
#
# from collections import OrderedDict
#
# d1 = OrderedDict()
# d1["JIM"] = (1,35)
# d1["Leo"] = (2,37)
# d1["Bob"] = (3,40)
# for k2 in d1:
#     print(k2)

d = {}
import time
from random import randint

players = list("ABCDEFGH")

start = time.time()
for i in range(8):
    input()
    p = players.pop(randint(0,7 - i))
    end = time.time()
    print(i + 1,p,end-start)
    d[p] = (i+1,end)

print("="*30)

for k in d:
    print(k,d[k])
