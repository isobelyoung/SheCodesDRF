from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    no_pledges = models.IntegerField(default=0)
    date_created = models.DateTimeField() 
    end_date = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
        # connect project to a user, and related_name vice versa
    )
    

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = 'supporter_pledges'
    )

class Project_Update(models.Model):
    project_update = models.TextField()
    project_update_date = models.DateTimeField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='project_updates'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = 'project_owner_updates'
    )
    update_picture = models.URLField(blank = True)