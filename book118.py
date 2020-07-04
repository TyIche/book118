import requests
import re
from json import loads
import os
import time
'''
思路：
在network js 抓包
https://openapi.book118.com/getPreview.html?&project_id=1&aid=184927237&view_token=qSDZ_RdydeQdJkn9IL81oH_08pKuDjMK&aid_encode=7132052161001150&page=13&callback=jQuery17105815868419103902_1584273046808&_=1584273046821
然后改page参数获取全部"\/\/view-cache.book118.com\/view1\/M02\/10\/0B\/wKh2BVyV9vGAM8t5AAF6rpyb2Is307.png地址
'''
if not os.path.exists('./img2/'):
    os.makedirs('./img2/')
url1 = r' https://openapi.book118.com/getPreview.html?&project_id=1&aid=184927237&view_token=qSDZ_RdydeQdJkn9IL81oH_08pKuDjMK&aid_encode=7132052161001150&page= '
url2 = r' &callback=jQuery17105815868419103902_1584273046808&_=1584273046821 '
hd={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'}
for i in range(21,25):
    time.sleep(2)
    FristPage=i*6-5
    url=url1+str(FristPage)+url2
    ParsePage=requests.get(url,headers =hd)
    print(ParsePage.text)
    jsonn=re.findall(r'({.*})',ParsePage.text)[0]
    print(jsonn)
    dic=loads(jsonn)
    data=dic.get("data")
    print(i)
    for j in range(0,6):
        x=str(FristPage+j)
        #print(data)
        string=data.get(x)
        #string=string.replace('/','')
        #print(x,string)
        if(string[0]=='h'):
            continue
        r=requests.get("https:"+string,headers=hd)
        with open('./img2/%d.jpg'%(FristPage+j),'wb') as fd:
            fd.write(r.content)

