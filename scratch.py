from fake_useragent import UserAgent
import requests
from lxml import etree
import time

def get_url(url):
    all_url=[]
    for i in range(1,6):
        urls=url.format(i)
        resp=requests.get(urls,headers={"User-Agent":UserAgent(verify_ssl=False).random},verify=False)
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

# def first_page(oneurls):
#     try:
#         for url in oneurls:
#             frt_url="https://www.24fa.top/"+"".join(url)
#             resp = requests.get(frt_url, headers={"User-Agent": UserAgent(verify_ssl=False).random},verify=False)
#             resp.encoding = 'utf-8'
#             e = etree.HTML(resp.text)
#             imgs = e.xpath('//div[@id="content"]/div/div/img/@src')
#             for img in imgs:
#                 img_url="".join(img).split('../..')[-1]
#                 url="https://www.24fa.top{}".format(img_url)
#                 resp=requests.get(url,headers={"User-Agent": UserAgent(verify_ssl=False).random},verify=False)
#                 path="".join(url).split('/')[-1]
#                 with open("D:\\meitu\\"+ path,'wb+') as f:
#                     print("正在下载")
#                     f.write(resp.content)
#     except:
#         print("退出循环")

def other_page(securls):
    for url in securls:
        link="".join(url).split('.html')[0]
        i=2
        links="https://www.24fa.top/{}p{}.html".format(link,i)
        all_url=[]
        print(all_url)
        while requests.get(links, headers={"User-Agent": UserAgent(verify_ssl=False).random},verify=False)==200:
            i=+1
            all_url.append(all_url)
            if requests.get(links, headers={"User-Agent": UserAgent(verify_ssl=False).random},verify=False)==400:
                break
        for url in all_url:
            resp=requests.get(url,headers={"User-Agent": UserAgent(verify_ssl=False).random},verify=False)
            resp.encoding='utf-8'
            e=etree.HTML(resp.text)
            imgs = e.xpath('//div[@id="content"]/div/div/img/@src')
            for img in imgs:
                url = "https://www.24fa.top/{}".format(img)
                resp = requests.get(url, headers={"User-Agent": UserAgent(verify_ssl=False).random},verify=False)
                path = "".join(url).split('/')[-1]
                with open("D:\\meitu\\" + path, 'wb+') as f:
                    print("正在下载")
                    f.write(resp.content)

if __name__=='__main__':
    url="https://www.24fa.top/search.aspx?page={}&keyword=PartyCat%E8%BD%B0%E8%B6%B4%E7%8C%AB&where=title&sum=109"
    pages=get_url(url)
    # oneurls=parse_url(pages)
    securls=parse_url(pages)
    # first_page(oneurls)
    other_page(securls)
