
"""
如何为元组中的每个元素命名,提高程序的可读性?
实际案例:学生信息系统中数据为固定格式:(名字,年龄,性别,邮箱地址...)
学生数量很大为了减小存储开销,对每个学生信息用元组表示:
("Jim",16,"male","jim123@mail.com")
("liwei",17,"male","liwei@qq.com")
...
访问时,我们使用索引(index)访问,大量索引会降低程序可读性,如何解决这个问题?
"""
## 方案一:定义类似于其他语言的枚举类型,也就是定义一系列数值常量
## 方案二:使用标准库中collections.namedtuple替代为内置tuple
student = ("bozai",27,"CQU","chengdu","123456789@qq.com")
NAME = 0
AGE = 1
SCHOOL = 2
ADDR = 3
EMAIL = 4

print(student[NAME])

from collections import namedtuple

Student = namedtuple("student",["name","age","school","address","email"])
s = Student("dabozai",26,"CQU_University","chengdu","123489@qq.com")
print(s)
print(s.address)
print(isinstance(s,tuple))
