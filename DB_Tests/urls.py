from django.urls import path

from . import views

app_name = 'DB_Tests'
urlpatterns = [
    path('', views.index, name='index'),
    #path('wx_passer', views.wx_passer, name="wx_passer"),
    path('wx_passer/<station_id>/<obsdate>/', views.wx_passer, name="wx_passer"),
    path('new_person/<first_name>/<last_name>/', views.new_person, name="New Person")
]