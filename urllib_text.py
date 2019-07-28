import urllib.request

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/75.0.3770.142 Safari/537.36'}
r = urllib.request.urlopen('https://www.xiaoniangao.cn')
print(r.read().decode('utf-8'))