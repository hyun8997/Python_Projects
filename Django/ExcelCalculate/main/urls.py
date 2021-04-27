# main urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),  # 메인 페이지  / 경로
    path('signup', views.signup, name='main_signup'),  # /signup
    path('signin', views.signin, name='main_signin'),  # /signin
    path('verifyCode', views.verifyCode, name='main_verifyCode'),  # /verifyCode
    path('verify', views.verify, name='main_verify'),  # /verify
    path('result', views.result, name='main_result'),  # /result

    path('signup/join', views.join, name='main_join'),
    path('signin/login', views.login, name='main_join'),
    path('logout', views.logout, name='main_logout'),
    path('loginFail', views.loginFail, name='main_loginFail'),
]
