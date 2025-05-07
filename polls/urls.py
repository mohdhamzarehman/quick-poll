from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_poll, name='create'),
    path('analytics/', views.analytics_view, name='analytics'),
] 