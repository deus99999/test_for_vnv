from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('groups/', views.groups, name='groups'),
    path('add_user/', views.add_user, name='add_user'),
   # path('save_user/', views.save_user, name='save_user'),
]