import requests
from lxml import etree
name="复变函数"
counter=0
content=''
for page in range(0,20):
    url='https://github.com/search?p='+str(page+1)+'&q=ustc+course&type=Repositories'
    text=requests.get(url).text
    html=etree.HTML(text)
    repo=html.xpath('//a[@class="v-align-middle"]/@href')
    print(len(repo))
    for href in repo:
        text=requests.get('https://github.com/'+href).text
        print('https://github.com/'+href)
        if name in text:
            content+=name+'\n'
        print('counter:',counter+1)
        counter+=1
print(content)
