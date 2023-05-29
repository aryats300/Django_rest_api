
from django.urls import path
from .user_views import UserAPIView, WelcomeAPIView, UserDetailsAPIView
from .user_role_views import UserRoleAPIView, UserRoleDetailsAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .user_assign_views import AssignUserRoleAPI,UserRolesAPI


urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    path('auth/login', TokenObtainPairView.as_view(), name='authLogin'),
    path('auth/refresh', TokenRefreshView.as_view(), name='authRefresh'),
    path('welcome/', WelcomeAPIView.as_view(), name='welcome'),
    path('user/<int:pk>/', UserDetailsAPIView.as_view(), name='userDetails'),
    path('user_role/', UserRoleAPIView.as_view(), name='userRole'),
    path('user_role/<str:role_id>/', UserRoleDetailsAPIView.as_view(), name='userroleDetails'),
    # path('authenticate/', UserAuthenticationAPI.as_view()),

    path('assign_role/<int:pk>/', AssignUserRoleAPI.as_view(), name='assign_role'),

     path('user_roles/<int:pk>/', UserRolesAPI.as_view(), name='userRoles'),
]

