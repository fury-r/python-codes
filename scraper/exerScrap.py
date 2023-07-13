# site_url/robots.txt shows what  you can scrap

import io
import os
from bs4 import BeautifulSoup

import requests
import pprint
import sys
import PyPDF2


def get_news(var):
    links = []
    scores = []
    for i in range(1, var):

        res = requests.get(f'https://news.ycombinator.com/news?p={str(i)}')
        if(res.status_code == 200):
            soup = BeautifulSoup(res.text, 'html.parser')
            # print(soup.head)  var.head gets head .body gets body
            # print(soup.find_all('a' ))
            # print(soup.find(id='28232645'))

            link = soup.select('.storylink')
            subtext = soup.select('.subtext')
            links.append(link)
            scores.append(subtext)
    return custom_news(links, scores)


def sort_news(list):

    return sorted(list, key=lambda k: k['score'], reverse=True)


def custom_news(links, subtext):
    custom = []
    for i, item in enumerate(links):
        link = links[i]
        score = subtext[i]
        for j, item in enumerate(link):

            l = link[j].getText()
            vote = score[j].select('.score')
            if len(vote):
                points = int((vote[0].getText()).replace(' points', ''))

                if(points >= 100):
                    href = link[j].get('href', None)
                    custom.append({"title": l, "link": href, 'score': points})
    write = PyPDF2.PdfFileWriter()
    merger=PyPDF2.PdfFileMerger()
    c, a = 0,0

    for d in custom:
        page = open("./text.txt", "a")


            
        text=f"Title:{d['title']}\nlinks:{d['link']}\nVotes:{d['score']}\n"
        page.write(text)
        page.write('\n')
 
    return sort_news(custom)

try:
    q=sys.argv[1]
    pprint.pprint(get_news(int(q)+1))
except IndexError:
    print("No input Swicthing  Default  to Scraping 1 page")
    pprint.pprint(get_news(2))


