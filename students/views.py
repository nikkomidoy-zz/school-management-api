from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from students.models import Student
from students.serializers import StudentSerializer
from utils.views import CacheResponseAndETAGMixin


class StudentViewSet(NestedViewSetMixin,
                     CacheResponseAndETAGMixin,
                     viewsets.ModelViewSet):
    queryset = Student.objects.all().prefetch_related('school')
    serializer_class = StudentSerializer
    filterset_fields = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)
    ordering_fields = ('created', 'first_name',)
