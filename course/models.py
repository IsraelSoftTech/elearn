from django.db import models
from user.models import Profile
from assignment.models import Assignment
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    content = models.ManyToManyField('Content', blank=True)
    teacher = models.ManyToManyField(Profile, related_name='course_teacher',  blank=True)
    enrolled_students = models.ManyToManyField(Profile, related_name='course_enrolled_in', blank=True)
    # reviews = 
    # comments =
    assignments = models.ManyToManyField(Assignment, blank=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_by = models.ManyToManyField(Profile, related_name='created_by',  blank=True)
    assignments = models.ManyToManyField(Assignment, blank=True)
    # class_taken = 
    media = models.FileField(upload_to='files', null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    assignments = models.ManyToManyField(Assignment, blank=True)


    def __str__(self):
        return self.title