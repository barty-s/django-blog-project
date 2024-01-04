from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filer(status=1).order_b('-created_on')
    template_name = 'index.html'
    paginate_by = 6
