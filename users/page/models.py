from django.db import models
from django.utils import timezone


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False, max_length=1000)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    created = models.DateField(default=timezone.now)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username



