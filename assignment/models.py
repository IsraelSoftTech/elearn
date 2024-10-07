from django.db import models
from user.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator

class MCQChoice(models.Model): 
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

class MCQQuestion(models.Model): 
    question = models.CharField(max_length=500)
    choices = models.ManyToManyField(MCQChoice, blank=True)
    question_type = models.CharField(max_length=20, default="MCQ")

    def __str__(self): 
        return f"{self.question} {self.question_type}"


class StructuralQuestion(models.Model): 
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)
    question_type = models.CharField(max_length=20, default="STRUCT")

    def __str__(self): 
        return self.question


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    reference_link = models.URLField(max_length=150, null=True, blank=True)
    media_content = models.FileField(upload_to="assignement", null=True, blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="creator")
    assigned_students = models.ManyToManyField(Profile, blank=True)
    mcq_questions = models.ManyToManyField(MCQQuestion, blank=True)
    struct_questions = models.ManyToManyField(StructuralQuestion, blank=True)

    def __str__(self): 
        return self.title


class AssignAssignmentSubmission(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='assignAssignementSubmission')
    assignment = models.OneToOneField(Assignment, on_delete=models.CASCADE, related_name="assignment")
    submission_date = models.DateTimeField(auto_now_add=True, blank=True)
    grade = models.CharField(max_length=2, blank=True)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True)
    is_graded = models.BooleanField(default=False)
    graded_by = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True, blank=True)
    graded_on = models.DateTimeField(auto_now_add=True, blank=True)

    
    def __str__(self):
        return f"{self.student.user.username} {self.assignment.title}"




