from django.shortcuts import render
from .models import bloglist
import markdown
# Create your views here.
def bloglistall (request):
    bglist = bloglist.objects.all()


    context = {
        'bglist':bglist
    }


    return render(request,'blog/bloglist.html',context)


def blogDetail (request,id):

    bglist = bloglist.objects.get(id=int(id))
    bglist.total_views += 1
    bglist.save(update_fields=['total_views'])
    bglist.content = markdown.markdown(bglist.content,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    context = {
        'bglist':bglist
    }


    return render(request,'blog/blogDetail.html',context)


def taglist(request,tag):
    tl = bloglist.objects.filter(category=tag)

    context = {
        'tagl':tl
    }

    return render(request,'blog/tagList.html',context)