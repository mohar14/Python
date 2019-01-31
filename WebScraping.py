import urllib2
from bs4 import BeautifulSoup
import csv
import pandas as pd

page=urllib2.urlopen('https://www.dell.com/community/Laptops/ct-p/Laptops')
soup=BeautifulSoup(page,'html.parser')

#1

laptops=soup.find_all('div', attrs={'class':'cat-card-title'})
posts=soup.find_all('span',attrs={'class':'cat-card-posts'})

postsData={}

for i in range(4):
    a=laptops[i].get_text().strip()
    postsData[a]=(posts[i].text.strip())

del postsData['Chromebook']
print postsData

#2
title=[]
author=[]
date=[]
time=[]
latestAuthor=[]
latestTime=[]
latestDate=[]
kudos=[]
replies=[]
views=[]
solved=[]


def insScrape(url):
    site = urllib2.urlopen(url)
    soup = BeautifulSoup(site, 'html.parser')


    for i in soup.find_all('div',attrs={'class':'lia-component-messages-column-thread-info'}):
        a=i.text.strip()
        title.append(a)

    for i in soup.find_all('div', attrs={'class': 'lia-info-area'}):
        a=list(filter(None,i.text.strip().replace('\n','*').split('*')))[1]
        author.append(a)

    for i in soup.find_all('div', attrs={'class': 'lia-info-area'}):
        a=list(filter(None,i.text.strip().replace('\n','*').split('*')))[3]
        date.append(a)

    for i in soup.find_all('div', attrs={'class': 'lia-info-area'}):
        a=list(filter(None,i.text.strip().replace('\n','*').split('*')))[4]
        time.append(a)


    length=len(soup.find_all('div', attrs={'class': 'lia-info-area'}))
    newList=[]


    for i in range(0,length):
        a= soup.find_all('div', attrs={'class': 'lia-info-area'})[i]
        div= a.find_all('span',class_='lia-info-area-item')
        lst=len(div)
        newList.append(lst)

    newAuthor = soup.find_all('div', attrs={'class': 'lia-info-area'})

    for i in range(len(newList)):
        if newList[i] == 1:
            latestAuthor.append('no latest post')
        else:
            a = newAuthor[i].text.strip().replace('\n', '*').split('*')[-1]
            latestAuthor.append(a)

    newTime=soup.find_all('div', attrs={'class': 'lia-info-area'})

    for i in range(len(newList)):
        if newList[i] == 1:
            latestTime.append('no new time')
        else:
            a = newTime[i].text.strip().replace('\n', '*').split('*')[-3]
            latestTime.append(a)

    newDate = soup.find_all('div', attrs={'class': 'lia-info-area'})

    for i in range(len(newList)):
        if newList[i] == 1:
            latestDate.append('no new date')
        else:
            a = newDate[i].text.strip().replace('\n', '*').split('*')[-4]
            latestDate.append(a)

    for i in soup.find_all('td', attrs={'class': 'cKudosCountColumn lia-data-cell-secondary lia-data-cell-integer'}):
        a = i.text.strip()
        kudos.append(a)

    for i in soup.find_all('td', attrs={'class': 'cRepliesCountColumn lia-data-cell-secondary lia-data-cell-integer'}):
        a = i.text.strip()
        replies.append(a)

    for i in soup.find_all('td', attrs={'class': 'cViewsCountColumn lia-data-cell-secondary lia-data-cell-integer'}):
        a = i.text.strip()
        views.append(a)

    resolved=soup.find('table',attrs={'class':'lia-list-wide'})
    for i in resolved.find_all('tr',attrs={'class':'lia-list-row'}):
        if resolved.find('td',attrs={'aria-label':'This thread is solved'}):
            solved.append('solved')
        else:
            solved.append('not solved')


insScrape('https://www.dell.com/community/Inspiron/bd-p/Inspiron')
insScrape('https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/2')
insScrape('https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/3')
insScrape('https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/4')
insScrape('https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/5')


print len(title)
print len(author)
print len(date)
print len(time)
print len(latestAuthor)
print len(latestTime)
print len(latestDate)
print len(kudos)
print len(replies)
print len(views)

postDict={'title':title,'author':author,'date':date,'time':time,'latestAuthor':latestAuthor,'latestDate':latestDate,
          'latestTime':latestTime,'kudos':kudos,'replies':replies,'views':views,'solved':solved}
dataframe=pd.DataFrame(data=postDict)
dataframe.to_csv('HW5mdey2.csv',encoding='utf-8',sep=',', index=False)

