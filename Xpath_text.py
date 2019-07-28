import requests
from lxml import etree

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/75.0.3770.142 Safari/537.36'}
r = requests.get('https://www.xiaoniangao.cn', headers=header)
html = etree.HTML(r.text)
result = html.xpath('/html/head/link[1]/@href')
for src in result:
    with open(r'D:\scrapy_text\Spyder_text\img\title.ico', 'wb+') as f:
        print(src)
        img = requests.get(src)
        print(img.content)
        f.write(img.content)
print(html.text)
