import requests
from bs4 import BeautifulSoup
#xpath法取头标签：//div[@class="sub_box-yNw9RL3I"]/ul/li/a/@href
url="http://gd.ifeng.com/listpage/80160/1/list.shtml"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
request = requests.get(url,headers=headers)
request.encoding='utf-8'
soup = BeautifulSoup(request.text,'lxml')
# links = soup.select('div .box_list > h2 > a')
data_text = soup.select('div .box650 > div')[6].attrs['data-title']
# print(links[1].text)
#print(data_text)
datas = soup.select('div .box650 > div')
#print(datas[0].attrs['data-title'])
i=0
for data in datas[1:-1]:
    title = data.attrs['data-title']
    #print(data.attrs['data-title'])
    link = data.attrs['data-url']
    detail = data.attrs['data-text']
    print("标题：",title,'\n','内容：',detail,'\n',"链接:",link)
    print('\n')
    # title=data[0].attrs['data-title']
    # text = data[0].attrs['data-text']
    # data_url = data[0].attrs['data-url']
    # print(title,'\n',text,'\n',data_url)
    # i=i+1