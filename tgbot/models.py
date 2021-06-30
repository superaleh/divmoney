from django.db import models
from main.mixins import TimeStampedModelMixin
from tgbot.managers import ChatManager, UserManager


class User(TimeStampedModelMixin, models.Model):
    objects = UserManager()
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    class Meta:
        verbose_name = 'Профиль TG'
        verbose_name_plural = 'Профили TG'


class Chat(TimeStampedModelMixin, models.Model):
    objects = ChatManager()
    chat_id = models.BigIntegerField(primary_key=True)
    members = models.ManyToManyField(User, related_name='chats')

    def __str__(self):
        return f'{self.chat_id}'

    class Meta:
        verbose_name = 'Чат TG'
        verbose_name_plural = 'Чаты TG'
