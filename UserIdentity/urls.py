from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('user/',views.user.as_view(),name='user'),
    path('login/',obtain_auth_token,name='login'),
    path('welcome/',views.welcome.as_view(),name='welcome'),
    path('userDetails/<int:pk>/',views.userDetails.as_view(),name='userDetails')
]