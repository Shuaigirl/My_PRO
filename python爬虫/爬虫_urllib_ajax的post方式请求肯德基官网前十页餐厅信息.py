# _*_coding:utf-8_*_
# @Time:2022/4/9 16:35
# @Author:Young
# @File:爬虫_urllib_ajax的post方式请求肯德基官网前十页餐厅信息


import urllib.request
import urllib.parse
# 用方法来获取路径并请求对象的定制
def creat_request(page):

    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
                'cname': '北京',
                'pid': '',
                'pageIndex': page,
                'pageSize': 10
         }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
         }
    request = urllib.request.Request(url=base_url, data=data, headers=headers)
    return request
# 用方法模拟浏览器向服务器发送请求
def creat_content(request):
     response=urllib.request.urlopen(request)
     content = response.read().decode('utf-8')
     return content
#湖区数据并写入到json文件
def creat_dowm(page,content):
    with open('demo/kendeji_'+str(page)+'.json', 'w', encoding='utf-8') as fp:
      fp.write(content)




#创建程序的入口
if __name__=='__main__':
    start_page = int(input('请输入起始页：'))
    end_page = int(input('请输入结束页：'))
    for page in range(start_page,end_page):
        #print(page)
        request = creat_request(page)
        content = creat_content(request)
        creat_dowm(page, content)


