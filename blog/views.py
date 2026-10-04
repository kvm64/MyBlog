from django.shortcuts import render
from .models import Post

def post_list(request):
    # Получаем все посты из базы данных, отсортированные по дате
    posts = Post.objects.all().order_by('-created_at')
    # Передаём их в шаблон blog/post_list.html
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    # Получаем один конкретный пост по его ID
    post = Post.objects.get(id=post_id)
    # Передаём его в шаблон blog/post_detail.html
    return render(request, 'blog/post_detail.html', {'post': post})