from . import views
from django.urls import path

app_name = 'movie'

urlpatterns= [
    path('', views.index, name='index'),
    path('movies/<int:id>/', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]