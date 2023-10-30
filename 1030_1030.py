import requests
from lxml import etree
headers={
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
      }
j=1#用于计算电影数
fl=open("电影排行.doc","w",encoding='utf-8')
for i in range(0,250,25):#i表示页数，1页25影片
      url='https://movie.douban.com/top250?start='+str(i)+'&filter='
      response=requests.get(url,headers=headers)
      text=response.text
      html=etree.HTML(text.encode('utf-8'))
      ul=html.xpath('//div[@class="info"]')
      for div in ul:
            t="".join(div.xpath('./div[@class="hd"]/a/span[@class="title"]/text()'))
            s="".join(div.xpath('./div[@class="hd"]/a/span[@class="other"]/text()'))
            title=t+s
            d="".join(div.xpath('./div[@class="bd"]/p/text()'))
            director=d.replace("              ","").replace("\n","").replace("主演","\n主演")
            quote="".join(div.xpath('./div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()'))
            content=str(j)+"."+title+"\n"+director+"\n主题："+quote+"\n"
            fl.write(content)
            j=j+1
fl.close()
