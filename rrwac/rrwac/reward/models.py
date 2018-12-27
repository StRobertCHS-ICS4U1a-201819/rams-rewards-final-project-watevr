from django.db import models


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
