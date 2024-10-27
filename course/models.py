from django.db import models
from user.models import Profile, Discussion
from assignment.models import Assignment

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    content = models.ManyToManyField('Content', blank=True)
    teachers = models.ManyToManyField(Profile, related_name='course_teacher',  blank=True)
    enrolled_students = models.ManyToManyField(Profile, related_name='course_enrolled_in', blank=True)
    # reviews = 
    # comments =
    # classes = models.ManyToManyField(blank=True)
    assignments = models.ManyToManyField(Assignment, blank=True)
    discussions = models.ManyToManyField(Discussion, blank=True, related_name='course_discussions')

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
    discussions = models.ManyToManyField(Discussion, blank=True, related_name='content_discussions')
    

    # checking the progress of the course 
    # still to do alot of work here.
    def course_progress(self): 
        if self.is_complete: 
            return 100
        else: 
            return 0

    def __str__(self):
        return self.title