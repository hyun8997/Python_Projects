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

    # grade별 value 의 최소값, 최대값, 평균값
    # grade별 구분
    grade_dic = {}
    total_row_num = len(df.index)

    for i in range(total_row_num):
        data = df.loc[i]

        if not data['grade'] in grade_dic.keys():
            grade_dic[data['grade']] = [data['value']]
        else:
            grade_dic[data['grade']].append(data['value'])

        print(grade_dic.keys(), '--', grade_dic.values())

    # # grade별 value 의 최소값, 최대값, 평균값
    grade_calculate_dic = {}
    for key in grade_dic.keys():
        grade_calculate_dic[key] = {}
        grade_calculate_dic[key]['min'] = min(grade_dic[key])
        grade_calculate_dic[key]['max'] = max(grade_dic[key])
        grade_calculate_dic[key]['avg'] = float(sum(grade_dic[key])/len(grade_dic[key]))

    #print(list(grade_calculate_dic.keys()))

    print('------------------------------')
    grade_list = list(grade_calculate_dic.keys())
    grade_list.sort()   # 딕셔너리라서 key의 순서가 보장되지 않음

    for key in grade_list:
        print('--- grage --- ', key)
        print('-- min : ', grade_calculate_dic[key]['min'], end=' ')
        print('-- max : ', grade_calculate_dic[key]['max'], end=' ')
        print('-- avg : ', grade_calculate_dic[key]['avg'], end='\n')

    print('------------------------------------')

    # 이메일 도메인별 인원 구하기
    domain_dic = {}

    for i in range(total_row_num):
        data = df.loc[i]
        # pos = data['email'].find('@')    # 데이터에서 email 중 @ 이후의 도메인 수집
        # domain_data = data['email'][pos+1:]
        domain_data = (data['email'].split('@'))[1]  # 데이터에서 email 중 @ 이후의 도메인 수집

        if not domain_data in domain_dic.keys():
            domain_dic[domain_data] = 1
        else:
            domain_dic[domain_data] = domain_dic[domain_data] + 1

        print(domain_dic.keys(), '--', domain_dic.values())

    for key in domain_dic.keys():   # 도메인 딕셔너리 출력
        print(key, ':', domain_dic[key])

    for key in domain_dic.keys():  # 2개 이상인 도메인 출력하기
        if domain_dic[key] > 1:
            print(key)

    return HttpResponse('calculate views - calculate function()')
