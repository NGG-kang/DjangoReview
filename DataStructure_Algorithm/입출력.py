input() # 한 줄의 문자열을 입력받는 함수
input().split() # 공백을 기준으로 입력받음

map() #리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# 입력을 공백으로 나누고, map을 사용하여 int로 각 원소마다 적용후, 리스트로 변환
list(map(int, input().split()))

# 3개의 원소만 들어온다면
a,b,c = map(int, input().split())


# 빠르게 입력 받기
# 사용자로부터 입력을 최대한 빠르게 받기
import sys
data = sys.stdin.readline().rstrip()
# 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용


# 표준 출력방법
print() # print함수롤 이용
# 기본적으로 출력 이후에 줄 바꿈을 수행
# 줄바꿈을 원치 않은경우 end 속성 이용 가능
print('a', end=" ")
print('b')
# a b  출력

# f-string
answer=1
print(f"{answer}")

