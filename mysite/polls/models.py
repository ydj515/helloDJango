import datetime

from django.db import models
from django.utils import timezone

"""
class는 각 하나의 모델
"""


def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Question(models.Model):
    question_text = models.CharField(max_length=200) # 필드
    pub_date = models.DateTimeField('date published') # 필드

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text