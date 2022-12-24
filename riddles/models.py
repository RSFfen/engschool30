from django.db import models


class Riddle(models.Model):
    riddle_text = models.CharField(max_length=255, verbose_name='Текст загадки')
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации загадки')

    def __str__(self):
        return self.riddle_text[:50]


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Option(models.Model):
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='Текст варианта ответа')
    correct = models.BooleanField(default=False, verbose_name='Верный вариант ответа')

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
