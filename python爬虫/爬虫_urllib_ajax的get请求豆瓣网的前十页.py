# _*_coding:utf-8_*_
# @Time:2022/4/9 15:10
# @Author:Young
# @File:爬虫_urllib_ajax的get请求豆瓣网的前十页

import urllib.request
import urllib.parse

def creat_request(page):
  base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
  data = {
      #切记这里的page是int类型，如果是字符串类型就会提示HTTPError
    'start': (page-1)*20,
    'limit': '20'
   }
  new_data = urllib.parse.urlencode(data)
  url = base_url+new_data
  print(url)
  headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36X'
  }

  request = urllib.request.Request(url=url, headers=headers)
  return  request

 # print(url)

def creat_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def creat_down(page,content):
    with open('demo/video_'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# ---------------------程序的入口----------------------
if __name__=='__main__' :
      start_page = int(input('请输入起始的页码：'))
      end_page = int(input('请输入起始的页码：'))
      for page in range(start_page, end_page+1):
        request = creat_request(page)
        # print(page)
        content = creat_content(request)
        creat_down(page, content)

