# python的自省是通过一定的机制查询到对象的内部结构
from private_method import Student
from class_method import Date

one = Student(Date(1993, 3, 1), Date(2001, 10,11))
print(one.__dict__)
print(Date.__dict__)
print(dir(one))








