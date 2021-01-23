from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Issue(models.Model):
    PRIORITY_CHOICES = (
        ('H', 1),
        ('HM', 2),
        ('M', 3),
        ('ML', 4),
        ('L', 5),
    )
    TYPE_CHOICES = (
        (1, 'Task'),
        (2, 'Improvement'),
        (3, 'New Feature'),
        (4, 'Bug')
    )
    STATUS_CHOICES = (
        (1, 'Done'),
        (2, 'In Progress'),
        (3, 'To Do')
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE_CHOICES)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True, null=True)
    priority = models.CharField(max_length=12, choices=PRIORITY_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES)
    finish_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    create_date = models.DateField()
