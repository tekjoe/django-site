from django.conf.urls import url, include
from django.views.generic import DetailView
from .models import Post
from . import views

urlpatterns =[
    url(r'^$', views.post_list, name='blog'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
                                            template_name="blog/post.html")),
]
