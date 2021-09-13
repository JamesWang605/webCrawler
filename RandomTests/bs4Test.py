# coding = utf-8
import re

from bs4 import BeautifulSoup


file = open("./baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")

# print(bs.title.attrs)
# print(type(bs))
# print(bs.attrs)
# print(bs.a.string)

# find_all()
# 字符串过滤 搜索所有“a”
# t_list = bs.find_all("a")

# 正则表达式搜索 search()
# t_list = bs.find_all(re.compile("a"))

# 方法：传入函数，根据函数要求搜索
# def name_exists(tag):
#     return tag.has_attr("")
#
# t_list = bs.find_all(name_exists)
# print(t_list)

# kwargs
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(text=re.compile("\d"), limit=3)
# t_list = bs.find_all("a",limit=3)

# t_list =bs.select("title")
# t_list =bs.select(".mnav")
# t_list =bs.select("#u1")
# t_list =bs.select("a[class='toindex']")
# t_list =bs.select("head > title")
t_list = bs.select(".mnav ~ .bri")
# for i in t_list:
#     print(i)

print(t_list[0].get_text())