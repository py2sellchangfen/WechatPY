import requests
from bs4 import BeautifulSoup
from sendMessage import sendmessage

user = 'oet2l6OAuvGUIoaBLFGsiA4uqLfI'  # 我的id
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }  # 假装通过计算机使用浏览器访问
url = 'https://m.78zw.com/55_55595/'  # 网页地址
propath = '/home/h/usr/project/WechatPY'  # 存放章节地址
if __name__ == '__main__':
    res = requests.get(url, headers)  # 获取响应
    res.encoding = 'utf-8'
    page_text = res.text
    # print(page_text)
    soup = BeautifulSoup(page_text, 'lxml')
    # print(soup)
    chapter = soup.find(attrs={"property": "og:novel:latest_chapter_name"})['content']
    # print(chapter)
    chapter = int(chapter[1:5:1])
    # print(chapter)
    with open(propath+"/log/xiaoshuo.txt", "r+") as fp:
        prechapter = int(fp.read())
        # print(prechapter)
        lasturl = ''
        if chapter > prechapter:
            t = soup.find_all('li')
            # print(t)
            for i in range(len(t)):
                if str(prechapter + 1) in t[i].text:
                    lasturl = 'http://m.78zw.com{}'.format(t[i].a['href'])
                    break
            fp.seek(0)
            fp.write(str(chapter))
            sendmessage(user, "小说已经更新，正在发送最新章节链接\n"+lasturl)
