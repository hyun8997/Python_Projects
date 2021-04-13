print()
# 다중 반복문
# 19단 출력
for dan in range(2, 20):
    for i in range(1,20):
        print(dan, '*', i, '=', (dan*i))
    print()  #개행해서 공간을 가질수 있도록 넣음?????

print('-----------------------------')
# 1 ~ 16까지 짝수 출력
for i in range(1, 17):
    if (i%2)==0:
        print(i)

print('-----------------------------')
# 1부터 10까지 출력 - 옆으로 출력
for i in range(1, 11):
    print(i, end=' ')  # end : 입력인수이며, 옆으로 print시 무엇을 붙일지
print('\n')  # 안넣어도 되긴 함 기본이 개행

print('-----------------------------')

# 1부터 10까지의 합을 출력
value = 0
for i in range(1, 11):
    value += i
print(value)





























