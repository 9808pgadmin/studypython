import requests
from bs4 import BeautifulSoup
import os

# 为了获取网页数据我们要使用requests的get()方法：
# 输出200相应成功，说明连接成功
#爬取多页图片


for i in range(1, 11):
    url = "https://www.ivsky.com/bizhi/fuchouzhelianmeng_t13547/index_{}.html"
    url = url.format(i)
    page = requests.get(url)
    # print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    all_img = soup.find('ul', class_='il').find_all('img')
    for img in all_img:
        src = 'http:' +img['src']
        img_url = src
        print(img_url)
        root = 'E:/pic/'
        path = root + img_url.split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                    r = requests.get(img_url)
                    with open(path, 'wb') as f:
                        f.write(r.content)
                        f.close()
                        print("文件保存成功")
            else:
                print("文件已存在")
        except:
            print("爬取失败")