from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from schools.models import School
from schools.serializers import SchoolSerializer
from utils.views import CacheResponseAndETAGMixin


class SchoolViewSet(NestedViewSetMixin,
                    CacheResponseAndETAGMixin,
                    viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filterset_fields = ('name',)
    search_fields = ('name',)
    ordering_fields = ('created',)
