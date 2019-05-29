from fake_useragent import UserAgent
import requests
from lxml import etree
import time

def get_url(url):
    all_url=[]
    for i in range(1,6):
        urls=url.format(i)
        resp=requests.get(urls,headers={"User-Agent":UserAgent(verify_ssl=False).random})
        resp.encoding='utf-8'
        e=etree.HTML(resp.text)
        titles=e.xpath('//div[@class="title"]/a/@href')
        for title in titles:
            all_url.append(title)
    return all_url

def parse_url(pages):
    all_page=[]
    for page in pages:
        all_page.append(page)
    return all_page

def first_page(urls):
    for url in urls:
        resp = requests.get(url, headers={"User-Agent": UserAgent(verify_ssl=False).random})
        resp.encoding = 'utf-8'
        e = etree.HTML(resp.text)
        imgs = e.xpath('//div[@id="content"]/div/div/img/@src')
        for img in imgs:
            img_url="".join(img).split('../...')[-1]
            url="https://www.24fa.top{}".format(img)
            resp=requests.get(url,headers={"User-Agent": UserAgent(verify_ssl=False).random})
            time.sleep(6)
            path="".join(url).split('/')[-1]
            with open("D:\\美图\\"+ path,'wb+') as f:
                f.write(resp.content)

def other_page(urls):
        link="".join(url).split('.')[-1]
        i=2
        links="https://www.24fa.top/{}p{}.html".format(link,i)
        urls=[]
        while requests.get(links, headers={"User-Agent": UserAgent(verify_ssl=False).random})==200:
            urls.append(links)
        for url in urls:
            resp=requests.get(url,headers={"User-Agent": UserAgent(verify_ssl=False).random})
            resp.encoding='utf-8'
            e=etree.HTML(resp.text)
            imgs = e.xpath('//div[@id="content"]/div/div/img/@src')
            for img in imgs:
                url = "https://www.24fa.top/{}".format(img)
                resp = requests.get(url, headers={"User-Agent": UserAgent(verify_ssl=False).random})
                time.sleep(6)
                path = "".join(url).split('/')[-1]
                with open("D:\\美图\\" + path, 'wb+') as f:
                    f.write(resp.content)

if __name__=='__main__':
    url="https://www.24fa.top/search.aspx?page={}&keyword=PartyCat%E8%BD%B0%E8%B6%B4%E7%8C%AB&where=title&sum=109"
    pages=get_url(url)
    urls=parse_url(pages)
    down_img(urls)