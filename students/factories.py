import factory
from factory.django import DjangoModelFactory

from schools.factories import SchoolFactory
from students.models import Student


class StudentFactory(DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    school = factory.SubFactory(SchoolFactory)

    class Meta:
        model = Student
        django_get_or_create = ('first_name',)
