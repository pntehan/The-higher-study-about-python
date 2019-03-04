# # python的变量是一个指针
# a = 1
# # 将a指向1
# a = 'abc'
# # 将a指向'abc'字符串
# # Python先生成对象再将变量指向这个对象
# b = 'abc'
# print(a is b)# 因指向同一对象, 即地址相同

# # is和==的区别
# a = [1, 2, 3, 4]
# b = [1, 2, 3, 4]
# print(id(a), id(b))
# print(a is b)
# print(a == b)
# # 在python中每新建一个对象地址将不一样, 而is直接在地址比较
# # 但是在小型的数据结构中不会新建新的对象, 如上方'abc'
# # ==使用__eq__魔法函数, 比较内部值是否相等

# # del语句和垃圾回收
# a = 1
# b = a
# del a
# del b
# # 在新建一个对象是有几个变量指向它, 它的计数器将依此加一, 当变量全部删除后, 此对象才会被回收
# # python的类可以重写del方法, 在回收此类时会调用魔法函数__del__里的逻辑
# class A:
# 	def __del__(self):
# 		pass

# python文件中参数传递的经典错误
def add(a, b):
	a += b
	return a

class A:
	def __init__(self, data=[]):
		self.data = data

	def add(self, value):
		self.data.append(value)

if __name__ == '__main__':
	a = A([1, 2, 3, 4])
	print(a.data)
	a.add(5)
	print(a.data)
	b = A()
	b.add(1)
	print(b.data)
	c = A()
	c.add(2)
	print(b.data)
	print(c.data)
	# 此处的相同是因为, 在传参是没有指定列表, 而默认新建列表[]为小型数据结构, 导致b, c指向的对象为同一对象
	# a = 1
	# b = 2
	# c = add(a, b)
	# print(c, a, b)
	# a = [1, 2]
	# b = [3, 4]
	# c = add(a, b)
	# print(c, a, b)
	# print(c is a)
	# # 因list可修改, 而+=是修改a而不是新建对象, 则对象指向相同
	# a = (1, 2)
	# b = (3, 4)
	# c = add(a, b)
	# print(c, a, b)















