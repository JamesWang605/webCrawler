# coding = utf-8

import sys
from bs4 import BeautifulSoup
import urllib.request, urllib.error
import re
import xlwt
import sqlite3


save_path = ".\\doubanTop250.xls"
base_url = "https://movie.douban.com/top250?start=74&filter="

def main():
    #爬取网页
    get_page(target_url)
    #解析数据
    save_data(save_path)
    #保存数据


def get_page(url):
    data = []
    for i in range(0,10):
        target_url = url+str(i*25)
        data.append(ask_url(target_url))
    return data


#Get Content
def ask_url(url):
    header = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
        "/92.0.4515.131 Safari/537.36"}
    request = urllib.request.Request(url=url, headers=header)
    html = ""
    try:
        response = urllib.request.urlopen(request,timeout=2)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error as e:
        print("err: "+e.reason)
    return html


def save_data(path):
    print("placeholder")


if __name__ == "__main__":
    print()