from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404
import markdown
# Create your views here.


def index(request,):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'index.html',
        context={ 'name':'wenhe','post_list': post_list})


def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'post': post})



def hello(request):
    return HttpResponse('hello dog')