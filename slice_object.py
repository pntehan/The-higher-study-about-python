import numbers

class Group:
	'''自定义一个可迭代的类'''
	def __init__(self, data):
		self.data = data

	def __reversed__(self):
		self.data.reverse()

	def __getitem__(self, item):
		cls = type(self)
		if isinstance(item, slice):
			return cls(data=self.data[item])
		elif isinstance(item, numbers.Integral):
			return cls(data=[self.data[item]])

	def __len__(self):
		return len(self.data)

	def __iter__(self):
		return iter(self.data)

	def __contains__(self, item):
		if item in self.data:
			return True
		else:
			return False

	# def __str__(self):
	# 	return 'Hello!'

g = Group(data=['one', 'two', 'three'])
print(g[1:2])
print(g[2])
print(reversed(g))


