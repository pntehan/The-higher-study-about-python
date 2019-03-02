# 类方法, 实例方法, 静态方法

class Date:
	'''
	This is a class
	'''
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	def tomorrow(self):
		self.day += 1

	# 类中定义静态函数
	@staticmethod
	def parse_from_string(date_str):
		year, month, day = tuple(date_str.split('-'))
		return Date(int(year), int(month), int(day))

	@classmethod
	def from_string(cls, date_str):
		year, month, day = tuple(date_str.split('-'))
		return cls(int(year), int(month), int(day))

	def __str__(self):
		return '{}/{}/{}'.format(self.year, self.month, self.day)

if __name__ == '__main__':
	new_day = Date(2019, 12, 21)
	new_day.tomorrow()
	print(new_day)
	# 用staticmethod初始化
	day = Date.parse_from_string('2017-06-07')
	print(day)
	day2 = Date.from_string('2014-09-03')
	print(day2)