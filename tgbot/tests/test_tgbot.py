import pytest
from tgbot.models import User, Chat


@pytest.mark.django_db
def test_get_user():
    class UserData:
        id = 1
        username = 'user_test'
        first_name = 'First'
        last_name = 'Last'
    user_data = UserData()
    user = User.objects.get_user(user_data)
    assert user.username == 'user_test'
    assert user.first_name == 'First'
    assert user.last_name == 'Last'


@pytest.mark.django_db
def test_get_chat():
    chat = Chat.objects.get_chat(chat_id=1)
    assert chat.chat_id == 1
