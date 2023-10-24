from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('groups/', views.groups, name='groups'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_group/', views.add_group, name='add_group'),
    path('delete_user/<str:username>/', views.delete_user, name='delete_user'),
    path('delete_group/<str:group_id>/', views.delete_group, name='delete_group'),
    path('<str:username>/update_user/', views.update_user, name='update_user'),
    path('<str:title>/update_group/', views.update_group, name='update_group'),
]