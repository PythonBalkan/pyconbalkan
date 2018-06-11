from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import viewsets

from pyconbalkan.conference.models import Conference
from pyconbalkan.news.models import Post
from pyconbalkan.news.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def news_view(request):
    conference = Conference.objects.filter(active=True)
    posts = Post.objects.filter(active=True, published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'news': posts,
        'conference': conference.first() if conference else None,
    }
    return render(request, 'news.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, active=True, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'post.html', context)