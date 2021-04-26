# calculate urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate, name='calculate_cal'),  # 엑셀 업로드, 분석  /calculate
]