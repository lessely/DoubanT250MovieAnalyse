import requests
import re
import csv
from lxml import html
global url
a=1
def douban():
    global a
    # 使用U-A伪装成浏览器发送请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    # 先使用requests发送网络请求从而获取网页
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.text)
    for i in range(1,26):
        movie_info=[]
        name=tree.xpath("//*[@id='content']/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1]".format(i))
        info = tree.xpath("//*[@id='content']/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[1]/text()[2]".format(i))
        data=[x.strip() for x in info]
        movie=re.sub('/',',',data[0])

        name=name[0].text
        date=movie[0:4]#日期
        country=movie[7:movie.index(",",7)].replace(" ","/").rstrip()
        type=movie[movie.index(",",7)+2:].replace(" ","/").lstrip()

        movie_info.append(a)
        movie_info.append(name)
        movie_info.append(date)
        movie_info.append(country)
        movie_info.append(type)

        csv_writer.writerow(movie_info)

        #print(name+","+date+","+country+","+type)
        print("已爬取第{}条记录".format(a))
        a+=1




if __name__ == '__main__':
    f = open('豆瓣T250.csv', 'w',newline='' ,encoding='utf_8_sig')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["movie_top","movie_name", "movie_date", "movie_country","movie_type"])
    for i in range(10):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        douban()

    f.close()