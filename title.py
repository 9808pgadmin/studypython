import requests
from bs4 import BeautifulSoup

# 为了获取网页数据我们要使用requests的get()方法：
url = "https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States"
page = requests.get(url)
# print(page.status_code)

# 上面的代码会显示http相应的全部内容，包括html代码和我们需要的文本数据信息。通过使用beautifulsoup的prettify()方法可以将其更美观的展示出来：
soup = BeautifulSoup(page.content,'html.parser')

# 使用bs4对象的find方法提取table标签中的数据，此方法返回bs4对象：
tb = soup.find('table',class_='wikitable')

# 使用find_all方法来迭代获取所有b标签下的a标签：
for link in tb.find_all('b'):
    # time = link.find('small')
    name = link.find('a')

    # 添加get_text()方法，即可提取出所有a标签下title元素的文本信息
    print(name.get_text())
