# 抽象基类
# 抽象基类的方法必须重写，抽象基类无法实例化

class Company(object):
	def __init__(self, employee_list):
		self.employee = employee_list

	def __len__(self):
		return len(self.employee)

from collections.abc import Sized

com = Company(['one', 'two'])
hasattr(com, '__len__')
isinstance(com, Sized)

# 如何模拟一个抽象基类
import abc

class CacheBase(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def get(self, key):
		pass

	@abc.abstractmethod
	def set(self, key, value):
		pass

class test(CacheBase):
	def get(self, key):
		print('已重写get函数')

	def set(self, key, value):
		print('已重写set函数')

one = test()








