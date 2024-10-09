from django.urls import path 
from .views import *

urlpatterns = [
    path('list/', AssignmentList.as_view(), name='assignment-list'),
    path('<int:pk>', AssignmentDetail.as_view(), name='assignment'),

    # MCQ questions 
    path("<int:assignment_id>/mcq-question/list/", MCQQuestionList.as_view(), name='mcq-question-list'),
    path("<int:assignment_id>/mcq-question/<int:pk>", MCQQuestionDetail.as_view(), name='mcq-question-detail'),

    # MCQ choice
    path('<int:assignment_id>/mcq-question/<int:mcq_id>/choice/list', MCQChoiceList.as_view(), name='mcq-question-choice-list'),
    path('<int:assignment_id>/mcq-question/<int:mcq_id>/choice/<int:choice_id>', MCQChoiceDetail.as_view(), name='mcq-question-choice'),

    # Structural Question 
    path("<int:assignment_id>/strut-question/list", StructuralQuestionList.as_view(), name='strut-question-list'), 
    path("<int:assignment_id>/strut-question/<int:struct_question_id>", StructuralQuestionDetail.as_view(), name='strut-question'), 


    # student submission 
    path("<int:assignment_id>/submissions", StudentSubmissionList.as_view(), name='assigment-submission'), 

    
]