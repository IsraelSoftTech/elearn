from django.urls import path
from course.api import views

urlpatterns = [
    path('list/', views.CourseList.as_view(), name='course-list'),
    path('<int:pk>', views.CourseDetails.as_view(), name='course')
]
