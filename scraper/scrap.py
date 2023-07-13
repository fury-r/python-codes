#site_url/robots.txt shows what  you can scrap

import requests
from bs4 import BeautifulSoup
import pprint

res=requests.get('https://news.ycombinator.com/news')
soup=BeautifulSoup(res.text,'html.parser')
#print(soup.head)  var.head gets head .body gets body
#print(soup.find_all('a' ))
#print(soup.find(id='28232645'))
link=soup.select('.storylink')
subtext=soup.select('.subtext')
def sort_news(list):
    return sorted(list,key=lambda k:k['score'],reverse=True)
    
def custom_news(link,subtext):
    custom=[]
    for i,item in enumerate(link):
        l=link[i].getText()
        vote=subtext[i].select('.score')
        if len(vote):
            points=int((vote[0].getText()).replace(' points',''))
            if(points>=100):
                href=link[i].get('href',None)
                custom.append({"title":l,"link":href,'score':points})
    return sort_news(custom)
        
pprint.pprint(custom_news(link,subtext))