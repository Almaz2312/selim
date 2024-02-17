from datetime import datetime

import factory
from factory.django import DjangoModelFactory

from products.models import Category, Feedback, OurWorks, Product, ProductImage


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("name", "id")

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: "category{}".format(n))
    image = factory.django.ImageField()
    description = factory.Sequence(lambda n: "sequence{}".format(n))


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
        django_get_or_create = ("type", "id")

    id = factory.Sequence(lambda n: n)
    type = factory.Sequence(lambda n: "product{}".format(n))
    description = factory.Sequence(lambda n: "sequence{}".format(n))
    created_at = datetime.now()
    updated_at = datetime.now()
    category = factory.SubFactory(CategoryFactory)


class FeedbackFactory(DjangoModelFactory):
    class Meta:
        model = Feedback
        django_get_or_create = ("name", "id")

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: "feedback{}".format(n))
    image = factory.django.ImageField()
    body = factory.Sequence(lambda n: "body{}".format(n))
    type = factory.SubFactory(ProductFactory)


class ProductImageFactory(DjangoModelFactory):
    class Meta:
        model = ProductImage

    image = factory.django.ImageField()
    product = factory.SubFactory(ProductFactory)
