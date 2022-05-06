# _*_coding:utf-8_*_
# @Time:2022/4/8 17:38
# @Author:Young
# @File:爬虫_urllib_下载

import urllib.request


# 网页下载
# url = 'https://www.baidu.com/'
# urllib.request.urlretrieve(url, 'demo/bilibili.html')

# 图片下载
url = 'https://alifei04.cfp.cn/creative/vcg/veer/1600water/veer-133698433.jpg'
urllib.request.urlretrieve(url=url, filename='demo/fly.jpg')

# 视频下载
# url_video = 'https://v2.kwaicdn.com/upic/2022/03/23/20/BMjAyMjAzMjMyMDQ0MjVfOTg0NzkwMl83MDMwNTA3NTAwOF8xXzM=_b_B8868bdc2f7be813b4004a692a6ce5ffd.mp4?pkey=AAUMBCh4yB9d52j0PeCjE9PoLvpsJCtYXSFbhRiyy3gbOEvu6VwOlhuqxTU3gtCcIwNCz6vYeERQHE4Sq6TCwqmPLwQgsyPZ725n1Wlu699HipjhrkWC40_wCHfa1uzRPac&tag=1-1649412481-xpcwebdetail-0-joszbhre57-41d147b444272bc7&clientCacheKey=3xieq4zbv6f5zre_b.mp4&tt=b&di=7177480d&bp=14944'
# urllib.request.urlretrieve(url=url_video, filename='demo/yyds.mp4')