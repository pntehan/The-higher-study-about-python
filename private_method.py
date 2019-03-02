# 数据封装和私有属性
from class_method import Date

class User:
	def __init__(self, birthday):
		self.__birthday = birthday

	def get_age(self):
		return 2019 - self.__birthday.year

# if __name__ == '__main__':
# 	user = User(Date.from_string('1998-12-21'))
# 	print(user.get_age())

# python的私有属性即是在实例属性前加__, python内部将会将此属性名称变为_classname__attr
class Student(User):
	def __init__(self, User_birth, Student_birth):
		User.__init__(self, User_birth)
		self.__birthday = Student_birth

	def get_age(self):
		return 2019 - self.__birthday.year

if __name__ == '__main__':
	# stu = Student(Date.from_string('2000-10-17'))
	# try:
	# 	print(stu.__birthday)
	# 	print('A')
	# except:
	# 	print(stu._Student__birthday)
	# 	print('B')
	# print(stu.get_age())
	stu = Student(Date(1990, 9, 21), Date(2000, 10, 17))
	print(stu._Student__birthday)
	print(stu._User__birthday)
	print(stu.get_age())