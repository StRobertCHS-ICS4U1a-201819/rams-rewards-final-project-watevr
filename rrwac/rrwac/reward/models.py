from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Student(AbstractUser):
    student_points = models.IntegerField('points', default=0)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.username


class Reward(models.Model):
    reward_number = models.BigAutoField(primary_key=True)
    reward_name = models.CharField('Activity Name', max_length=30)
    reward_object = models.ManyToManyField(Student)
    date = models.DateField('Activity Date', auto_now_add=True)
    description = models.TextField(max_length=300, default="You don't have any description yet")
    points = models.IntegerField(default=0)

    class Meta:
        db_table = 'reward'

    def __str__(self):
        return self.reward_name
