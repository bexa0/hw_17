from django.utils import timezone
from django.db import models


class Task(models.Model):
    choises_for_status = [('1', 'высокий'), ('2', 'средний'), ('3', 'низкий')]

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=255, choices=choises_for_status)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, default='in process')
    completed_at  = models.DateTimeField(null=True, blank=True, default=timezone.now)
    image = models.ImageField(upload_to='',)

    def __str__(self):
        return self.title


class ActionType(models.Model):
    action_name = models.CharField(max_length=255)

    def __str__(self):
        return self.action_name


class Actions(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    action = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    made_at = models.DateTimeField()

    def __str__(self):
        return f"{self.action} {self.title} {self.made_at}"
