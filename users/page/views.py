from django.http import HttpResponse
from .models import User, Group
from .forms import CreateUser, CreateGroup
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404


def users(request):
    users = User.objects.order_by('-created')
    context = {'users': users, 'title': 'Users'}
    return render(request, 'page/users.html', context)


def groups(request):
    groups = Group.objects.all()
    context = {'groups': groups, 'title': 'Groups'}
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
    context = {'form': form, 'groups': groups, 'title': 'Add User'}
    return render(request, 'page/add_user.html', context)


def update_user(request, username):
    upd_user = User.objects.get(username=username)

    if request.method == 'POST':
        form = CreateUser(request.POST, instance=upd_user)
        if form.is_valid():
            form.save()  # Сохраняем обновленные данные
            return redirect('users')  # Перенаправляем на страницу успеха
    else:
        form = CreateUser(instance=upd_user)
    context = {'form': form, 'title': 'Update User'}
    return render(request, 'page/add_user.html', context)


def delete_user(request, username):
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
    context = {'form': form, 'groups': groups, 'title': 'Add Group'}
    return render(request, 'page/add_user.html', context)


def update_group(request, title):
    upd_group = Group.objects.get(title=title)
    if request.method == 'POST':
        form = CreateGroup(request.POST, instance=upd_group)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = CreateGroup(instance=upd_group)
    context = {'form': form, 'title': 'Update Group'}
    return render(request, 'page/add_group.html', context)


def delete_group(request, group_id):
    """can delete group only if there are no users in this group"""
    users_of_group = User.objects.filter(group_id=group_id)
    if users_of_group:
        try:
            Group.objects.filter(id=group_id).delete()
            return redirect('groups')
        except Group.DoesNotExist:
            raise Http404("Group does not exist")
    else:
        return render(request, 'page/add_group.html')

