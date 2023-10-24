from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Group
from .forms import CreateUser
from django.shortcuts import render, get_object_or_404, redirect


def users(request):
    users = User.objects.order_by('-created')
    context = {'users': users}
    return render(request, 'page/users.html', context)


def groups(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'page/groups.html', context)


def add_user(request):
    groups = Group.objects.all()
    error = ''
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            print('saved')
            return redirect('users')
        if request.method == 'GET':
            error = "Form is incorrect."
    else:
        form = CreateUser()
    context = {'form': form, 'error': error, 'groups': groups}
    return render(request, 'page/add_user.html', context)


