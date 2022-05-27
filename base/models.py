from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    daily_calorie_consumption = models.IntegerField(null=True, blank=True)
    exercise_daily_calores_burned = models.IntegerField(null=True, blank=True)
    daily_hours_fasted = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['date']