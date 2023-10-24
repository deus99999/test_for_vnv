from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Group
from .forms import CreateUser, CreateGroup
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404


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
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('users')
    else:
        form = CreateUser()
    context = {'form': form, 'groups': groups}
    return render(request, 'page/add_user.html', context)


def delete_user(request, username):
    # if request.method == 'POST':
    try:
        User.objects.filter(username=username).delete()
        return redirect('users')
    except User.DoesNotExist:
        raise Http404("User does not exist")


def add_group(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        form = CreateGroup(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('groups')
    else:
        form = CreateGroup()
    context = {'form': form, 'groups': groups}
    return render(request, 'page/add_user.html', context)
