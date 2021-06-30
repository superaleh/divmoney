import factory
from money.models import Category, Expense
from tgbot.tests.factories import ChatFactory, UserFactory


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'name_{n}')


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense
