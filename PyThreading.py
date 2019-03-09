# # GIL is global interpreter lock
# # gil使得python中同一时刻只有一个线程在一个cpu上执行，无法将多个线程映射到多个cpu上
#
# total = 0
#
# def add():
# 	global total
# 	for i in range(1000000):
# 		total += 1
#
# def desc():
# 	global total
# 	for i in range(1000000):
# 		total -= 1
#
# import threading
# thread1 = threading.Thread(target=add)
# thread2 = threading.Thread(target=desc)
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
# print(total)
# # 通过以上实例可知，GIL不会一直占有线程，他会在执行到多少语句后释放线程，这本身就算不稳定的
# # 不过在I/O操作比较频繁时，多线程还是有效的

# # 多线程编程
# # 1.通过thread类实例化
# import time
# import threading
#
# def get_html(url):
# 	print('开始获取网页内容...')
# 	time.sleep(2)
# 	print('已获取到网页内容...')
#
# def get_url(url):
# 	print('开始获取网页地址...')
# 	time.sleep(2)
# 	print('已获取到网页地址...')
#
# if __name__ == '__main__':
# 	thread1 = threading.Thread(target=get_html, args=('',))
# 	thread2 = threading.Thread(target=get_url, args=('',))
# 	start_time = time.time()
# 	thread1.start()
# 	thread2.start()
# 	thread1.join()
# 	thread2.join()
# 	print('耗时{}...'.format(time.time()-start_time))
# 	# 此类只使用比较简单逻辑线程时

# # 2.通过继承thread来实现多线程
# import time
# import threading
#
# class get_html(threading.Thread):
#
# 	def run(self):
# 		# 重写run方法
# 		print('开始获取网页内容...')
# 		time.sleep(2)
# 		print('已获取到网页内容...')
#
# class get_url(threading.Thread):
#
# 	def run(self):
# 		# 重写run方法
# 		print('开始获取网页地址...')
# 		time.sleep(2)
# 		print('已获取到网页地址...')
#
# if __name__ == '__main__':
# 	thread1 = get_html()
# 	thread2 = get_url()
# 	start_time = time.time()
# 	thread1.start()
# 	thread2.start()
# 	thread1.join()
# 	thread2.join()
# 	print('耗时{}...'.format(time.time()-start_time))
# 	# 此处适用于逻辑比较复杂的多线程编程时

# # 线程间通信
# # 通过queue
#
# import time
# import threading
#
# url_list = []
#
# def get_html(url_list):
# 	while True:
# 		if len(url_list) != 0:
# 			url = url_list.pop()
# 			print('开始获取{}内容...'.format(url))
# 			time.sleep(2)
# 			print('已获取到{}内容...'.format(url))
#
# def get_url(url_list):
# 	while True:
# 		print('开始获取网页地址...')
# 		time.sleep(2)
# 		for i in range(20):
# 			url_list.append('http://www.PNTEHAN.com/movie{}'.format(i))
# 		print('已获取到网页地址...')
#
# # 1.共享变量方法，对变量而言并不安全
#
# if __name__ == '__main__':
# 	thread1 = threading.Thread(target=get_url, args=(url_list, ))
# 	thread2 = threading.Thread(target=get_html, args=(url_list,))
# 	thread1.start()
# 	thread2.start()
# 	thread1.join()
# 	thread2.join()

import time
import threading
from queue import Queue

def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        url = queue.get()
        # for url in detail_url_list:
        print("get detail html from {} started".format(url))
        time.sleep(2)
        print("get detail html from {} end".format(url))

def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://www.PNTEHAN.com/Game-{id}".format(id=i))
        print("get detail url end")

if  __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
    thread_detail_url.start()
    html_thread.start()
    start_time = time.time()
    # detail_url_queue.task_done()
    detail_url_queue.join()
    thread_detail_url.join()
    html_thread.join()
    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time()-start_time))


























