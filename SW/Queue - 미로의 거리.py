# 2021-10-19
# - 문제 설명
# NxN 크기의 미로에서 출발지 목적지가 주어진다.

# 이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

# 경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

# 다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

# 13101
# 10101
# 10101
# 10101
# 10021

# 마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


# [입력]

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

# 다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

# 0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 입력
# 3
# 5
# 13101
# 10101
# 10101
# 10101
# 10021
# 5
# 10031
# 10111
# 10101
# 10101
# 12001
# 5
# 00013
# 01110
# 21000
# 01111
# 00000

# 출력
# #1 5
# #2 5
# #3 0


# == 나의 풀이 == 
T = int(input())
def bfs(sx,sy):
    global ans
    q.append((sx, sy))
    visit.append((sx, sy))
    
    while q:
        sx, sy = q.pop(0)
        for mx, my in [(-1,0),(1,0),(0,-1),(0,+1)]:
            x = sx + mx
            y = sy + my
            if 0<=x<n and 0<=y<n and back[x][y] !=1 and back[x][y]!=2 and (x,y) not in visit:
                q.append((x,y))
                visit.append((x,y))
                dist[x][y] = dist[sx][sy] + 1
                if back[x][y] == 3:
                    ans = dist[x][y] -1
                    return
                
for test_case in range(1, T + 1):
    n = int(input())
    back = []
    for i in range(n):
        lst = list(int(i) for i in input())
        if 2 in lst:
            sx, sy = i, lst.index(2)
        back.append(lst)
        
    q= []
    visit = []
    ans = 0
    dist = [[0] *n for _ in range(n)]
    
    bfs(sx, sy)
    print(f'#{test_case} {ans}')