import json
import requests
from sendMessage import sendmessage
from SearchWeb import serchimg, serchurl

# define userid
userid = ['oet2l6C-GgjRquvA1vQapoL9i4gc', 'oet2l6I_x_SE855_JUlcKFa0FBAs', 'oet2l6Bc7Eb6iQC_IZtJnf8B5Hfw',
          'oet2l6Erv9Dx8IOHS4p1onuVnR54', 'oet2l6K7rz55wfxEWUiaRqjngHs4', 'oet2l6GyNH0GBxSfLmbtGQIpkWsU',
          'oet2l6MRKfBNjp_GGzx7p5E_pARo', 'oet2l6OUp0EqzBbwq9Uz6xXNIBIQ', ''
          ]
username = ['狗罐头', '子超', '小可爱', '嘉老板', '尿布', 'josh', '楠哥', '小猫咪', '']

url = 'https://forum.netmarble.com/api/game/stonemmogb/official/forum/stone_kr/article/list?rows=15&start=0&menuSeq=24&_=1700000000000'

if __name__ == '__main__':
    newurl, aid, menuseq = serchurl(url, 'kr')
    if newurl:
        imgurl = serchimg(aid, menuseq)
        for i in range(8):
            try:
                sendmessage(userid[i], "更新资讯已发布，{}大佬请看:\n".format(username[i]) + imgurl)
            except:
                print('用户'+username[i]+'超出互动时间，无法发送。')
                pass
            continue



