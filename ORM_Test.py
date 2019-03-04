# 定义一个ORM
# 首先定义属性描述符
from numbers import Integral

class Field:
	pass

class StrField(Field):
	def __init__(self, db_column, max_length=100):
		self._value = None
		self.max_length = max_length
		self.db_column = db_column

	def __get__(self, instance, owner):
		return self._value

	def __set__(self, instance, value):
		if isinstance(value, str):
			if len(value) > self.max_length:
				raise Exception('[ERROR]: Value len must smaller than max_length.')
			else:
				self._value = value
		else:
			raise Exception('[ERROR]: Value must be String.')

	def __delete__(self, instance):
		pass

class IntField(Field):
	def __init__(self, db_column, min_value=-1000000, max_value=1000000):
		self._value = None
		self.min_value = min_value
		self.max_value = max_value
		self.db_column = db_column
		if not isinstance(min_value, Integral):
			raise Exception('[ERROR]: min_value must be Integral.')
		else:
			if min_value < 0:
				raise Exception('[ERROR]: min_value must be positive Int.')
		if not isinstance(max_value, Integral):
			raise Exception('[ERROR]: max_value must be Integral.')
		else:
			if max_value < 0:
				raise Exception('[ERROR]: max_value must be positive Int.')
		if min_value > max_value:
			raise Exception('[ERROR]: max_value must be bigger than min_value.')

	def __get__(self, instance, owner):
		return self._value

	def __set__(self, instance, value):
		if not isinstance(value, Integral):
			raise Exception('[ERROR]: Value must be Integral.')
		else:
			if value < self.max_value and value > self.min_value:
				self._value = value
			else:
				raise Exception('[ERROR]: Value must between min_value and max_value.')

class ModelMetaClass(type):
	def __new__(cls, name, bases, attrs, **kwargs):
		if name == 'BaseModel':
			return super().__new__(cls, name, bases, attrs, **kwargs)
		fields = {}
		for key, value in attrs.items():
			if isinstance(value, Field):
				fields[key] = value
		attrs_meta = attrs.get('Meta', None)
		_meta = {}
		db_table = name.lower()
		if attrs is not None:
			table = getattr(attrs_meta, 'db_table', None)
			if table is not None:
				db_table = table
		_meta['db_table'] = db_table
		attrs['_meta'] = _meta
		attrs['fields'] = fields
		del attrs['Meta']
		return super().__new__(cls, name, bases, attrs, **kwargs)

class BaseModel(metaclass=ModelMetaClass):
	def __init__(self, *args, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)
		return super().__init__()

	def save(self):
		fields = []
		values = []
		for key, value in self.fields.items():
			db_column = value.db_column
			if db_column is None:
				db_column = key.lower()
			fields.append(db_column)
			value = getattr(self, key)
			values.append(str(value))
		sql = 'insert {}({}) value ({})'.format(db_column, ','.join(fields), ','.join(values))
		print(sql)
		# 后续可以使用pymysql直接创建表写入

class User(BaseModel):
	name = StrField(db_column='name', max_length=10)
	age = IntField(db_column='age', min_value=0, max_value=100)

	class Meta:
		db_table = 'user'

if __name__ == '__main__':
	user = User(name='one', age=28)
	user.save()