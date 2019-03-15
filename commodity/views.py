from django.shortcuts import render
from django.db import models
from .models import *
from django.http import HttpResponse,HttpRequest
# Create your views here.


def index(request):
    dity = commonDity.objects.all()
    context = {'commondity':dity}
    return render(request,'index.html',context)



def commonlist(request):
    return render(request,'commondity/commonlist.html')


def shoplist(request,id):
    comid = id

    shopobj = shopname.objects.filter(common_id=comid)

    context = {'shoplist':shopobj}

    return render(request,'commondity/shoplist.html',context)