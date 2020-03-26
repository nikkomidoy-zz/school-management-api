import factory
from factory.django import DjangoModelFactory

from schools.models import School


class SchoolFactory(DjangoModelFactory):
    name = factory.Faker('city')

    class Meta:
        model = School
        django_get_or_create = ('name',)
