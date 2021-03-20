###############################################
# 리스트
list = []

# 리스트 인덱싱
list[0], list[1]
list[-1], list[-2]
# 리스트 슬라이싱
list[0:10], list[:5], list[1:]
list[first:last:step]

# 리스트 삭제
list.pop(index) # pop 인덱스값, 인덱스 없으면 맨 뒤의 값
list.remove(item) # remove 아이템
del list[index] # del 리스트값

# 리스트 삽입
list.append(item) # 리스트 맨 뒤에 값을 넣음
list.insert(index, value) # insert 인덱스, 값

# 기타
list.reverse()      # 리스트 reverse
list.clear()        # 리스트 초기화
list.sort()         # 리스트 정렬
list.copy()         # 리스트 복사, 얕은 복사로 기존 리스트 미변경
list.index(value)   # 특정 value의 인덱스를 반환
list.count(value)   # 특정 value의 개수를 반환
list.extend(list2)  # iteralbe의 모든 항목을 넣는다 / 문자열이면 문자열 한개씩 넣음
# list = [1,2], list2 = [3,4]가 있다고 하면
# list.append(list2) = [1,2,[3,4]]
# list.extend(list2) = [1,2,3,4]

###############################################
# 튜플
# 생성, 삭제, 수정이 불가능
tuple = ()

tuple = (1,2,3)
tuple.index(value) # 특정 value의 인덱스를 반환
tuple.count(value) # 특정 value의 개수를 반환

###############################################
# 딕셔너리
# key와 value를 한 쌍으로 가지고 있다
# key중복을 허용하지 않음
# 순서가 상관이 없다

dict = {'key': 'value'}

dict['key'] = 'value'   # 딕셔러니 추가
dict.pop(key)           # key에 해당하는 요소 삭제
dict.popitem()          # 사전에 마지막으로 삽입된 항목(처음 들어온 항목)을 삭제, 파이썬 3.7이전버전은 임의의 항목 제거
del dict['key']         # key에 해당하는 요소 삭제
dict.clear()            # 모든 요소 삭제
dict['key'].append('value') # dict = {'a':[]} dict에 list가 있을때 사용 가능
                        # dict['a'].append('a.value') == {'a':['a.value']}
dict.update()           # 여러 데이터를 한번에 업데이트
                        # dict.update({'a': 'b.value','b': 'a.value'})
                        # 만약 dict에 key가 없다면 새로 추가한다
dict.get('key', 'default') # key를 토대로 item 반환, 디폴트 값을 줄수있다
                           # 없을시 False 반환하므로 if문에 적합하다
dict.setdefault(key, 'default_value') # get과 비슷하다, key의 값을 찾고, 없을시 default_value로 지정
dict.keys()             # keys 리스트 반환
dict.values()           # values 리스트 반환
dict.items()            # 키, 값 튜플목록 반환
dict.copy()             # 복사본 반환
dict.fromkeys('value1', 'value2', 'value3') # dict의 key순서에 맞게 value가 들어간다

###############################################
# 집합
# set은 수학에서의 집합과 비슷하다
# mutable한 객체
# 순서가 정해져있지 않고, 중복되지 않는 고유한 요소
# 중복된 값이 있을시 제거됨
s = set()
s = {1,2,3}
s2 = {2,3,4,5}
s-s2 or s.difference(s2)   # 차집합
s&s2 or s.intersection(s2) # 교집합
s+s2 or s|s2 or s.union(s2)  # 합집합
s==s2 # 요소가 같은지
s.isdisjoint(s2) # 요소와 타입이 같은지

s.add(value)            # 요소 추가
s.update({value, value})   # 요소 여러개 추가
s.update([value, value])   # 중괄호나 대괄호로 추가 가능
s.remove(value)            # 특정 요소 제거, 없을시 오류
s.discard(value)           # 특정 요소를 안전하게 제거, 없을시 아무일도 없음
s.pop()                    # 임의의 요소를 갖고 온 후 제거
s.clear()                  # 모든 요소 제거

###############################################
# for enumerate
# iterable값의 요소를 가져올때
# 리스트도 같이 받고 싶을때
# enumerate(iterable)을 쓴다

for i in list:
    pass

for index, value in enumerate(list):
    # 인덱스, element를 따로 받을수 있다
    pass

for l in enumerate(list):
    # l = (index, element) 튜플 형태로 인덱스, 요소를 반환함
    pass


###############################################
# 스택
# Last In First Out(LIFO)
# 마지막에 들어온게 처음으로 나간다
# 프링글스

###############################################
# 큐
# First in First Out(FIFO)
# 처음 들어온게 처음으로 나간다
# 줄서기

from collections import deque

###############################################
# 딕셔너리

###############################################
# 기타

# 언팩
print(*list)    # 리스트값
print(*tuple)   #
print(*dict)    # dict는 키값만 가져온다

a,b = list
a,b = tuple
a,b = dict


# 정렬
list2 = sorted(list)    # 반복가능한 개체 정렬후 새로운 값으로 반환

# 특정 문자열 제거

'123,456'.replace(',','') # relace('x를','y로 변경')
'string'.strip()









# https://wikidocs.net/3037 연습문제
import math

naver_closing_price = [
    ['날짜', '요일', '종가'],
    ['9/11', '금', '488,500'],
    ['9/10', '목', '500,500'],
    ['9/09', '수', '501,000'],
    ['9/08', '화', '461,500'],
    ['9/07', '월', '474,500'],
]
naver_closing_price2 = {'09/07':474500, '09/08':461500, '09/09':501000, '09/10': 500500, '09/11':488500}
print(naver_closing_price2['09/09'])
max_price = -math.inf
min_price = math.inf
max_day = ''
min_day = ''
for index, price in enumerate(naver_closing_price):
    if index == 0:
        continue

    num = int(price[2].replace(',', ''))

    if num > max_price:
        max_price = num
        max_day = price[1]

    if num < min_price:
        min_price = num
        min_day = price[1]

    if price[1] == '수':
        print('수요일 종가: ', price[2])




print('최대값: ', max_price)
print('최솟값: ', min_price)

print(f'{max_day}-{min_day}: {max_price-min_price}')

