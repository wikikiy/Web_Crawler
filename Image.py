import requests
from fake_useragent import UserAgent
from lxml import etree

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

def parse_url(pages):
    all_url=[]
    for page in pages:
        response = requests.get(page,headers={"User-Agent": UserAgent(verify_ssl=False).random}).text
        e = etree.HTML(response)
        nums = e.xpath('//div[@class="pager"]/ul/li/a/text()')
        num=int(nums[-2])
        new_page = "".join(page).split(".html")[0]
        for i in range(2,num+1):
            last_page=new_page+"p"+str(i)+".html"
            all_url.append(last_page)
    return all_url

def down_img(imgsurl):
    num = 0
    for imgurl in imgsurl:
        response = requests.get(imgurl,headers={"User-Agent": UserAgent(verify_ssl=False).random}).text
        e = etree.HTML(response)
        imglinks = e.xpath('//div[@id="content"]/div/p/img/@src')
        if imglinks!=0:
            for imglink in imglinks:
                link="".join(imglink).split("../..")[-1]
                path="".join(imglink).split("/")[-1]
                links="https://www.24fa.top"+link
                resp=requests.get(links,headers={"User-Agent": UserAgent(verify_ssl=False).random})
                if resp.status_code==200:
                    with open("D:\\meitu\\"+path,"wb+") as f:
                        print("正在下载第%s张"%num)
                        f.write(resp.content)
                        num+=1
                else:
                    print("图片加载失败")
        else:
            print("遇到广告页")

if __name__=='__main__':
    url="https://www.24fa.top/MeiNv/"
    pages=get_url(url)
    imgurl=parse_url(pages)
    down_img(imgurl)
