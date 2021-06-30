import re
import logging
import telebot
from django.db.models import Sum
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from project.settings import TELEGRAM_TOKEN, WEBHOOK_URL
from money.models import Category, Expense
from money.services import get_report_chat
from tgbot.models import Chat, User
from tgbot import static_text


# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')
# Установка урл вебхук для telegram api
# bot.set_webhook(url=WEBHOOK_URL)
# Включаю логирование
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, static_text.start_help)


@bot.message_handler(commands=['cat'])
def create_category(message):
    chat = Chat.objects.get_chat(message.chat.id)
    regexp_result = re.findall(r'\w+', message.text)
    text = static_text.category_not_created
    if len(regexp_result) > 1:
        name = ' '.join(regexp_result[1:])
        Category.objects.create(name=name, chat=chat)
        text = static_text.category_created.format(name=name)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['add'])
def create_expense(message):
    user = User.objects.get_user(message.from_user)
    chat = Chat.objects.get_chat(message.chat.id)
    chat.members.add(user)
    regexp_result = re.findall(r'\d+', message.text)
    if regexp_result:
        amount = regexp_result[0]
        Expense.objects.create(amount=amount, user=user, chat=chat)
        keybord = InlineKeyboardMarkup()
        for cat in Category.objects.filter(chat=chat):
            keybord.add(InlineKeyboardButton(cat.name, callback_data=f'{cat.id}'))
        bot.reply_to(message, static_text.expense_added.format(amount=amount), reply_markup=keybord)
    else:
        bot.reply_to(message, static_text.no_expense_added)


@bot.callback_query_handler(func=lambda call: True)
def assign_category(call):
    user = User.objects.get_user(call.message.reply_to_message.from_user)
    chat = Chat.objects.get_chat(call.message.chat.id)
    expense = Expense.objects.filter(user=user, chat=chat).last()
    cat = Category.objects.get(id=call.data)
    expense.category = cat
    expense.save()
    # отправляю ответ, чтобы выключить загрузку у кнопки
    bot.answer_callback_query(call.id)
    # убираю кнопки у сообщения
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    # меняю сообщение
    bot.edit_message_text(static_text.expese_cat.format(amount=expense, cat=cat),
                          call.message.chat.id, call.message.message_id)


@bot.message_handler(commands=['rep'])
def report(message):
    chat = Chat.objects.get_chat(message.chat.id)
    data = get_report_chat(chat)
    text = f"В группе потрачено — {data['total']} на {len(data['members'])} человек\n"
    for cat in data['categories']:
        text += f"{cat['total']} — {cat['name']}\n"
    if data['no_cat_tota']:
        text += f"{data['no_cat_tota']} — без категории\n"
    text += '=============' if len(data['members']) > 1 else ''
    for m in data['members']:
        text += f"\n@{m['username']} потратил — {m['total']}"
        text += f", а должен — {m['debt']}" if m['debt'] else ''
    bot.send_message(message.chat.id, text)
