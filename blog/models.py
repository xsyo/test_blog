from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    '''Класс Поста'''
    title = models.CharField(max_length=255,verbose_name='Имя')
    img = models.ImageField(upload_to='posts/%Y/%m/%d/', verbose_name='Изобродение поста')
    content = RichTextUploadingField(verbose_name='Содержание')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published',]


