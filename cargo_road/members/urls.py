from django.urls import path
from . import views
urlpatterns = [
    path('login-user', views.login_user, name = "login_user"),
    path('register-user', views.register_user, name='register_user'),
    path('logout-user', views.logout_user, name='logout_user')
]
