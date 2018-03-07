from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by("-date")[:25]
    return render(request, 'blog/blog.html', {'posts': posts})
