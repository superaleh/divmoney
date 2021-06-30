from money.services import get_report_chat
import pytest
from tgbot.tests.factories import ChatFactory, UserFactory
from money.tests.factories import CategoryFactory, ExpenseFactory


@pytest.mark.django_db
def test_report_chat():
    user_1 = UserFactory.create()
    user_2 = UserFactory.create()
    chat = ChatFactory.create(members=(user_1, user_2))

    cat_1 = CategoryFactory.create(chat=chat)
    cat_2 = CategoryFactory.create(chat=chat)
    ExpenseFactory.create(amount=100, user=user_1, chat=chat, category=cat_1)
    ExpenseFactory.create(amount=200, user=user_1, chat=chat, category=cat_2)
    ExpenseFactory.create(amount=50, user=user_2, chat=chat)

    data = get_report_chat(chat)
    assert data['total'] == 350
    assert len(data['categories']) == 2
    assert data['no_cat_total'] == 50
    assert len(data['members']) == 2
    member = list(filter(lambda m: m['username'] == user_2.username, data['members']))
    assert member[0]['debt'] == 125
