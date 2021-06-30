from django.contrib import admin
from tgbot.models import Chat, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass
