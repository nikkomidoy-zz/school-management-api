from rest_framework import serializers

from schools.serializers import SchoolSerializer
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    # def validate_school(self, value):
    #     """
    #     Check whether number of students exceed on the number of count
    #     """
    #
    #
    # NOTE: Check also if its good to separate both serializers for create and list
