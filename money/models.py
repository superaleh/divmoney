from main.mixins import TimeStampedModelMixin
from django.db import models


class Expense(TimeStampedModelMixin, models.Model):
    user = models.ForeignKey('tgbot.User', related_name='expenses',
                             verbose_name='Пользователь', on_delete=models.PROTECT)
    chat = models.ForeignKey('tgbot.Chat', related_name='expenses',
                             verbose_name='Группа', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', related_name='expenses',
                                 verbose_name='Категория', null=True, default=None, on_delete=models.SET_NULL)
    amount = models.IntegerField('Сумма')

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'


class Category(TimeStampedModelMixin, models.Model):
    name = models.CharField(max_length=100)
    chat = models.ForeignKey('tgbot.Chat', related_name='categories',
                             verbose_name='Группа', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
