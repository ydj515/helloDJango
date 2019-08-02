from django.db import models

"""
class는 각 하나의 모델
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200) # 필드
    pub_date = models.DateTimeField('date published') # 필드

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text