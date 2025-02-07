from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
