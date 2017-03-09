# -*- coding: utf-8 -*- 
from urllib import request

import http.cookiejar

url = 'http://www.baidu.com'

print('第一次:')

response1 = request.urlopen(url)

print(response1.getcode())

print(len(response1.read()))




print('第二次')

req = request.Request(url)

req.add_header('user-agent', 'Mozilla/5.0')

response2 = request.urlopen(req)

print(response2.getcode())

print(len(response2.read()))



print('第三次')

cj = http.cookiejar.CookieJar()

opener = request.build_opener(request.HTTPCookieProcessor(cj))

request.install_opener(opener)

response3 = request.urlopen(url)

print(response3.getcode())

print(cj)

print(response3.read())