
score = 85
result = "Success" if score >= 80 else "Fail"

# 다른 프로그래밍 언어와 다르게 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용 가능
if 0 < score < 20:
    pass

array = []
# for의 배열 방문시
for i in array:
    print(i)
# for의 range
for i in range(start=0,stop=10,step=1):
    pass


# lambda
# 매개변수, 함수내용, 들어갈 값 순서로 넣는디
plus = (lambda a,b: a+b)(3,5)

#기본 sorted 사용 함수
def my_key(x):
    return x[1]
sorted(array, key=my_key)

#위와 같은 lambda 함수
sorted(array, key = lambda x: x[1])

list1, list2 = [], []
result = map(lambda a,b:a+b,list1,list2)



# 표준 라이브러리

# itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공
# 특히 순열과 조합라이브러리, 코딩테스트에서 자주 사용됨
#
# heapq: 힙 자료구조를 제공
# 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
#
# bisect: 이진탐색(Binary Search)기능을 제공
# collections: 덱(deque), 카운터(Counter)등의 유용한 자료구조를 포함
# math: 필수적인 수학적 기능을 제공
# 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함

sum([1,2,3,4,5])
min(7,3,2,5)
max(7,3,2,5)
eval("(3+5)*7") # 계산식을 수로 반환

# sorted()
sorted([1,4,6,9,7])
sorted([1,4,6,9,7], reverse=True)
# sorted() with key
# key속성으로 정렬 기준을 줄 수 있다
result = sorted(array, key=lambda x: x[1], reverse=True)


# 순열과 조합
모든 경우의 수를 고려해야 할 때 어떤 라이브러리를 쓸까

순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
{'A', 'B', 'C'} 에서 세 개를 선택하여 나열하는 경우: 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

조합: 서로 다른n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
{'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우: 'AB', 'AC', 'BC'

순열의 수: nPr = n*(n-1)*(n-2)* ... * (n-r+1)
조합의 수: nCr = n*(n-1)*(n-2)* ... * (n-r+1) / r!


# 순열 예시
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data, 3)) # 3개를 선택하여 나열하는 경우

# 조합 예시
from itertools import combinations
data = ['A','B','C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합

from itertools import product
data = ['A','B','C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)

from itertools import  combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)


# Counter
# 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지를 알려줌
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # blue가 등장한 횟수 출력 : 3
print(counter['green']) # green이 등장한 횟수 출력 : 1
print(dict(counter)) # 사전 자료형으로 반환

# 최대공약수, 최소공배수
import math
def lcm(a,b):
    return a*b // math.gcd(a,b)
a=21
b=14
print(math.gcd(21,14)) # 최대 공약수(GCD) 계산
print(lcm(21,14)) # 최소 공배수(LCM) 계산
# 최소공배수는 곱한 값의 최대공약수를 나눈 몫이 최소공배수
# a * b // gcd(a,b)