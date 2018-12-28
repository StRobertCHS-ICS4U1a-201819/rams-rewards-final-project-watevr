from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Reward(models.Model):
    reward_name = models.CharField('Activity Name', max_length=30)
    reward_object = models.CharField('The one who gets the points', max_length=30)
    date = models.DateField('Activity Date', auto_now_add=True)
    description = models.TextField()
    points = models.IntegerField()

    class Meta:
        db_table = 'reward'

    def __str__(self):
        return self.reward_name


class Student(AbstractUser):
    qrCode = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    student_points = models.IntegerField('points', default=0)
    rank = models.IntegerField('rank', default=0)
    student_description = models.TextField(max_length=300)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.username
