from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    users = User.objects.order_by('-pub_date')
    context = {'users': users}
    return render(request, 'page/index.html', context)


def add_user(request, user_id):
    pass