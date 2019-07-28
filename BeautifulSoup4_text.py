import bs4
import requests
import lxml

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/75.0.3770.142 Safari/537.36'}
r = requests.get('https://www.xiaoniangao.cn', headers=header)
html = bs4.BeautifulSoup(r.text, 'lxml')
html.prettify()
print(html.find_all(name='link'))
