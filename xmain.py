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
    page_text = res.text
    soup = BeautifulSoup(page_text, 'lxml')
    chapter = soup.find(attrs={"property": "og:novel:latest_chapter_name"})['content']
    chapter = int(chapter[1:5:1])
    # time = soup.find(attrs={"property": "og:novel:update_time"})['content']
    # lasturl = soup.find(attrs={"property": "og:novel:latest_chapter_url"})['content']
    with open(propath+"/log/xiaoshuo.txt", "r+") as fp:
        prechapter = int(fp.read())
        lasturl = ''
        if chapter > prechapter:
            t = soup.find_all('li')
            for i in range(len(t)):
                if str(prechapter + 1) in t[i].text:
                    lasturl = 'http://m.78zw.com{}'.format(t[i].a['href'])
                    break
            fp.seek(0)
            fp.write(str(chapter))
            sendmessage(user99, "小说已经更新，正在发送最新章节链接\n"+lasturl)


