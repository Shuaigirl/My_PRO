import requests
import os
from lxml import etree
from threading import *
from time import sleep

nMaxThread = 3  #这里设置需要开启几条线程
ThreadLock = BoundedSemaphore(nMaxThread)

gHeads = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

class Meizitu(Thread):
    #构造函数
    def __init__(self,mainReferer,url,title):
        Thread.__init__(self) #调用父类构造函数
        self.MainReferer = mainReferer  
        self.url = url
        self.title = title[3:-4]  #这里是为了把<b></b>给删除  因为网站中的titles是<b>这个是一个标题</b>  同时<b> 正好是3 右边</b> 正好是-4

    #线程开始函数
    def run(self):
        try:
            urlList = self.GetPhotoUrl()
            if len(urlList) > 0 and urlList != None:
                self.SavePath(urlList)
            
        finally:#当线程执行完成之后释放 说明这个线程已经结束了 不管是异常结束还是正常结束 他都是结束了 那么就需要启动下一个新的线程来执行 新的内容了 
            ThreadLock.release()

    #获取图片url列表
    def GetPhotoUrl(self):
        heads={
            "Referer":self.MainReferer
        }
        heads.update(gHeads)
        html = requests.get(self.url,headers=heads)
        if html.status_code == 200:
            xmlContent = etree.HTML(html.text)
            urlList = xmlContent.xpath("//div[@id='picture']/p/img/@src")  #获取所有图片列表
            return urlList
        else:
            return None

    #保存图片 如果文件夹不存在则创建文件夹
    def SavePath(self,urlList):
        heads = {
            "Referer": self.url #这里是referer是因为网站有防盗链 加了这个字段就可以过掉他的防盗链
        }
        heads.update(gHeads)
        savePath = "./photo/%s" % self.title
        if not os.path.exists(savePath):  #判断文件夹是否存在
            os.makedirs(savePath)   #makedirs 是递归创建目录  mkdir是创建目录 区别就是在于递归是可以创建深层目录
        for i in range(len(urlList)):
            j = 0
            while j<5: #这里判断5的原因是 如果错误超过5次 就不会继续再执行了 也就是抛弃了这个图片
                print ("Download : %s/%d.jpg" % (self.title.encode("gbk"), i + 1))  #这里使用encode("gbk")是因为 win7的情况下 控制台是gbk编码的 中文会乱码
                html = requests.get(urlList[i],headers=heads)
                if html.status_code == 200:
                    with open(savePath + "/%d.jpg"%(i+1),"wb") as f:   #open 使用wb时因为 图片是二进制数据 不能按照文本的形式进行保存
                        f.write(html.content)
                    break       #当保存执行完成之后跳出while 进行下一个图片的保存
                elif html.status_code == 404: #这里还可以加入多种错误代码 比如405 401 等等
                    j+=1
                    sleep(0.05)
                    continue
                else:
                    return None


def main():
    while True:
        try:
            nNum = int(input("请输入要下载几页: "))   #这里是python2的用法 python3应该没有raw_inpu了 可以换成input  如果不换也行 可以直接写入num的内容 这里主要就是下载数量的数值
            if nNum>0:
                break
        except ValueError:
            print("请输入数字。")
            continue
    for i in range(nNum):
        url = "http://www.meizitu.com/a/more_%d.html"%(i+1)
        html = requests.get(url, headers=gHeads)
        if html.status_code == 200:
            xmlContent = etree.HTML(html.content)
            hrefList = xmlContent.xpath("//div[@class='pic']/a/@href")
            titleList = xmlContent.xpath("//div[@class='pic']/a/img/@alt")
            for i in range(len(hrefList)):
                ThreadLock.acquire()   #这里使用信号量的原因是 比如当前的设置是3 是为了控制线程数 如果这里没有这个信号量 那么线程会无限启动
                t = Meizitu(url,hrefList[i],titleList[i])
                t.start()  


if __name__ == '__main__':
    main()
