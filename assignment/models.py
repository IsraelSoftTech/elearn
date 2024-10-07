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
        return f"{self.question_type} | {self.question}"


class StructuralQuestion(models.Model): 
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000, blank=True)
    question_type = models.CharField(max_length=20, default="STRUCT")

    def __str__(self): 
        return f"{self.question_type} | {self.question}"


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

class MCQStudentAnswer(models.Model): 
    student = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    question = models.OneToOneField(MCQQuestion, on_delete=models.CASCADE, null=True)
    choice = models.OneToOneField(MCQChoice, on_delete=models.CASCADE, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.student.user.username} {self.question.question}"

class StructuralStudentAnswer(models.Model): 
    student = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, related_name="struct_question")
    question = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=2000)
    is_correct = models.BooleanField(default=False)
    score = models.IntegerField(blank=True)

    def __str__(self): 
        return f"{self.student.user.username} {self.question.question}"

class AssignAssignmentSubmission(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='assignAssignementSubmission')
    assignment = models.OneToOneField(Assignment, on_delete=models.CASCADE, related_name="assignment")
    mcq_answers = models.ManyToManyField(MCQStudentAnswer, blank=True)
    stuctural_answers = models.ManyToManyField(StructuralStudentAnswer, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True, blank=True)
    grade = models.CharField(max_length=2, blank=True)
    total_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0, blank=True)
    is_graded = models.BooleanField(default=False)
    graded_by = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True, blank=True)
    graded_on = models.DateTimeField(auto_now_add=True, blank=True)

    
    def __str__(self):
        return f"{self.student.user.username} {self.assignment.title}"




