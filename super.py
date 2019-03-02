# python中类的继承顺序及初始化方式

class A:
	def __init__(self):
		print('A')

class B(A):
	def __init__(self):
		super().__init__()
		print('B')

class C(A):
	def __init__(self):
		super().__init__()
		print('C')

class D(B, C):
	def __init__(self):
		super().__init__()
		print('D')

d = D()
print(D.__mro__)

class one:
	def __init__(self):
		print('1')

class two(one):
	def __init__(self):
		one.__init__(self)
		print('2')

class three(one):
	def __init__(self):
		one.__init__(self)
		print('3')

class four(two, three):
	def __init__(self):
		two.__init__(self)
		three.__init__(self)
		print('4')

f = four()
print(four.__mro__)
