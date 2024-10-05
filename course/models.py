from django.db import models
from user.models import Profile

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    content = models.ManyToManyField('Content', blank=True)
    teacher = models.ManyToManyField(Profile, related_name='course_teacher',  blank=True)
    enrolled_students = models.ManyToManyField(Profile, related_name='course_enrolled_in', blank=True)
    # reviews = 
    # comments =

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_by = models.ManyToManyField(Profile, related_name='created_by',  blank=True)
    # assignements =
    # class_taken = 
    media = models.FileField(upload_to='files', null=True, blank=True)

    def __str__(self):
        return self.title