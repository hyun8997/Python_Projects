print()
'''
리스트나 문자열에서 여러 값을 한꺼번에 가져오는 방법
'''

list = [1, 2, 3, 4, 5]
print(list[1])

text = 'Hello Python World'
print(text[1])

print('-----------------------------------------')
# slice
print(list[1:3])
print(text[1:3])

print('-----------------------------------------')
# 리스트에서 숫자 2부터 끝까지 가져오기
print(list[1:])
print(list[1:len(list)])

# 처음부터 숫자 3까지 가져오기
print(list[:3])
print(list[0:3])

# 처음부터 끝까지
list[:]
print(list[:])
'''
list[:]는 원래 list값을 돌려주지만 자료 구조상 이런식으로 
즉, 원래 값을 주는 것이 아니라 똑같은 값을 가지는 새로운 리스트를 넘겨주는 형태임.
풀어서 보면 리스트를 self로 복사해주는 형태 => 연산낭비

이런 패턴을 파이선3부터는 지양 - anti pattern
anti-pattern : 쓸 수도 있고 실제로도 쓰고 있지만 되도록 쓰지 않길 권하는 사용방식
'''

# 권장 : 명확히 해라.
list2 = [2, 3, 4, 5, 6]
list3 = list2.copy()

print(list3)


print('-----------------------------------------')





























