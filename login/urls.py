from django.urls import path

from . import views

app_name = 'Login'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_login/', views.new_login, name='New Login')
]