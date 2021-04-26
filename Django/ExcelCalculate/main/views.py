from django.shortcuts import render, redirect  # redirect 추가
from .models import *
from random import *
from sendEmail.views import *

# main views.py

def index(request):
    return render(request, 'main/index.html')  # templates를 바로 찾아온다
                                    # 앱 자신의 템플릿임을 확인키위해 main이름또 쓰는 것
def signup(request):
    return render(request, 'main/signup.html')

def signin(request):
    return render(request, 'main/signin.html')

def verifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    return redirect('main_index')  # 뷰는 없고 기능만 있으면 되는데, 아직은 메인으로 바로 보냄

def result(request):
    return render(request, 'main/result.html')

def join(request):
    #print('request:', request)
    name = request.POST['signupName']  # signup.html에서 주는 이름 그대로
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name=name, user_email=email, user_password=pw)  # 모델 데이터 넣기
    user.save()  # db에 넣기

    # 인증 코드 관련 4자리 정수로 생성 - 랜덤
    code = randint(1000, 9999)
    # 쿠키에 저장
    response = redirect('main_verifyCode')
    response.set_cookie('code', code)  # 쿠키는 이름이 필수
    response.set_cookie('user_id', user.id)

    # 인증 코드 - 이메일로 전송
    # ==> view에서 template으로 나감 다른 앱이므로 import 필요
    send_result = send(email, code)  # receiverEmail, verifyCode
    if send_result:  # 잘 보내지면 True 리턴
        return response
    else:
        return HttpResponse('이메일 발송에 실패했습니다.')

    #return redirect('main_verifyCode')  # 요청 출력하고 이메일 코드확인 페이지까지
    #return response
