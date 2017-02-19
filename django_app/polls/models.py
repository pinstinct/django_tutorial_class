import datetime
from django.db import models
from django.utils import timezone

# 데이터베이스가 어떻게 만들어질지 정의
class Question(models.Model):
    q_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.q_text

    def was_published_recently(self):
        """
        최근에 발행된 Question 인가 판단해주는 메서드
        :return: Boolean
        """
        # 자신의 발행일자 >= 현재시각 - 하루만큼의 시간간
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    c_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text
