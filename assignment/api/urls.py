from django.urls import path 
from .views import *

urlpatterns = [
    path('list/', AssignmentList.as_view(), name='assignment-list'),
    path('<int:pk>', AssignmentDetail.as_view(), name='assignment'),

    # MCQ questions 
    path("mcq-question/list/", MCQQuestionList.as_view(), name='mcq-question-list'),
    path("mcq-question/<int:pk>", MCQQuestionDetail.as_view(), name='mcq-question-detail'),

    # MCQ choice
    path('mcq-question/choice/list', MCQChoiceList.as_view(), name='mcq-question-choice'),
]