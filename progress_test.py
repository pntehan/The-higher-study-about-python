# # 多进程编程
# # 进程切换代价高于线程切换，多进程是多cpu操作，所以在耗cpu操作时用多进程，耗IO操作用多线程
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
# import time
#
#
# def fib(num):
# 	if num <= 2:
# 		return 1
# 	else:
# 		return fib(num-1) + fib(num-2)
#
#
# if __name__ == '__main__':
# 	with ThreadPoolExecutor(max_workers=3) as executor:
# 		start_time = time.time()
# 		for future in executor.map(fib, [num for num in range(20, 41)]):
# 			print('Executor Result: {}'.format(future))
# 		end_time = time.time()
# 		print('Use time is %.2fs'%(end_time-start_time))
# 	with ProcessPoolExecutor(max_workers=3) as executor:
# 		start_time = time.time()
# 		for future in executor.map(fib, [num for num in range(20, 41)]):
# 			print('Executor Result: {}'.format(future))
# 		end_time = time.time()
# 		print('Use time is %.2fs'%(end_time-start_time))
#
# 	# 通过斐波那契这种消耗运算的算法实战可得多进程在耗cpu情况下性能优于多线程

# import time
# import multiprocessing
#
# def get_html(n):
# 	time.sleep(n)
# 	print('Sub progess executing...')
# 	return n
#
# if __name__ == '__main__':
# 	# progress = multiprocessing.Process(target=get_html, args=(1, ))
# 	# progress.start()
# 	# print(progress.pid)
# 	# progress.join()
# 	# print('Main progress end.')
# 	# # 进程池使用
# 	# pool = multiprocessing.Pool(multiprocessing.cpu_count())
# 	# result = pool.apply_async(get_html, (1, ))
# 	# pool.close()
# 	# pool.join()
# 	# print('{} sleep be done.'.format(result.get()))
# 	# count = [1, 3, 2]
# 	# # imap方法，按照参数传入顺序返回结果
# 	# pool = multiprocessing.Pool(multiprocessing.cpu_count())
# 	# for result in pool.imap(get_html, count):
# 	# 	print('{} sleep be done.'.format(result))
# 	# # imap_unordered方法按照进程结束顺序返回结果
# 	# pool = multiprocessing.Pool(multiprocessing.cpu_count())
# 	# for result in pool.imap_unordered(get_html, count):
# 	# 	print('{} sleep be done.'.format(result))

# 多进程间的通信
# 共享全局变量在多进程是不可以的

# from multiprocessing import Process, Queue
# Queue不能直接用于进程池

# def producer(a, pipe):
# 	a += 1
# 	# queue.put(a)
# 	pipe.send(a)
# 	print('a = {}'.format(a))
#
# def consumer(pipe):
# 	# a = queue.get()
# 	a = pipe.recv()
# 	a -= 1
# 	print('a = {}'.format(a))
#
#
# if __name__ == '__main__':
# 	# queue = Queue()
# 	# p = Process(target=producer, args=(1, queue))
# 	# c = Process(target=consumer, args=(queue, ))
# 	# p.start()
# 	# c.start()
# 	# p.join()
# 	# c.join()
# 	# from multiprocessing import Manager, Pool
# 	# queue = Manager().Queue()
# 	# # 用于进程池的进程通信
# 	# pool = Pool(2)
# 	# pool.apply_async(producer, (1, queue))
# 	# pool.apply_async(consumer, (queue, ))
# 	# pool.close()
# 	# pool.join()
# 	# 利用pipe实现进程间通信，性能也高于queue
# 	# import multiprocessing
# 	# recevie_pipe, send_pipe = multiprocessing.Pipe()
# 	# p = multiprocessing.Process(target=producer, args=(1, send_pipe))
# 	# c = multiprocessing.Process(target=consumer, args=(recevie_pipe, ))
# 	# p.start()
# 	# c.start()
# 	# p.join()
# 	# c.join()

# 多进程的内存共享
import multiprocessing
from multiprocessing import Manager

def give_value(p_dict, key, value):
	p_dict[key] = value

if __name__ == '__main__':
	p_dict = Manager().dict()
	progress1 = multiprocessing.Process(target=give_value, args=(p_dict, 'Mary', 21))
	progress2 = multiprocessing.Process(target=give_value, args=(p_dict, 'Lucy', 22))
	progress1.start()
	progress2.start()
	progress1.join()
	progress2.join()
	print(p_dict)









