# poll/models.py

from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question
