from django.shortcuts import get_object_or_404, render

from .models import Group, Post


# Create your views here.
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
