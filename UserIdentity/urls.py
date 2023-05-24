from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('user/',views.user.as_view(),name='user'),
    path('login/',obtain_auth_token,name='login'),
    path('welcome/',views.welcome.as_view(),name='welcome'),
    path('user/<int:pk>/',views.userDetails.as_view(),name='userDetails'),
    path('user_role/',views.user_role.as_view(),name='userRole'),
    path('user_role/<str:role_id>/',views.user_role_Details.as_view(),name='userroleDetails')
]