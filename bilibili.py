import requests
import json
import time
import math

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
    return json['data']

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
    return json['data']

# 稿件统计
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
    return json['data']


# 合集信息 https://api.bilibili.com/x/polymer/web-space/seasons_archives_list?mid=23947287&season_id=665&sort_reverse=false&page_num=1&page_size=30
def seasons_archives_list(mid,seasonId,pageNum):
    url = 'https://api.bilibili.com/x/polymer/web-space/seasons_archives_list'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    params = {
        "mid":mid,
        "season_id":seasonId,
        "page_num":pageNum,
        "sort_reverse": True,
        "page_size":30
    }
    json = requests.get(url,params=params,headers=headers).json()
    return json['data']


# up主统计数据  https://api.bilibili.com/x/relation/stat?vmid=23947287&w_rid=e6a6e31cc15fa5b806f9f1ad6ce548bb&wts=1695312456&web_location=333.999
def up_stat(mid):
    url = 'https://api.bilibili.com/x/relation/stat'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    params = {
        "vmid":mid,
    }
    json = requests.get(url,params=params,headers=headers).json()
    return json['data']


def saveInfo(jsonObj,fileName):
    basePath = "src/assets/{fileName}"
    with open(basePath.format(fileName=fileName),"w", encoding='utf-8') as f:
        f.write(json.dumps(jsonObj,ensure_ascii=False,indent=4))
    return

def readFile(fileName:str):
    basePath = "src/assets/{fileName}"
    with open(basePath.format(fileName=fileName),"r", encoding='utf-8') as f:
        content = f.read()
        return json.loads(content)


def saveFile(url:str):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    urls= url.split("/")
    path = urls[len(urls)-1]
    response = requests.get(url,headers=headers)
    basePath = "public/image/{path}"
    
    bytes = response.content

    with open(basePath.format(path=path),"wb") as f:
        f.write(bytes)

    return path


# print(new_vedio_list(23947287,1,10)['data'])
# print(upinfo(23947287))
# print(navnum(23947287)['data'])
# print(seasons_archives_list(23947287,665,1))
# upinfo(23947287)
# up_stat(23947287)

def john_info():
    mid = 23947287
    up_stat_info= up_stat(mid)
    upinfo_json= upinfo(mid)

    john ={
        "mid": mid,
        "name": upinfo_json['name'],
        "sign": upinfo_json['sign'],
        "avatar": upinfo_json['face'], 
        "birthday": upinfo_json['birthday'], 
        "sex": upinfo_json['sex'],
        "title": upinfo_json['official']['title'],
        "follower": up_stat_info['follower'],
        "space":"https://space.bilibili.com/{0}".format(mid),
        "live_room": upinfo_json["live_room"]["url"],
    }

    path= saveFile(john['avatar'])

    john['avatar'] = path

    saveInfo(john,"john.json")
    return

def liganma_info():
    mid = 1156068103
    up_stat_info= up_stat(mid)
    upinfo_json= upinfo(mid)

    john ={
        "mid": mid,
        "name": upinfo_json['name'],
        "sign": upinfo_json['sign'],
        "avatar": upinfo_json['face'], 
        "birthday": upinfo_json['birthday'], 
        "sex": upinfo_json['sex'],
        "title": upinfo_json['official']['title'],
        "follower": up_stat_info['follower'],
        "space":"https://space.bilibili.com/{0}".format(mid),
        "live_room": '' if upinfo_json["live_room"] == None else upinfo_json["live_room"]["url"],
    }

    path= saveFile(john['avatar'])

    john['avatar'] = path

    saveInfo(john,"liganma.json")
    return

def season(mid,seasonId,fileName):
    pageNum = 1
    bvBathPath = "https://www.bilibili.com/video/{bvid}"
    durationInfo = "{m}分{s}秒"
    
    all_archives=[]

    dataInFile = readFile(fileName=fileName)
    
    while True :
        seasons_archives= seasons_archives_list(mid,seasonId,pageNum)
        page = seasons_archives['page']
        archives = seasons_archives['archives']
        for item in archives :
            
            data = None

            for f in dataInFile:
                if f['bvid'] == item['bvid']:
                    data = f

            all_archives.append({
                "countryName":data['countryName'] if data != None and 'countryName' in data else ['#'],
                "leader":data['leader'] if data != None and 'leader' in data else ['#'],
                "personName":data['personName'] if data != None and 'personName' in data else ['#'],
                "organizationName":data['organizationName'] if data != None and 'organizationName' in data else ['#'],
                "name": item['title'],
                "bvid": item['bvid'],
                "aid": item['aid'],
                "cover": item['pic'],
                "view": item['stat']['view'],
                'duration': durationInfo.format(m=math.floor( item['duration'] / 60 ),s=item['duration'] % 60),
                "pub_date": time.strftime("%Y-%m-%d", time.localtime(item['pubdate'])) ,
                "url": bvBathPath.format(bvid=item['bvid'])
            })

        if(page['page_num'] * page['page_size'] >= page['total']):
            break
        pageNum+=1

    # 下载封面
    

    for item in all_archives:
        path= saveFile(item['cover'])
        item['cover'] = path

    saveInfo(all_archives,fileName)
    return



def country():
    mid = 23947287
    seasonId = 665
    season(mid,seasonId,"country.json")
    return

def person():
    mid = 23947287
    seasonId = 3491
    season(mid,seasonId,"person.json")
    return

def organization():
    mid = 23947287
    seasonId = 1095498
    season(mid,seasonId,"organization.json")
    return

liganma_info()
john_info()
country()
person()
organization()
