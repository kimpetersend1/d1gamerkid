import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# ForeignKey: https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.ForeignKey

class Question(models.Model):
    question_text = models.CharField(max_length=200) # question_text, pub_date = field instance
    pub_date = models.DateTimeField('date published')

    # __str__() method
    # https://docs.djangoproject.com/en/1.9/ref/models/instances/#django.db.models.Model.__str__
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # default value of votes to 0

    def __str__(self):
        return self.choice_text
