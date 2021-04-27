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

def verify(request):
    user_code = request.POST['verifyCode']  # verifyCode.html에서 저 이름으로 넘어올 것임
    cookie_code = request.COOKIES.get('code')  # 쿠키에 가입때 넣어둔 랜덤 코드 가져오기

    if user_code == cookie_code:
        user = User.objects.get(id=request.COOKIES.get('user_id'))
        user.user_validate = 1
        user.save()
        response = redirect('main_index')
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        # response.set_cookie('user', user)  # 이제 가입 처리 후, 로그인 정보를 쿠키말고 세션처리하기로

        request.session['user_email'] = user.user_email  # 회원 가입과 동시에 세션에 넣기
        request.session['user_name'] = user.user_name

        return response
    else:
        redirect('main_verifyCode')

def logout(request):
    del request.session['user_email']  # 세션에서 삭제
    del request.session['user_name']
    return redirect('main_signin')

def login(request):
    loginEmail = request.POST['loginEmail']  # signin.html에서 name대로 가져옴
    loginPw = request.POST['loginPW']

    # 회원등록여부 체크
    try:
        user = User.objects.get(user_email=loginEmail)  # 없으면 에러날거니까 에러처리로
    except Exception as e:
        print('e:', e)
        return redirect('main_loginFail')

    # 이메일 체크해서 있으면 넘어오는 곳임, 없으면 에러처리로 실패화면이동함
    # 비밀번호 일치 여부
    if user.user_password == loginPw:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('main_index')
    else:
        return redirect('main_loginFail')

def loginFail(request):
    return render(request, 'main/loginFail.html')
    
    
    
    
    
    
    
    
    
    
