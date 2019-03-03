# # 深入理解python的set和dict
# # dict的继承关系
# from collections.abc import MutableMapping
# a = dict()
# print(isinstance(a, dict))
# print(isinstance(a, MutableMapping))
# # dict常用方法
# a = {'mary': 45, 'mark': 32, 'lucy': 25}
# print(a)
# b = a.copy()
# a.clear()
# print(a)
# print(b)
# l = ['a', 'b', 'c']
# c = b.fromkeys(l, 1)
# print(c)
# print(c.get('d', 1))
# c.setdefault('e', 2)
# print(c)
# b.update(c)
# print(b)
# # 具体用法查看源码即可

# # dict子类
# # python中不建议直接继承数据结构
# from collections import UserDict
#
# class MyDict(dict):
# 	def __setitem__(self, key, value):
# 		super().__setitem__(key, value+1)
#
# mydict = MyDict(one=9)
# print(mydict)
#
# class MyDict(UserDict):
# 	def __setitem__(self, key, value):
# 		super().__setitem__(key, value+1)
#
# mydict = MyDict(one=9)
# print(mydict)

# # set and frozenset
# # set为集合, frozenset为不可变集合
# # set无序不重复
# s = set('abbccdd')
# s.add('e')
# print(s)
# ss = frozenset('abbccd')
# # ss.add('e')
# print(ss)
# # 向set添加数据
# s2 = set('zjkkzza')
# print(s & s2)
# s.update(s2)
# print(s)
# r = s.difference(s2)
# print(r)
# print(s - s2)
# print(s2.issubset(s))






