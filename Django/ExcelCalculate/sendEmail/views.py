from django.shortcuts import render
from django.http import HttpResponse  # 응답 객체
from django.core.mail import send_mail, EmailMessage  #email
from django.template.loader import render_to_string  #로더, 렌더링

# sendEmail views.py

# def send(receiverEmail):
#     return HttpResponse('sendEmail views - sendFunction()')


def send(receiverEmail, verifyCode): #이메일과 코드 받아서 사용
    try:
        print(receiverEmail, ' : ', verifyCode)
        content = {'verifyCode': verifyCode}  #dict 권장
        msg_html = render_to_string('sendEmail/email_format.html', content)
        msg = EmailMessage(subject='인증코드발송메일', body=msg_html, from_email='ajrwk1995@gmail.com', bcc=[receiverEmail])
                #제목, 내용바디, 보낸사람, 받는사람 순
        msg.content_subtype='html' #html로 보냄 명시
        msg.send()
        return True
    except:
        print('-----------error----------')
        return False
