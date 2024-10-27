from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [ 

    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', views.CreateUser.as_view(), name='register'),
    
]