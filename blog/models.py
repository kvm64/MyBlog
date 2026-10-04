from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200) # Заголовок
    content = models.TextField() # Текст статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Автор
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания

    def __str__(self):
        return self.title