# sendEmail urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('send', views.send, name='email_send'),  # 이메일 인증  /email/send
]
