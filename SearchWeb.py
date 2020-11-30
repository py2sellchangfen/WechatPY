import json
import requests

propath = '/home/h/usr/project/WechatPY'
# url = 'https://forum.netmarble.com/api/game/stonemmogb/official/forum/stone_cn/article/list?rows=15&start=0&menuSeq=3&_=1606025508703'
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }

def serchurl(url, na):
    response = requests.get(url=url, headers=headers)
    jres = json.loads(response.text)
    count = jres['totalCount']
    artcile = jres['articleList'][0]
    aid = artcile['id']
    menuseq = artcile['menuSeq']
    # 中文url
    newurl = 'https://forum.netmarble.com/stone_{}/view/{}/{}'.format(na, menuseq, aid)
    # newurl = 'https://forum.netmarble.com/stone_{}/view/{}/{}'.format(na, menuseq, aid)
    with open(propath+'/log/stone{}.txt'.format(na), "r+") as fp:
        precount = int(fp.read())
        if count != precount:
            fp.seek(0)
            fp.write(str(count))
            return newurl, aid, menuseq
        else:
            return 0, 0, 0

def serchimg(aid, menuseq):
    # newrurl = 'https://forum.netmarble.com/api/game/stonemmogb/official/forum/stone_cn/article/{}?menuSeq={}&viewFlag=true&_=1700000000000'.format(aid, menuseq)
    newrurl = 'https://forum.netmarble.com/api/game/stonemmogb/official/forum/stone_kr/article/{}?menuSeq={}&viewFlag=true&_=1700000000000'.format(aid, menuseq)
    response = requests.get(newrurl, headers)
    jres = json.loads(response.text)
    artcile = jres['article']
    imgurl = artcile['attachFileInfo'][0]['url']
    return imgurl

# response = requests.get(url=url, headers=headers)
# jres = json.loads(response.text)
# count = jres['totalCount']
# artcile = []
# artcile = jres['articleList'][0]
#
# id = artcile['id']
# menuseq = artcile['menuSeq']
# newurl = 'https://forum.netmarble.com/stone_cn/view/{}/{}'.format(menuseq, id)
# print(newurl)



# response.encoding = 'utf-8'
# page_text = response.text
# soup = BeautifulSoup(page_text, 'lxml')
# print(soup.p.contents)

# udtime = soup.find(attrs={"property": "og:novel:update_time"})['content']
# with open(propath+'/log/xiaoshuo.txt', "a+", encoding='utf-8') as f:
#     f.write(udtime+'\n')



