from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Todo(models.Model):
    class Status(models.TextChoices):
        DONE = "DONE", "Done"
        IN_PROGRESS = "IN_PROGRESS", "in progress"
        DRAFT = "DRAFT", "draft"
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=11, choices=Status.choices, default=Status.DRAFT)
    creat_time = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
