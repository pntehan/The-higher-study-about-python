# # 迭代器与生成器
# # 迭代器是一种访问集合内元素的一种方式
# # 迭代器和以下标访问不一样，迭代器无法返回，是一种惰性方式访问数据
#
# from collections.abc import Iterable, Iterator
# # 可迭代类型不同于迭代器
# a = [1, 2, 3, 4]
# print(isinstance(a, Iterable))
# print(isinstance(a, Iterator))
# b = iter(a)
# print(isinstance(b, Iterable))
# print(isinstance(b, Iterator))

# class Company:
# 	def __init__(self, people):
# 		self.people = people
#
# 	def __iter__(self):
# 		return My_Iterator(self.people)
#
# 	# def __getitem__(self, item):
# 	# 	return self.people[item]
# 	#
# 	# def __len__(self):
# 	# 	return len(self.people)
#
# class My_Iterator:
# 	def __next__(self):
# 		# 真正返回迭代逻辑
# 		try:
# 			word = self.data[self._index]
# 		except IndexError:
# 			raise StopIteration
# 		self._index += 1
# 		return word
#
# 	def __init__(self, data):
# 		self.data = data
# 		self._index = 0
#
# if __name__ == '__main__':
# 	a = Company(['Mary', 'Bob', 'Jark', 'Lucy'])
# 	# b = iter(a)
# 	for item in a:
# 		# 使用循环语句时，类会调用iter()函数，iter函数首先会查找类中有无__iter__，其次查找其余魔法函数实现迭代性
# 		print(item)

# # 生成器
# # 只要存在yield即位生成器函数
# def gen_func(max):
# 	for i in range(max):
# 		yield i
#
# def gen_fib(num):
# 	n, a, b = 0, 0, 1
# 	while n < num:
# 		yield b
# 		a, b = b, a+b
# 		n += 1
#
# if __name__ == '__main__':
# 	# max = 100
# 	# gen = gen_func(max)
# 	# # 返回一个生成器对象
# 	# for i in range(max):
# 	# 	print(gen.__next__())
# 	for result in gen_fib(100):
# 		print(result)

# # python中函数的工作原理
# # python.exe会用一个叫做 PyEval_EvalFramEx(c函数)去执行foo函数， 首先会创建一个栈帧(stack frame)
# """
# python一切皆对象，栈帧对象， 字节码对象
# 当foo调用子函数 bar， 又会创建一个栈帧
# 所有的栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在
# """
# import dis
# print(dis.dis(foo))
#
# import inspect
# frame = None
#
# def foo():
#     bar()
# def bar():
#     global frame
#     frame = inspect.currentframe()
#
# foo()
# print(frame.f_code.co_name)
# caller_frame = frame.f_back
# print(caller_frame.f_code.co_name)
#
#
# def gen_func():
#     yield 1
#     name = "bobby"
#     yield 2
#     age = 30
#     return "imooc"
#
# import dis
# gen = gen_func()
# print (dis.dis(gen))
#
# print(gen.gi_frame.f_lasti)
# print(gen.gi_frame.f_locals)
# next(gen)
# print(gen.gi_frame.f_lasti)
# print(gen.gi_frame.f_locals)
# next(gen)
# print(gen.gi_frame.f_lasti)
# print(gen.gi_frame.f_locals)
















