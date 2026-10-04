from django.contrib import admin
from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list),           # Главная страница со списком постов
    path('post/<int:post_id>/', post_detail), # Страница конкретной статьи
]