import requests
import json
# 获取最新视频列表
# https://api.bilibili.com/x/space/wbi/arc/search?mid=23947287&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&w_rid=cefc6ff6a9b2003dd001e7ff4d7e21cb&wts=1693982211

def new_vedio_list(mid,pageNum,pageSize):
    url='https://api.bilibili.com/x/space/wbi/arc/search'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    params = {
        'mid': mid,
        'pn':pageNum,
        'ps':pageSize,
        'order':'pubdate'
    }
    json= requests.get(url,params=params,headers=headers).json()
    return json

# 获取用户信息
# https://api.bilibili.com/x/space/wbi/acc/info?mid=23947287&token=&platform=web&web_location=1550101&w_rid=76d46ebbed24101710fdcb030df91d61&wts=1693982211
def upinfo(mid):
    url = 'https://api.bilibili.com/x/space/wbi/acc/info'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    params = {
        "mid":mid
    }
    json = requests.get(url,params=params,headers=headers).json()
    return json

# 统计信息
# https://api.bilibili.com/x/space/navnum?mid=23947287
def navnum(mid):
    url = 'https://api.bilibili.com/x/space/navnum'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    params = {
        "mid":mid
    }
    json = requests.get(url,params=params,headers=headers).json()
    return json

def saveInfo(jsonStr,fileName):
    # base path = src/assets/fileName
    
    return


print(new_vedio_list(23947287,1,10)['data'])
print(upinfo(23947287))
print(navnum(23947287)['data'])