from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('groups/', views.groups, name='groups'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_group/', views.add_group, name='add_group'),
    path('delete_user/<str:username>/', views.delete_user, name='delete_user')
]