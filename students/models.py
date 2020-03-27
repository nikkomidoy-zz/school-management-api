import uuid

from django.core.exceptions import ValidationError
from django.db import models
from model_utils.models import TimeStampedModel

from schools.models import School


class Student(TimeStampedModel):
    """
    Model for Student
    """
    student_id = models.UUIDField(
        default=uuid.uuid4, editable=False
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='students'
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def check_maximum_student_count(self):
        if self._state.adding and (self.school.students.count() + 1) > self.school.max_student_count:
            raise ValidationError(
                'Maximum number of students of this school is reached.'
            )

    def clean(self):
        self.check_maximum_student_count()
