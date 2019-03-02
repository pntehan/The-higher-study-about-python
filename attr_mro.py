# 类和实例属性的查找顺寻
class A:
	name = 'A'
	def __init__(self):
		self.name = 'obj'

a = A()
print(a.name)
print(A.name)
# 实例属性的查找是自下而上的, 现在实例属性中查找, 再在类属性之中查找

# C3算法, 确定类的查找顺序
class D:
	pass

class C(D):
	pass

class B(D):
	pass

class A(B, C):
	pass

print(A.__mro__)

class five:
	pass

class four:
	pass

class three(five):
	pass

class two(four):
	pass

class one(two, three):
	pass

print(one.__mro__)
