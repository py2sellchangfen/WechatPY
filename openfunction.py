propath = '/home/h/usr/project/WechatPY'

for i in range(5):
    print(i)
with open(propath+"/log/test.txt", "r+",) as fp:
    print(fp.readlines())