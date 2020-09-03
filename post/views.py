from django.shortcuts import render

from . models import Blog





def head(request):

    posts = Blog.objects.all()



    return render(request ,'post/index.html' , {'post' : posts})
