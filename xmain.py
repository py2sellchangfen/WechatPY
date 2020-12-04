from sendMessage import sendmessage
import requests
from bs4 import BeautifulSoup

# define userid
user99 = 'oet2l6C-GgjRquvA1vQapoL9i4gc'  # 我id
user98 = 'oet2l6OAuvGUIoaBLFGsiA4uqLfI'
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
url = 'https://m.78zw.com/55_55595/'
propath = '/home/h/usr/project/WechatPY'
if __name__ == '__main__':
    res = requests.get(url, headers)
    res.encoding = 'utf-8'
    page_text = res.text.replace('<span>','').replace('</span>','')
    soup = BeautifulSoup(page_text, 'lxml')
    chapter = soup.find(attrs={"property": "og:novel:latest_chapter_name"})['content']
    chapter = int(chapter[0].replace('第','').replace('章',''))
    with open(propath+"/log/xiaoshuo.txt", "r+") as fp:
        prechapter = int(fp.read())
        if chapter > prechapter:
            url = soup.find_all('a',text='第{}章'.format(prechapter+1))[0]['href']
            lasturl = 'http://m.78zw.com{}'.format(url)
            fp.seek(0)
            fp.write(str(chapter))
            sendmessage(user99, "小说已经更新，正在发送最新章节链接\n"+lasturl)
        else:
            lasturl = None