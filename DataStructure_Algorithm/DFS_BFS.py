
#
# 스택
# LIFO Last In First Out
# 마지막으로 들어간 요소가 처음으로 나옴
# 프링글스
# 리스트 pop()은 O(k) 시간복잡도를 가짐
stack = []
stack.append(1)
stack.append(3)
stack.append(5)
stack.append(7)
stack.pop()

# 큐
# FIFO First In First Out
# 처음으로 들어간 요소가 처음 나옴
# 줄서기

from collections import deque

queue = deque()

queue.append(1)
queue.append(3)
queue.append(5)
queue.append(7)
queue.popleft()
# 가장 처음 들어온게 맨 왼쪽이므로 popleft()
# 현재 형태는 왼쪽부터 들어가므로
# queue.reverse()를 사용하여 반대로 오른쪽 형태로 바꿀수 있음



# 재귀함수(Recursive Function)
# 자기 자신을 다시 호출하는 함수
# 복잡한 알고리즘을 간결하게 작성할 수 있다
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다
# 예시 유클리드 호제법(최대공약수)

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b, a % b)




# DFS (Depth-Fisrt Search)
# DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# DFS는 스택 자료구조(혹은 재귀함수)를 이용한다
# 1. 탐색 노드를 스택에 삽입하고 방문처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리.
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# 3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복



## BFS (Breath-First Search)
# BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘
# BFS는 큐 자료구조를 이용한다
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복



## 음료수 얼려먹기
# N*M크기의 얼음 틀
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
# 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 건주
# 이때 얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램
#
# 입력조건
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다 (1<=N, M<=1000)
# 두번째 줄 부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1
# 풀이시간 30초, 시간제한 1초, 메모리 제한 128MB
# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력 예시
# 3

# n, m = map(int, input().split())
# ice = []
# for _ in range(n):
#     ice.append(list(map(int, input())))
#
# result = 0
# def dfs(x,y):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
#     if ice[x][y] == 0:
#         ice[x][y] = 1
#         dfs(x - 1,y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1
# print(result)

# 그러니까 n,m입력 받은만큼 2중 포문으로 전부 돌리고
# 0,0을 들어가보고 방문처리(1로 변환)
# 왼, 오, 위, 아래, 다 보고
# 방문 안한 지점이고, 숫자가 0이면 계속(재귀함수)
# 만약 1이면 취소
# 0을 다 찾았으면(더 이상 없으면) (0,0)부터 시작했으니 (0,1)부터 계속하기




# N*M 크기의 직사각형 형태의 미로에 갇혔습니다
# 위치는 (1,1)이며 출구는 (n,m)의 위치에 존재하며, 한 번에 한 칸씩 이동할 수 있다
# 이때 괴물이 있는 부분은 0, 없는 부분은 1로 표시
# 탈출하기 위헤 움직여야 하는 최소 칸의 개수를 구하라(깊이 우선방식인듯)
# 칸을 셀 때는 시작칸과 마지막 칸을 모두 포함해서 계산
#
# 첫째줄에 두 정수 N,M(4<=n, m<=200)이 주어짐
# 다음 n개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다
# 시작칸과 마지막칸은 항상 1
# 시간 제한 30분
# 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 출력 예시
# 10

from collections import deque

def maze_runner(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(maze_runner(0, 0))


