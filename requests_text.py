import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/75.0.3770.142 Safari/537.36'}
r = requests.get('https://www.xiaoniangao.cn', headers=header)
print(r.text)
print(r.status_code)
print(r.json)
