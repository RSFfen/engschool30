from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок заметки')
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name='Автор заметки')
    body = models.TextField(verbose_name='Текст заметки')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
