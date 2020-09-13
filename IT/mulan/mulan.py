#http://m.maoyan.com/mmdb/comments/movie/1200486.json?_v_=yes&offset=0&startTime=2018-08-18%2022%3A25%3A03
#coding=utf-8
import requests
import json
import time
from datetime import datetime
from datetime import timedelta
import random

#获取随机IP
def get_random_ip():
    alist = []
    with open('UsabelIP.txt', 'r') as f:
        num = len(f.readlines())
        f.seek(0, 0)
        for i in range(0, num):
            line = f.readline().strip()
            alist.append(line)
        # print (' '.join(alist))
    proxy_ip = random.choice(alist)
    print(proxy_ip)
    proxies = {'http': proxy_ip}
    return proxies

#获取页面信息
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
    # with open('UsabelIP.txt', 'r') as f:
    #     #count = len(f.readlines())
    #     #f.seek(0, 0)
    #    # num = random.randrange(1, count, 1)
    #     text = f.readline()
    #     #print(count)
    #     #print("+" * 10)
    #     #print(text)
    #retry_count = 5
    #proxy = get_proxy().get("proxy")
    #while retry_count>0:
    proxy = get_random_ip()
    response = requests.get(url,headers=headers,proxies=proxy)
    time.sleep(3)
    if response.status_code ==200:
        print(response.text)
        return response.text
    return None

#处理数据
def parse_data(html):
    data = json.loads(html)['cmts']
    comments=[]
    for item in data:
        comment = {
            'id':item['id'],
            'nickName':item['nickName'],
            'cityName':item['cityName'] if 'cityName' in item else '',
            'content':item['content'].replace('\n',' ',10), #处理评论内容换行的情况
            'score':item['score'],
            'startTime':item['startTime']
        }
        comments.append(comment)
    return comments


#保存数据
def save2txt():
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end_time = '2020-09-12 22:00:00'
    print(start_time)


    #print({"http": "http://{}".format(proxy)})
    while start_time>end_time :
        url = 'https://m.maoyan.com/mmdb/comments/movie/1210778.json?_v_=yesyes&offset=0&startTime=' + start_time.replace(' ', '%20')
        html = None
        try:

            html = get_data(url)
        except Exception as e:
            time.sleep(0.5)
            html = get_data(url)
        else:
            time.sleep(0.1)

        comments = parse_data(html)
        print(comments)
        start_time = comments[14]['startTime']
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(seconds=-1)
        start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')

    for item in comments:
        with open('comments.txt','a',encoding='utf-8') as f:
            f.write(
                str(item['id']) + ',' + item['nickName'] + ',' + item['cityName'] + ',' + item['content'] + ',' + str(
                    item['score']) + ',' + item['startTime'] + '\n')


if __name__=="__main__":
    # url = 'https://m.maoyan.com/mmdb/comments/movie/1210778.json?_v_=yes&offset=0&startTime=2020-09-11%2022%3A25%3A03'
    # html = get_data(url)
    # comments = parse_data(html)
    # print(comments)
    save2txt()




