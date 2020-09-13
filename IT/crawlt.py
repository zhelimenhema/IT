from lxml import etree
import requests
import re
import pymysql
def crawl():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}

    url = "http://gd.ifeng.com/listpage/80160/1/list.shtml"
    resp = requests.get(url,headers=header).content
    content = etree.HTML(resp)
    #print(content)
    titles = content.xpath('//div/h2/a/@title')
    links = content.xpath('//div/h2/a/@href')
    time_list = obj2str(content.xpath('//div/span'))
    data2base(titles,links,time_list)


# for i in range(len(titles)):
#     print(titles[i])
#     print(links[i])
#     print(time_list[i])
#
# date=[]


def obj2str(data):
    source=[]
    for i in range(len(data)):
        data[i] = data[i].text
        source.append(data[i].split('&nbsp;&nbsp;'))
    return source

def data2base(titles,links,date):
    for i in range(len(date)):
        db = pymysql.connect(host='localhost',port=3306,user='root',
                             password='123456',database='baidu',charset='utf8')
        cur = db.cursor()
        sql = 'INSERT INTO test(title,link,date) VALUES(%s,%s,%s)'
        cur.execute(sql,(titles[i],links[i],date[i]))
        db.commit()
        cur.close()
        db.close()



# for i in range(len(time_list)):
#     #print(type(time_list[i].text))
#     time_list[i] = re.sub(r'&brvbar;', '', time_list[i].text)
#     #time_list[i] = re.sub(r'&brvbar;', '', time_list[i])
#     #date.append(time_list[i].split('&brvbar;')[0])
#     #date[i] = date[i].strip()
#     date.append(time_list[i])
#     print(date[i])
if __name__=="__main__":
    crawl()