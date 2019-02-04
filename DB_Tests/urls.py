from django.urls import path

from . import views

app_name = 'DB_Tests'
urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name="index2"),
]