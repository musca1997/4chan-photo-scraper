import requests
import os
from bs4 import BeautifulSoup

url = 'http://boards.4chan.org/mlp'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'DNT': '1',
                'Connection': 'keep-alive'} 

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content,"lxml")
ponies = soup.findAll('a', attrs={"class":"fileThumb"})
length = len(ponies)
for i in range(length):
    pony = ponies[i].attrs['href']
    with open('pony.txt','a') as f:
        f.write('http:' + pony + '\n')
    
os.system('wget -i pony.txt')
