# DFS/BFS 네트워크

[TOC]



## 문제 설명

네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

### 제한사항

- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
- 각 컴퓨터는 0부터 `n-1`인 정수로 표현합니다.
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
- computer[i][i]는 항상 1입니다.

### 입출력 예

| n    | computers                         | return |
| ---- | --------------------------------- | ------ |
| 3    | [[1, 1, 0], [1, 1, 0], [0, 0, 1]] | 2      |
| 3    | [[1, 1, 0], [1, 1, 1], [0, 1, 1]] |        |

### 입출력 예 설명

예제 #1
아래와 같이 2개의 네트워크가 있습니다.
<img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/5b61d6ca97/cc1e7816-b6d7-4649-98e0-e95ea2007fd7.png" alt="image0.png" style="zoom: 25%;" />

예제 #2
아래와 같이 1개의 네트워크가 있습니다.
<img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/7554746da2/edb61632-59f4-4799-9154-de9ca98c9e55.png" alt="image1.png" style="zoom: 25%;" />



## DFS

```python
def dfs(i, computers, visited):
    n = len(computers)
    visited[i] = True
    if i==n:
        return
    for j in range(len(computers[i])):
        print(j)
        if j==i:
            continue
        if computers[i][j]==1 and visited[j] == False:
            visited[j] = True
            dfs(j, computers, visited)
            
# 1. 이어지지 않는다면? 다음 번호로 넘어가는 과정이 필요
# 2. 전부 탐색하고 값을 어떻게 받아야 할지...

        

def solution(n, computers):
    visited = [False]*n
    answer = 0
    for i in range(n):  # 0번방부터 전부 탐색
        if visited[i] == False:
            dfs(i, computers, visited) # 끝까지 닿았다면 빠져나와서 
            answer += 1                # answer += 1
    return answer
```



## BFS

```python
from collections import deque
def bfs(computers, visited, q):
    while q:
        computer = q.pop()
        for j in range(len(computer)):
            if visited[j]==False and computer[j]==1:
                visited[j] = True
                q.appendleft(computers[j])
            
        
        

def solution(n, computers):
    visited = [False]*n
    answer = 0
    # BFS
    q = deque()
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            q.appendleft(computers[i])
            bfs(computers, visited, q)
            answer += 1

    return answer
```

​            

## 해결

이어진 방을 찾아야 하므로 for문을 돌려 전부 찾아야 하는건 BFS와 DFS는 동일하다

하지만 queue와 재귀함수를 사용함의 차이 정도?

DFS는 바로 재귀를 돌려 다음 연결지점을 찾고

BFS는 일단 큐에 집어 넣어 전부 확인후에 다음 연결을 찾는것이다