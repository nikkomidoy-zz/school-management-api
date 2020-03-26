from django.db import models
from model_utils.models import TimeStampedModel


class School(TimeStampedModel):
    """
    Model for School
    """
    name = models.CharField(max_length=20)
    max_student_count = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name
