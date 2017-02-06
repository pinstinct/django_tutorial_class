from django.conf.urls import url
from . import views

urlpatterns = [
    # 아무것도 입력되지 않았을 경우, views.index 호출
    # ex: /polls/
    url(r'^$', views.index),

    # 숫자 1개 이상이면, views.detail 호출
    # 이때, question_id에 패턴을 넣어 넘겨준다.
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
