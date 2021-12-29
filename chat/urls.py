from django.urls import path
from . import views


app_name="chat"
urlpatterns = [
    path('', views.home, name='home'),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
    path('<str:room>/<str:username>/', views.room, name="room"),
    path('checkview/', views.checkview, name='checkview'),
    path('send/', views.send, name='send'),
]
