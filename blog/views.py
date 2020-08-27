from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .models import Post

def main(request):
    '''Главная страница'''
    
    context = {
        'last_post': Post.objects.first(),
        'posts': Post.objects.all()[1:10]
    }
    return render(request, 'blog/main.html', context)

class PostCreateView(CreateView):
    '''Страница для создания нового поста'''

    model = Post
    template_name = 'blog/post_create.html'
    fields = ('title', 'img', 'content')

class PostDetailView(DetailView):
    '''Страница отдельного поста'''

    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'