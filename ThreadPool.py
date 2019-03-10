# # python线程池操作
# from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
# import time
#
# def get_html(page):
# 	time.sleep(1)
# 	# print('Get {} success.'.format(page))
# 	return 'Get {} success.'.format(page)
#
# executor = ThreadPoolExecutor(max_workers=3)
# # 此处创建了一个线程池，最多开启三个线程
# # task1 = executor.submit(get_html, ('http://www.PNTEHAN.com/page1'))
# # task2 = executor.submit(get_html, ('http://www.PNTEHAN.com/page2'))
# # time.sleep(3)
# # print(task1.done())
# # print(task2.done())
# # print(task1.result())
# # print(task2.result())
# # 这种方法在大量的任务需要进行时就显得十分愚笨
# urls = ['http://www.PNTEHAN.com/page'+str(i+1) for i in range(21)]
# all_task = [executor.submit(get_html, url) for url in urls]
# for task in as_completed(all_task):
# 	print(task.result())
# # 此方法使用了生成器，生成大量的任务
#
# # # ThreadPoolExecutor提供了一个map方法导入大量任务
# # for future in executor.map(get_html, urls):
# # 	print(future)
# # 	# 此处返回的是task.result()
# # wait方法用于阻塞线程执行
# wait(all_task)
# print('all task be done.')
