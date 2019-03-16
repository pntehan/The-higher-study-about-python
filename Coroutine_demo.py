# def simple_coroutine():
# 	for i in range(3):
# 		x = yield i + 1
# 		print('从调用方获取数据:{}.'.format(x))
#
# my_coro = simple_coroutine()
# first = next(my_coro)
# for i in range(5):
# 	try:
# 		y = my_coro.send(i)
# 		print('从生成器获取的数据:{}.'.format(y))
# 	except StopIteration:
# 		print('生成器的数据拉取完毕.')
#
# print('生成器最初获取的数据是:{}.'.format(first))

# from inspect import getgeneratorstate
# from time import sleep
# import threading
#
# def get_state(coro):
# 	print('其他线程生成器的状态:{}'.format(getgeneratorstate(coro)))
#
# def simple_coroutine():
# 	for i in range(3):
# 		sleep(0.5)
# 		x = yield i + 1
#
# my_coro = simple_coroutine()
# print('生成器的初始状态:{}'.format(getgeneratorstate(my_coro)))
# first = next(my_coro)
# for i in range(5):
# 	try:
# 		my_coro.send(i)
# 		print('主线程生成器的初始状态:{}'.format(getgeneratorstate(my_coro)))
# 		t = threading.Thread(target=get_state, args=(my_coro,))
# 		t.start()
# 	except StopIteration:
# 		print('生成器的数据拉取完毕.')
#
# print('生成器的最后状态:{}'.format(getgeneratorstate(my_coro)))

# def first_gen():
# 	for c in 'AB':
# 		yield c
# 	for i in range(3):
# 		yield i
#
#
# print(list(first_gen()))
#
# def second_gen():
# 	yield from 'AB'
# 	yield from range(3)
#
#
# print(list(second_gen()))

# def chain(*args):
# 	for i in args:
# 		yield from i
#
# s = 'ABC'
# t = tuple(range(3))
# print(list(chain(s, t)))

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
	for x in items:
		if isinstance(x, Iterable) and not isinstance(x, ignore_types):
			yield from flatten(x)
		else:
			yield x

# items = [1, 2, [3, 4, [5, 6], 7], 8]
# for i in flatten(items):
# 	print(i)

# items = ['bobby', 'lucy', ['Bob', ['Soul', 'Hope'], 'Jerk', 'Asshole', ['Amazing'], 'No'], 'END']
# for i in flatten(items):
# 	print(i)

# def my_Sum(items):
# 	yield sum(items)
#
# def main(*args):
# 	for i in args:
# 		if isinstance(i, Iterable) and not isinstance(i, str):
# 			yield from my_Sum(i)
#
# l = [1, 2, 3, 4, 5]
# print(list(main(l, l, l)))

from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
	# 计算平均值
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield
		if term is None:
			break
		total += term
		count += 1
		average = total/count
	return Result(count=count, average=average)

def grouper(result, key):
	# 委托生成器
	while True:
		result[key] = yield from averager()

def main(data):
	results = {}
	for key, values in data.items():
		group = grouper(results, key)
		next(group)
		for value in values:
			group.send(value)
		group.send(None)
	report(results)

def report(results):
	# 输出数据
	for key, result in sorted(results.items()):
		group, unit = key.split(";")
		print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))

data = {
	'girls;kg': [40.9, 38.5, 44.3],
	'girls;m': [1.6, 1.51, 1.4],
	'boys;kg': [39.0, 40.8],
	'boys;m': [1.38, 1.5],
}

if __name__ == '__main__':
	main(data)
















