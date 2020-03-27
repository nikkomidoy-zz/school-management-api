from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError

from schools.serializers import SchoolSerializer
from students.models import Student


class StudentSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        school_obj = validated_data.get('school')
        if (school_obj.students.count() + 1) > school_obj.max_student_count:
            raise ValidationError(
                'Maximum number of students of this school is reached.'
            )

        return super().create(validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['school'] = SchoolSerializer(instance=instance.school).data

        return ret
