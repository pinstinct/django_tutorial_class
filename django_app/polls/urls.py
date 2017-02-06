from django.conf.urls import url
from . import views

urlpatterns = [
    # 아무것도 입력되지 않았을 경우, views.index 호출
    url(r'^$', views.index),
]
