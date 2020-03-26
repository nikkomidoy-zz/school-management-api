import uuid

from django.db import models
from model_utils.models import TimeStampedModel

from schools.models import School


class Student(TimeStampedModel):
    """
    Model for Student
    """
    student_id = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
