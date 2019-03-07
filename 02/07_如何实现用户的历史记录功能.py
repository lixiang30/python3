
# 如何实现用户的历史记录功能

"""
很多应用程序都有浏览用户的历史记录功能,例如:
浏览器可以查看最近访问过的网页
视频播放器可以查看最近播放过的视频文件
Shell可以查看用户输入过的命令
...
现在我们制作一个简单的猜数字的小游戏,添加历史记录功能,显示用户最近猜过的数字,如何实现?
"""
# 使用容量为n的队列存储历史记录
# 使用标准库collections中的deque，它是一个双端循环队列
# 程序退出前,可以使用pickle将队列对象存入文件,再次运行程序时将其导入





# N = randint(0,100)
# from collections import deque
# q = deque([],5)
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# q.append(5)
# q.append(6)
# q.append(7)
# print(q)

from collections import deque
from random import randint

N = randint(0,100)
history = deque([],5)

def guess(k):
    if k == N:
        print("right")
        return True
    if k < N:
        print("%s is less than N" % k)
    else:
        print("%s is greater than N" % k)
        return False

while True:
    line = input("please input a number:")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
        elif line == "history" or line == "h?":
            print(list(history))
