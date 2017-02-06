from django.db import models


# 데이터베이스가 어떻게 만들어질지 정의
class Question(models.Model):
    q_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    c_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
