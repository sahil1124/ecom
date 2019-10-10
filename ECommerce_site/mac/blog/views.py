from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request):
    # postId=Blogpost.objects.all()
    # all_posts=[]
    # for id in postId:
    #     all_posts.append(id)
    # params={'all_posts':all_posts}
    myposts=Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html',{'myposts':myposts})

    # def __str__(self):
    #     return self.title

def blogpost(request,id):
    # postId=Blogpost.objects.all()
    post=Blogpost.objects.filter(post_id=id)[0]

    print(post)
    return render(request,'blog/blogpost.html',context={'post':post})
