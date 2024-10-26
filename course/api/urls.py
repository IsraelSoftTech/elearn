from django.urls import path
from course.api import views

urlpatterns = [
    path('list/', views.CourseList.as_view(), name='course-list'),
    path('<int:pk>', views.CourseDetails.as_view(), name='course'), 

    # assign teacher to course
    path('assign-tutor', views.CourseAssignTeacher.as_view(), name='assign_tutor'),
    path('unassign-tutor', views.CourseUassignTeacher.as_view(), name='unassign_tutor'),
    #  enroll studends
    # path('enroll', views.CourseEnroll.as_view(), name="enroll_student"), 
    # path('unenroll', views.CourseOnenroll.as_view(), name="unenroll_student"),

    # content list 
    path('<int:course_id>/content/list', views.ContentList.as_view(), name='content-list'), 
    path('<int:course_id>/content/<int:pk>', views.ContentDetail.as_view(), name='content'),

    # assignment creation
    path('<int:course_id>/assignment/list', views.CourseAssignmentList.as_view(), name='course-assignment'),
    path('<int:course_id>/assignment/<int:assignment_id>', views.CourseAssignmentDetail.as_view(), name='course-assignment-detail')

]
