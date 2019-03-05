# python的socket通信之http请求
import socket
from urllib.parse import urlparse

def get_url(url):
	# 通过socket请求网页
	host, path = parse_url(url)
	if path == '':
		path = '/'
	data = connect_server(host, path).decode()
	html_headers = data.split('\r\n\r\n')[0]
	html_data = data.split('\r\n\r\n')[1]
	return html_headers, html_data

def connect_server(host, path):
	# 通过socket连接服务器
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((host, 80))
	client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode())
	data = b''
	while True:
		d = client.recv(1024)
		if d:
			data += d
		else:
			break
	return data

def parse_url(url):
	# 分析网页地址，返回域名和路径
	url = urlparse(url)
	return url.netloc, url.path


url = 'http://www.baidu.com/'
html_headers, html_data = get_url(url)
print(html_headers)
print(html_data)
