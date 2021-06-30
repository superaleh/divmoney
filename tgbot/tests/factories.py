import factory
from tgbot import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    user_id = factory.Sequence(lambda n: n)
    username = factory.LazyAttribute(lambda a: '{}_{}'.format(a.first_name, a.last_name).lower())
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('first_name')


class ChatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Chat

    chat_id = factory.Sequence(lambda n: n)

    @factory.post_generation
    def members(self, create, extracted):
        if not create:
            return

        if extracted:
            for m in extracted:
                self.members.add(m)
