# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    # 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정

# 파이썬 이진 탐색 라이브러리
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
bisect_left(a, x)   # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a, x)  # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반한
# print : 2, 4
# 값이 특정 범위에 속하는 데이터 개수 구하기
# 왼쪽 인덱스, 오른쪽 인덱스 구해서 빼주면 개수를 구할수 있다


# 파라메트릭 서치
# 최적화 문제를 결정 문제(예, 아니오)로 바꾸어서 해결하는 기법
    # ex) 특정한 조건을 만족하는 가장 알맞는 값을 빠르게 찾는 최적화 문제
# 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결 가능
#0942~1022

# n, m = map(int, input().split())
# dduck = list(map(int, input().split()))
n, m = 5, 3
dduck = [19,15,10,17,13]
start = 0
end = max(dduck)

result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2
    for i in dduck:
        if i>mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

# print(result)

# 1046
from bisect import bisect_left, bisect_right
# n, x = map(int, input().split())
# array = list(map(int, input().split()))
n, x = 7, 2
array = [1,1,2,2,2,3]
left = bisect_left(array, x)
right = bisect_right(array, x)

if right-left==0:
    print(-1)
else:
    print(right-left)




