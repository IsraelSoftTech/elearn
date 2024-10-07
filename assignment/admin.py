from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MCQChoice)
admin.site.register(MCQQuestion)
admin.site.register(StructuralQuestion)
admin.site.register(AssignAssignmentSubmission)
admin.site.register(Assignment)
admin.site.register(StructuralStudentAnswer)
admin.site.register(MCQStudentAnswer)
