# # 元类编程
# # property理解使用
# class User:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		self._sex = 'woman'
#
# 	@property
# 	def get_next_year(self):
# 		return self.age + 1
#
# 	@property
# 	def sex(self):
# 		return self._sex
#
# 	@sex.setter
# 	def sex(self, value):
# 		if isinstance(value, str):
# 			self._sex = value
# 		else:
# 			raise Exception('\n[ERROR]: value must be str')
#
# if __name__ == '__main__':
# 	user = User(name='pntehan', age=21)
# 	# print('in {} file'.format(__file__))
# 	print(user.get_next_year)
# 	print(user.sex)
# 	user.sex = 'boy'
# 	print(user.sex)

# # getattr, getattribute魔法函数
# # getattr查找不到属性时调用该函数
# # getattribute在访问属性时直接进入此函数
# class User:
# 	def __init__(self, name, age, info={}):
# 		self.name = name
# 		self.age = age
# 		self.info = info
#
# 	def __getattr__(self, item):
# 		if item in self.info.keys():
# 			return self.info[item]
# 		else:
# 			raise Exception('[ERROR]: Not find {}'.format(item))
#
# 	def __getattribute__(self, item):
# 		return '控制属性访问的逻辑函数'
#
# if __name__ == '__main__':
# 	user = User('pntehan', 21, {'sex': 'man',
# 								'company': 'AI'})
# 	print(user.company)

# # 属性描述符和属性的查找过程
# import numbers
#
# class IntField:
# 	# 实现一下任一魔法函数即成为属性描述符
# 	def __get__(self, instance, owner):
# 		return self.value
#
# 	def __set__(self, instance, value):
# 		if isinstance(value, numbers.Integral):
# 			self.value = value
# 		else:
# 			raise Exception('[ERROR: Value must be Integral.')
#
# 	def __delete__(self, instance):
# 		pass
#
# class NodataIntField:
# 	# 非数据属性描述符
# 	def __get__(self, instance, owner):
# 		return self.value
#
# '''
# 数据描述符和非数据描述符的区别在于查找过程
# 如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
# 首先调用__getattribute__。如果类定义了__getattr__方法，
# 那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
# 而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
# user = User(), 那么user.age 顺序如下：
#
# （1）如果“age”是出现在User或其基类的__dict__中， 且age是data descriptor， 那么调用其__get__方法, 否则
#
# （2）如果“age”出现在user的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则
#
# （3）如果“age”出现在User或其基类的__dict__中
#
# （3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则
#
# （3.2）返回 __dict__[‘age’]
#
# （4）如果User有__getattr__方法，调用__getattr__方法，否则
#
# （5）抛出AttributeError
# '''
#
# class User:
# 	age = IntField()
# 	sex = NodataIntField()
#
# # class User:
# # 	def __init__(self, name, age, info={}):
# # 		self.name = name
# # 		self.age = age
# # 		self.info = info
# # 		self._sex = 'woman'
# #
# # 	def __getattr__(self, item):
# # 		if item in self.info.keys():
# # 			return self.info[item]
# # 		else:
# # 			raise Exception('[ERROR]: Not find {}'.format(item))
# #
# # 	@property
# # 	def sex(self):
# # 		return self._sex
# #
# # 	# 这样的限制传参类型很麻烦, 造成代码臃肿, 即引入属性描述符
# # 	@sex.setter
# # 	def sex(self, value):
# # 		if isinstance(value, str):
# # 			self._sex = value
# # 			return self._sex
# # 		else:
# # 			raise Exception('[ERROR]: Value must be str.')
#
# if __name__ == '__main__':
# 	# user = User('pntehan', 21, {'sex': 'man',
# 	# 							'company': 'AI'})
# 	# user.sex = 'man'
# 	# print(user.sex)
# 	user = User()
# 	user.age = 30
# 	print(user.age)
# 	user.sex = 'man'
# 	print(user.sex)

# __new__, __init__
class User:
	def __new__(cls, *args, **kwargs):
		# 控制对象的生成过程, 如果new方法不返回对象, 类不进行init
		print('In new')
		return super().__new__(cls)

	def __init__(self):
		# 完善对象的属性
		print('In init')

if __name__ == '__main__':
	user = User()













