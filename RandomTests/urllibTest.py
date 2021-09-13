# coding = utf-8

import urllib.request
import urllib.parse


# get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))


# post请求
# post_data = bytes(urllib.parse.urlencode({123:321}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=post_data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=3)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("Err: timeout")

# response = urllib.request.urlopen("http://www.baidu.com", timeout=3)
# #print(response.status)
# print(response.getheaders("Server"))


# url = "http://www.httpbin.org/post"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
# }
# data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
# request = urllib.request.Request(url=url, data=data, headers=header, method="POST")
# response = urllib.request.urlopen(request)
# print(response.read().decode("utf-8"))


url = "http://www.baidu.com"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
}
# data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
request = urllib.request.Request(url=url, headers=header)
# request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request,timeout=2)
f = open("baidu.html","w",encoding="utf-8")
f.write(response.read().decode("utf-8"))