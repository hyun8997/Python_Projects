print()

'''
리스트 관련 함수들
'''

# 리스트에 요소 추가 : append
a = [10, 20, 30]
a.append(40)
print(a)

# append를 통해 어떠한 자료형도 추가 가능
a.append([50, 60])
a.append('hihi')
print(a)

# 리스트 정렬 : sort
b = [2, 34, 23, 12, 35, 45, 22, 6]
b.sort()    #오름차순
print(b)

str = ['wow', 'fantastic', 'python']
str.sort()  #알파벳순
print(str)

# 리스트 역순 : reverse
# 알파벳 역순(내림차순)이 아니고 그대로 역순서임에 유의
str.reverse()
print(str)

# 위치 반환 : index - 리스트에 찾는 값이 있으면 위치값을 리턴
c = [10, 20, 30, 40, 50]
print(c.index(40))  #있으면 인덱스 번호로, 없으면 에러발생















































