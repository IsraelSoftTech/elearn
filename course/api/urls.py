from django.urls import path
from course.api import views

urlpatterns = [
    path('list/', views.CourseList.as_view(), name='course-list'),
    path('<int:pk>', views.CourseDetails.as_view(), name='course'), 


    # content list 
    path('<int:course_id>/content/list', views.ContentList.as_view(), name='content-list'), 
    path('<int:course_id>/content/<int:pk>', views.ContentDetail.as_view(), name='content'),

    # assignment creation
    path('<int:course_id>/assignment/list', views.CourseAssignmentList.as_view(), name='course-assignment')

]
