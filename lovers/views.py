from django.shortcuts import render
from .models import loveclass,songer,songcomment
import requests
import json,time
from bs4 import BeautifulSoup
from django.http import HttpResponse
# Create your views here.


def lovelist(request):
    lover = loveclass.objects.all()
    context = {
        'lover':lover
    }


    return render(request,'lovers/create.html',context)

# def songcommesnt(request):
#
#     url = 'https://music.163.com/artist?id=6452'
#     headers = {'content-type': 'application/json',
#                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
#     req = requests.get(url=url,headers=headers)
#
#     res = BeautifulSoup(req.content,'html.parser')
#
#     con_list =  res.find_all('ul',class_='f-hide')
#
#     sid = {}
#
#     for i in con_list:
#         ia = i.findAll('a')
#         for j in ia:
#             id = str(j['href'])
#
#             sid[j.string] = id.split('=',1)[1]
#
#     for s in sid:
#         songobj = songer.objects.all()
#         nid = int(sid[s])
#         songobj.create(songername='周杰伦',musicname=s,songid=nid)
#
#     return HttpResponse('添加信息成功')


def songlist(request,ser):

    songobj = songer.objects.filter(songername=ser)

    context = {
        'songli':songobj
    }

    return render(request,'lovers/songlist.html',context)


def songcomments(request,sid,songname):
    music = '"https://music.163.com/#/song?id='
    url = music + str(sid)
    rname_id = url.split('=')[1]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",}
       # "referer": "http://music.163.com/song?id=4466775&market=baiduqk"}

    params = "PWXGrRPQKqZfgF4QTEivQ9eZfrCscY2YtKA60Xw6P6kL6v4J09c/g+PNwzks+mpwUDmjDWvJ0CNfV/Vzeh0iLNIVyWZ+9wezTESdC2/lpPKgcSgFo8au3evlS5OpciLmVG7YGhEFiocZQ/ccGaFdG4WdqStjPDEIoBfzeGZJZIsixW0SG4zVhBrfgKTi0i22"
    encSecKey = "61be0f8c5305c919985b294069695d2ba84746c75ed902e8157b6b595a920c57cfedf552f5c764fed37be84bfd1cce31e05eb364644930fbe6bc074747ed8e670933aef4d8b8841209c6956f4b532f8a3caadfaffb61f233a42e53dc5795183b9c6ccb30b8aa56d656466cc6523e8213560bb3e476ab95d58755f47f91cf7f53"

    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    target_url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}??csrf_token=".format(rname_id)
    res = requests.post(target_url, headers=headers, data=data)

    comments_json = json.loads(res.text)

    hot_comments = comments_json['hotComments']

    for i in hot_comments:

        commentid = i['commentId']


        try:
            if songcomment.objects.get(comment_id=commentid):
                continue
        except:
            user = i['user']['nickname']
            avatarurl = i['user']['avatarUrl']
            likeCount = int(i['likedCount'])
            ctime = i['time']
            timeArray = time.localtime(ctime)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            content = i['content']

            comm = songcomment.objects.all()
            comm.create(comment_id=commentid,songname=songname,commenter=user,comment=content,likedcount=likeCount,avatarurl=avatarurl,comment_time=otherStyleTime)

    comlist = songcomment.objects.filter(songname=songname)

    context = {
        'comlist':comlist,
        'songname':songname,
    }

    return render(request,'lovers/commentlist.html',context)


