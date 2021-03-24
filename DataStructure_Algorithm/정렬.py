# # 정렬(Sorting) 데이터를 특정한 기준에 따라 순서대로 나열하는 것
#
# # 1. 선택정렬
# # 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것
# # n + (n-1) + (n-2) + ... + 2
# # 시간 복잡도 O(n2)
#
# array = [7,5,9,0,3,1,6,2,4,8]
# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i] #스와프
#
#
# # 2. 삽입 정렬
# # 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# # 선택 정렬에 비해 구현 난이도가 높지만, 일반적으로 빠름
# # 시간복잡도 O(n2) 최선의 경우 O(n)
#
# array = [7,5,9,0,3,1,6,2,4,8]
# for i in range(1, len(array)):
#     for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
#         if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break
#
#
# # 3. 퀵 정렬
# # 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# # 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리
# # 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정한다
# # 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로(nlogn)를 기대할 수 있다
# # 하지만 최악은 O(n2)의 시간복잡도
#
# def quick_sort(array, start, end):
#     if start>=end: # 원소가 1개인 경우 종료
#         return
#     pivot = start # 피벗은 첫번째 원소
#     left = start +1
#     right = end
#     while(left <= right):
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while(left <= end and array[left] <= array[pivot]):
#             left +=1
#         # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while(right > start and array[right] >= array[pivot]):
#             right -= 1
#         if(left > right): # 왼쪽, 오른쪽이 엇갈렸다면, 작은 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#         else: # 정방향이면 작은 데이터와 큰 데이터 교체
#             array[left], array[right] = array[right], array[left]
#     # 분할 이후 왼쪽과 오른쪽 부분에서 각각 퀵소트 수행
#     quick_sort(array, start, right -1)
#     quick_sort(array, right + 1, end)
# quick_sort(array, 0, len(array)-1)
# # print(array)
# # 파이썬의 장점을 살린 방식
#
# def quick_sort2(array):
#     if len(array)<=1:
#         return array
#     pivot = array[0] # 피벗은 첫번째 원소
#     tail = array[1:] # 피벗을 제외한 리스트
#
#     left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
#     right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
# # 4. 계수 정렬
# # 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
# # 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
# # 데이터의 개수가 N 데이터(양수)중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N+K)를 보장한다
# # 계수 정렬의 시간복잡도와 공간 복잡도는 모두 O(N+K)
# # 계수 정렬은 때에 따라서 심각한 비효율성 초래
# # ex)데이터가 0과 999999로 단 2개만 존재하는 경우
# # 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용 가능
# # ex) 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적
#
# # 모든 원소의 값이 0보다 크거나 같다고 가정
# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# # 모든 범위를 포함하는 리스트 선언(0으로 초기화)
# count = [0] * (max(array)+1)
#
# for i in range(len(array)):
#     count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가
#
# for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
#     for j in range(count[i]): # count의 기록된 값 만큼 반복하여 출력
#         pass
#         # print(i, end=' ')


# 선택정렬 시간복잡도 O(n2) 공간복잡도 O(n) 아이디어 간단
# 삽입정렬 시간복잡도 O(n2) 공간복잡도 O(n) 데이터가 거의 정렬되어 있을 때는 가장 빠름
# 퀵 정렬 시간복잡도 O(nlogn) 공간복잡도 O(n) 대부분의 경우에 가장 적합하며 충분히 빠름
# 계수정렬 시간복잡도 O(n+k) 공간복잡도 O(n+k) / 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작
# 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(nlogn)을 보장하도록 설계


# n, k = map(int, input().split())
# list2 = []
# list2.append(list(map(int, input().split())))
# list2.append(list(map(int, input().split())))
n, k = 5, 3
list2 = [[1, 2, 5, 4, 3], [5, 5, 6, 6, 5]]
import random
import time
list2 = [[random.randrange(10000000) for i in range(500000)], [random.randrange(10000000) for i in range(500000)]]
list2[0].sort()
list2[1].sort(reverse=True)
one = max(list2[0])
two = max(list2[1])
a = list2[0]
b = list2[1]
if one>two:
    k=one
else:
    k=two

start = time.time()
for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break
print(sum(a))
# 위는 동영상 강의
# 내가 만든거
# for j in range(k):
#     if min(list2[0])<max(list2[1]):
#         list2[0][list2[0].index(min(list2[0]))], list2[1][list2[1].index(max(list2[1]))] = max(list2[1]), min(list2[0])
#     else:
#         break
# print(sum(list2[0]))
## min, max, index 하는게 시간이 엄청 걸리네...
## 
end = time.time()
print(end-start)