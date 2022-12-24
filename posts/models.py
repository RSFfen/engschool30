from django.db import models


class Post(models.Model):
    text = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
