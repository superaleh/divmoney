from django.db import models


class UserManager(models.Manager):
    def get_user(self, user_data):
        defaults_data = {
            'username': user_data.username,
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
        }
        u, _ = self.update_or_create(user_id=user_data.id, defaults=defaults_data)
        return u


class ChatManager(models.Manager):
    def get_chat(self, chat_id):
        c, _ = self.get_or_create(chat_id=chat_id)
        return c
