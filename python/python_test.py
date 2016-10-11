import re
from urllib import request 
from urllib import parse
from bs4 import BeautifulSoup as bs
#from urllib.request import urlopen

import sys


""""
## 1
url = "http://www.demo8.com/service/"
html_doc = ""
for line in request.urlopen(url):
    #type(line)
    #print(line.decode("utf-8"))
    html_doc += line.decode("utf-8")

soup = bs(html_doc,"html.parser")
#print(soup.prettify())  #格式化输出html代码
print(soup.title.string) #.get_text()
#print(soup.find(id=""))
#main_content = soup.find("div",{"class":"main"}) #.get_text()
#print(main_content)
all_tit = soup.find_all("p",{"class":"specail_tit"})
## <p class="specail_tit"> <a href="http://xxx">推广</a></p>
for ptit in all_tit:
	print(ptit.get_text(),ptit.find("a")["href"])

## 2

resp = request.urlopen(url)
#help(resp)
#dir(resp)
hd = resp.getheaders()
docline = resp.read().decode("utf-8")
print(hd)
print(docline)
"""

## 3 request
"""
getUrl = "http://cn.bing.com/search?q=python"
postUrl = "http://cn.bing.com/search"

req2 = request.Request(getUrl)
req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36")
req2.add_header("Host","cn.bing.com")
resp2 = request.urlopen(req2)

print("resp2: \n",resp2.read().decode("utf-8"))
"""
#post请求
#postData = parse.urlencode([])
#

'''类的内置类属性，可以直接在外部调用：myClass.__name__
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''
class digPage:
	plist = [1,2,3,4,5,6] #类成员变量相当于静态变量，各对象实例共享
	__empCount=0  #私有写法，不能在类地外部被使用或直接访问，内部访问需加self.

	def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      digPage.empCount += 1

	def test(self,list):
		print(self.plist )
		print(list )
		
num = input("Enter a number  :")
print(type(num))
#num = 1234
d = digPage()
d.test(num)
