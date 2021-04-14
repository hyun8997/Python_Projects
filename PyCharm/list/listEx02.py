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

# 리스트에 요소 삽입 : insert
# insert(x, y) : x번째 위치에 y값을 삽입
c.insert(3, 4)
print(c)

# 리스트 요소 제거 : remove
c.remove(4)  # 값을 탐색해서 지워줌
print(c)

c.insert(3, 40)
print(c)
c.remove(40)  # 중복값이 있을 시, 먼저 탐색된놈 하나만 지움
print(c)
c.remove(40)
print(c)

# 리스트 요소 꺼내기(추출) : pop
d = [1, 2, 3]
e = d.pop()
print(d)
print(e)  #추출된 3이 있음

# pop(x) : x번째 요소를 삭제
e = [1, 2, 3, 4, 5]
e.pop(3)
print(e)

print('-------------------------------------------------')
# 리스트에 포함된 요소의 갯수 세기 : count
f = [10, 20, 30, 20, 20, 20]
print(f.count(20))  # count에서 탐색해서 갯수 셈

# 리스트 확장 :extend
g = [1, 2, 3]
g.extend([4, 5])
print(g)
g.extend([6, 7])
print(g)

g += [8, 9]
print(g)






















