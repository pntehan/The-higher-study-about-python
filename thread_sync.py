# # python线程同步
# from threading import Lock
# import threading
# # 在一个线程运行时，锁住其他线程
#
# total = 0
# # 初始化锁
# lock = Lock()
#
# def add():
# 	global total
# 	# 获取锁
# 	global lock
# 	for i in range(1000000):
# 		# 加锁，锁住变量，此时进行此段代码时，其他锁不能运行
# 		lock.acquire()
# 		total += 1
# 		# 释放锁
# 		lock.release()
#
# def desc():
# 	global total
# 	for i in range(1000000):
# 		lock.acquire()
# 		total -= 1
# 		lock.release()
#
# thread1 = threading.Thread(target=add)
# thread2 = threading.Thread(target=desc)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(total)
# # 锁影响性能，获取锁和释放锁需要时间
# # 锁可能造成死锁，在一个锁获取后，其他线程无法获取到锁，如果还未释放锁时就再次获取锁就会造成死锁
# # 死锁还有一种情况是互相等待，比如一个锁先获取a再获取b，另一个锁先获取b再获取a，他们就会相互等待对方释放变量
#
# from threading import RLock
# # RLock在同一个线程里面可以多次调用acquire
#
# rlock = RLock()
# def start(rlock):
# 	rlock.acquire()
# 	print('Start...')
# 	doSomething(rlock)
# 	rlock.release()
#
# def doSomething(rlock):
# 	rlock.acquire()
# 	print('Fuck You!')
# 	rlock.release()
#
# thread3 = threading.Thread(target=start, args=(rlock,))
# thread3.start()
# thread3.join()

# 条件变量，用于复杂的线程间同步，依旧是同步锁

# from threading import *
#
#
# class MGK(Thread):
# 	def __init__(self, Con):
# 		super().__init__(name='MGK')
# 		self.Con = Con
#
# 	def run(self):
# 		with self.Con:
# 			print('{}: Sup?'.format(self.name))
# 			self.Con.notify()
# 			self.Con.wait()
#
#
# class Shady(Thread):
# 	def __init__(self, Con):
# 		super().__init__(name='Shady')
# 		self.Con = Con
#
# 	def run(self):
# 		with self.Con:
# 			self.Con.wait()
# 			print('{}: Not bad, son.'.format(self.name))
# 			self.Con.notify()
#
#
# if __name__ == '__main__':
# 	Con = Condition()
# 	mgk = MGK(Con)
# 	shady = Shady(Con)
# 	shady.start()
# 	mgk.start()

# semaphore 是用于控制进入数量的值

from threading import *
import time

class GetHtml(Thread):
	def __init__(self, sem, url):
		super().__init__()
		self.url = url
		self.sem = sem

	def run(self):
		for i in range(21):
			self.sem.acquire()
			Do = GetContent('{}/movie{}'.format(self.url, i), self.sem)
			Do.start()


class GetContent(Thread):
	def __init__(self, url, sem):
		super().__init__()
		self.url = url
		self.sem = sem

	def run(self):
		time.sleep(1)
		print('{} be done...'.format(self.url))
		self.sem.release()

if __name__ == '__main__':
	sem = Semaphore(3)
	gethtml = GetHtml(sem, 'http://www.PNTEHAN.com')
	gethtml.start()










