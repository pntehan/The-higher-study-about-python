# # 并发与并行
# # I/O多路复用
#
# # 非阻塞IO
# import socket
# from urllib.parse import urlparse
#
# def get_url(url):
# 	# 通过socket请求网页
# 	host, path = parse_url(url)
# 	if path == '':
# 		path = '/'
# 	data = connect_server(host, path).decode()
# 	html_headers = data.split('\r\n\r\n')[0]
# 	html_data = data.split('\r\n\r\n')[1]
# 	return html_headers, html_data
#
# def connect_server(host, path):
# 	# 通过socket连接服务器
# 	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	client.setblocking(False)
# 	try:
# 		client.connect((host, 80))
# 	except:
# 		pass
# 	while True:
# 		try:
# 			client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode())
# 			break
# 		except:
# 			pass
# 	data = b''
# 	while True:
# 		try:
# 			d = client.recv(1024)
# 		except:
# 			continue
# 		if d:
# 			data += d
# 		else:
# 			break
# 	return data
#
# def parse_url(url):
# 	# 分析网页地址，返回域名和路径
# 	url = urlparse(url)
# 	return url.netloc, url.path
#
# if __name__ == '__main__':
# 	url = 'http://www.baidu.com/'
# 	html_headers, html_data = get_url(url)
# 	print(html_headers)
# 	print(html_data)


# 使用select完成http请求
# select+回调+事件循环

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
urls = []
stop = True

class Fetcher:
	def get_url(self, url):
		self.url = url
		url = urlparse(url)
		self.host = url.netloc
		self.path = url.path
		self.data = b""
		if self.path == '':
			self.path = '/'
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.setblocking(False)
		try:
			self.client.connect((self.host, 80))
		except:
			pass
		selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

	def connected(self, key):
		selector.unregister(key.fd)
		self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode())
		selector.register(self.client.fileno(), EVENT_READ, self.readable)

	def readable(self, key):
		d = self.client.recv(1024)
		if d:
			self.data += d
		else:
			selector.unregister(key.fd)
			data = self.data.decode('utf-8')
			html_data = data.split('\r\n\r\n')[1]
			print(html_data)
			self.client.close()
			urls.remove(self.url)
			if not urls:
				global stop
				stop = False

def loop():
	# 事件循环，不停请求socket状态并返回相应函数
	while stop:
		ready = selector.select()
		for key, mask in ready:
			call_back = key.data
			call_back(key)

if __name__ == '__main__':
	for i in range(36):
		url = ''
		urls.append(url)
		fetcher = Fetcher()
		fetcher.get_url(url)
	loop()