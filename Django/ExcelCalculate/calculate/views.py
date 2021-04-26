from django.shortcuts import render
from django.http import HttpResponse  # 응답 객체

# calculate views.py

def calculate(request): #요청만 열어둠
    return HttpResponse('calculate views - calculate function()')
