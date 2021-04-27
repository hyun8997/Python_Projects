from django.shortcuts import render
from django.http import HttpResponse  # 응답 객체
import pandas as pd  # pandas 추가

# calculate views.py

def calculate(request): #요청만 열어둠
    file = request.FILES['fileInput']  # 파일 자체를 업로드한게 아니고 정보를 담아둔 것
    # 파일은 DB에 올리는거랑 서버에 올리는거랑 다르다.

    # print(file)

    # 받아있는 데이터가 테이블 형태로 잘 정리된 엑셀 파일임
    # pandas 사용해서 데이터 간단 분석
    df = pd.read_excel(file, sheet_name='Sheet1', header=0)
    # sheet_name:엑셀파일 시트명, 가진 파일에는 Sheet1임
    # header
    # print(df.head(5))  # 적당히 5개 잘라서 출력

    # grade별 value의 최소값, 최대값, 평균값
    # grade별 구분
    grade_dic = {}
    total_row_num = len(df.index)  # 길이 구함

    # for i in range(total_row_num):
    #     data = df.loc[[i], ['grade'], ['name'], ['']]
    #
    #     if not data['grade'] in grade_dic.keys():  # 데이터는 컬럼 이름으로 찾아올 수 있음
    #         grade_dic[data['grade']] = [data['value']]  # 키(grade)마다 값(value) 넣어줌
    #     else:
    #         grade_dic[data['grade']].append(data['value'])
    #
    # # grade별 value의 최소값, 최대값, 평균값
    # grade_calculate_dic = {}
    # for key in grade_dic.keys():
    #     grade_calculate_dic[key] = {}
    #     grade_calculate_dic[key]['min'] = min(grade_dic[key])
    #     grade_calculate_dic[key]['max'] = max(grade_dic[key])
    #     grade_calculate_dic[key]['avg'] = float(sum(grade_dic[key])/len(grade_dic[key]))



    return HttpResponse('calculate views - calculate function()')
