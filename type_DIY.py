# 元类的理解以及自定义元类
# 类也是对象, type创建类的类
def say(self):
	return 'Hello, World!'

class BaseClass:
	def answer(self):
		return 'I am a BaseClass.'

# 元类是创建类的类, type就是一个元类, 继承type也是元类
User = type('User', (BaseClass,), {'name': 'pntehan',
						'say': say})

class MetaClass(type):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, *args, **kwargs)

class New(metaclass=MetaClass):
	# 在创建对象是会先进行metaclass所指定的类的逻辑, 使用type创建对象
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'DIY.'

if __name__ == '__main__':
	user = User()
	print(user.name)
	print(user.say())
	print(user.answer())
	one = New('ONE')
	print(one)





