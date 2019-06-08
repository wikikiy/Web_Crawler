import requests
from fake_useragent import UserAgent
from lxml import etree
import time

# Get first page urls
def get_url(url):
    response=requests.get(url,headers={"User-Agent": UserAgent(verify_ssl=False).random}).text
    e=etree.HTML(response)
    links=e.xpath('//td[@align="center"]/a/@href')
    first_url="https://www.24fa.top{}"
    urls=[]
    for link in links:
        path="".join(link).split("..")[-1]
        last_url=first_url.format(path)
        urls.append(last_url)
    return urls

# Get all image url
def parse_url(pages):
    all_url=[]
    for page in pages:
        response = requests.get(page,headers={"User-Agent": UserAgent(verify_ssl=False).random}).text
        e = etree.HTML(response)
        nums = e.xpath('//div[@class="pager"]/ul/li/a/text()')
        num=int(nums[-2])
        new_page = "".join(page).split(".html")[0]
        for i in range(2,num+1):
            # Split joint all image url
            last_page=new_page+"p"+str(i)+".html"
            all_url.append(last_page)
    return all_url

# Down all image
def down_img(imgsurl):
    for imgurl in imgsurl:
        response = requests.get(imgurl,headers={"User-Agent": UserAgent(verify_ssl=False).random}).text
        e = etree.HTML(response)
        imglinks = e.xpath('//div[@id="content"]/div/p/img/@src')
        for imglink in imglinks:
            link="".join(imglink).split("../..")[-1]
            # Get image name
            path="".join(imglink).split("/")[-1]
            links="https://www.24fa.top"+link
            resp=requests.get(links,headers={"User-Agent": UserAgent(verify_ssl=False).random})
            # Enter your store folder
            with open("***"+path,"wb+") as f:
                time.sleep(3)
                f.write(resp.content)

if __name__=='__main__':
    url="https://www.24fa.top/MeiNv/"
    pages=get_url(url)
    imgurl=parse_url(pages)
    down_img(imgurl)
