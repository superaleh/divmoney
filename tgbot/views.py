import telebot
from django.views import View
from django.http import JsonResponse, HttpResponseNotFound
from tgbot.handlers import bot


def index(request):
    return JsonResponse({"error": "sup hacker"})


class TelegramBotWebhookView(View):
    def post(self, request, *args, **kwargs):
        if request.META['CONTENT_TYPE'] == 'application/json':
            json_data = request.body.decode('utf-8')
            update = telebot.types.Update.de_json(json_data)
            bot.process_new_updates([update])
            return JsonResponse({"ok": "POST request processed"})
        return HttpResponseNotFound()

    def get(self, request, *args, **kwargs):
        return JsonResponse({"ok": "Get request processed. But nothing done"})
