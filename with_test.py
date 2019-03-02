# 上下文管理器
class test:
	def __enter__(self):
		print('START')

	def __exit__(self, exc_type, exc_val, exc_tb):
		print('FINISH')

import contextlib

@contextlib.contextmanager
def file_open(fileName):
	print("{} START OPEN...".format(fileName))
	yield {}
	print("{} OPENED...".format(fileName))

if __name__ == '__main__':
	with test() as t:
		print('DOING')
	with file_open('F:/Python/ClassOne.mp4') as f:
		print("{} OPENING...".format('F:/Python/ClassOne.mp4'))