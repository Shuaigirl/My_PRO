# _*_coding:utf-8_*_
# @Time:2022/4/9 17:38
# @Author:Young
# @File:URLError和HTTPError异常i

import urllib.request
import urllib.error
# https://blog.csdn.net/qq_53348314/article/details/123021856(正确的url)
#url = 'https://blog.csdn.net/qq_53348314/article/details/1230218563666'
url = 'https://blog.csdn23232.net'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

except urllib.error.HTTPError:
            print('系统正在升级...')
except urllib.error.URLError:
    print('请求的URL有无，或许系统正在升级...')



