import factory
from . import models

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model= 'inventory.Category'

    name = factory.Faker('name')
