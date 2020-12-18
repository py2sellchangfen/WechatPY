from sendMessage import sendmessage
import requests
from bs4 import BeautifulSoup

# define userid
user99 = 'oet2l6C-GgjRquvA1vQapoL9i4gc'  # 我id'
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.61 Safari/537.36"
    }
url = 'https://m.78zw.com/55_55595/'
propath = '/home/h/usr/project/WechatPY'
if __name__ == '__main__':
    res = requests.get(url, headers)
    res.encoding = 'utf-8'
    page_text = res.text.replace('<span>','').replace('</span>','')  # 将所有span关键字去掉，可以通过搜索text来确定链接
    soup = BeautifulSoup(page_text, 'lxml')
    chapter = soup.find(attrs={"property": "og:novel:latest_chapter_name"})['content']
    chapter = int(chapter[1:5])
    with open(propath+"/log/xiaoshuo.txt", "r+") as fp:
        prechapter = int(fp.read())
        if chapter > prechapter:
            fp.seek(0)
            fp.write(str(chapter))
            try:
                url = soup.find_all('a',text='第{}章'.format(prechapter+1))[0]['href']
                showchapter = prechapter + 1
            except:
                # url = soup.find_all('a', text='第{}章'.format(chapter))[0]['href']
                # showchapter = chapter
                url = soup.find_all('a', text='第{}章 ：'.format(prechapter + 1))[0]['href']
                showchapter = prechapter + 1
            lasturl = 'http://m.78zw.com{}'.format(url)
            sendmessage(user99, "小说已经更新，之前浏览到第{}章，正在发送第{}章链接:\n".format(prechapter, showchapter)+lasturl)
        else:
            lasturl = None