# _*_coding:utf-8_*_
# @Time:2022/4/9 11:20
# @Author:Young
# @File:爬虫_urllib_post请求百度翻译之详细页面

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
headers = {
            #'Accept': '*/*',
             #' Accept-Encoding': 'gzip, deflate, br',
            #' Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Connection': 'keep-alive',
            # 'Content-Length': 158,
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'BIDUPSID=58B49850A582896B26E4D784028CA994; PSTM=1647914457; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; BAIDUID=A8DF1F8B76A5F8AC637570B70F7A0E5F:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1649325189,1649381156,1649412820,1649470676; delPer=0; PSINO=6; BAIDUID_BFESS=A8DF1F8B76A5F8AC637570B70F7A0E5F:FG=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1649473431; ab_sr=1.0.1_NzZiYzE2NDNlMDZkMzA2MjgyNmUyMDFlMGM1ZmUwYTBmZjFiNmE1ZDhkZjY0NTliMGYyNDY5OTliYTExZWFmZjQ4ZWVkYTUwYmNlNThiYTg5MzUzNjZiNmIwYWU1NmNjOThiNDg3NDVkMjY3NTQ3MGIzYmFiMDA4YTA5Nzc3MWMyZWJhYmEyYzAxZDZhMmRjNDFjNjMwOTYwNzE1NmIzYQ==; BDRCVFR[Fc9oatPmwxn]=srT4swvGNE6uzdhUL68mv3; H_PS_PSSID=35837_36175_36057_36020_36004_36088_36165_34584_36141_36120_36074_36264_36125_36235_26350_36061; BA_HECTOR=2gak2h0h8425842l1p1h51u1t0q'
            # 'Host': 'fanyi.baidu.com',
            # 'Origin': 'https://fanyi.baidu.com',
            # 'Referer':' https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
            # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"''',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-ch-ua-platform': 'Windows',
            # 'Sec-Fetch-Dest': 'empty',
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Site':' same-origin',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            # 'X-Requested-With': 'XMLHttpRequest'
}
data = {
                'from': 'zh',
                'to': 'en',
                'query': '梦想是',
                'transtype': 'realtime',
                'simple_means_flag': '3',
                'sign':  '403647.183182',
                'token': '9ff06e4bffc482c18575932b7ab41311',
                'domain': 'commo'

}
# post请求的参数，必须进行编码encode()
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求参数，是不会拼接在url后面的，而是需要放在请求对象的定制中
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求r
response = urllib.request.urlopen(request)

# 获取数据
content = response.read().decode('utf-8')
#print(content)

obj = json.loads(content)
print(obj)






