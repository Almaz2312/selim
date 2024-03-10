import factory

from news.models import News, NewsImage


class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News

    title = factory.Faker("sentence", nb_words=4)
    body = factory.Faker("paragraph")


class NewsImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NewsImage

    news = factory.SubFactory(NewsFactory)
    title = factory.Faker("sentence", nb_words=3)
    image = factory.Faker("image_url")
