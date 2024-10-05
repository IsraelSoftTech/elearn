from django.urls import path
from course.api import views

urlpatterns = [
    path('list/', views.CourseList.as_view(), name='course-list'),
    path('<int:pk>', views.CourseDetails.as_view(), name='course'), 

    # content list 
    path('content/list', views.ContentList.as_view(), name='content-list'), 
    path('content/<int:pk>', views.ContentDetail.as_view(), name='content')
]
