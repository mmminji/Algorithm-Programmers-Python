# 2021-10-20
# - 문제 설명
스마트폰을 무선 충전 할 때 최적의 BC (Battery Charger)를 선택하는 알고리즘을 개발하고자 한다. [그림 1]과 같이 가로 세로 10*10 영역의 지도가 주어졌을 때, 설치된 BC 정보는 다음과 같다.

BC의 충전 범위가 C일 때, BC와 거리가 C 이하이면 BC에 접속할 수 있다. 이때, 두 지점 A(XA, YA), B(XB, YB) 사이의 거리는 다음과 같이 구할 수 있다.

D = |XA – XB| + |YA – YB|

위의 [그림 1]에서 (4,3)과 (5,4) 지점은 BC 1과 BC 3의 충전 범위에 모두 속하기 때문에, 이 위치에서는 두 BC 중 하나를 선택하여 접속할 수 있다.

[그림 2]와 같이 사용자 A와 B의 이동 궤적이 주어졌다고 가정하자. T는 초(Second)를 의미한다. 예를 들어 5초에 사용자 A는 (5, 2) 지점에, 사용자 B는 (6, 9) 지점에 위치한다.

매초마다 특정 BC의 충전 범위에 안에 들어오면 해당 BC에 접속이 가능하다. 따라서 T=5에 사용자 A는 BC 3에, 사용자 B는 BC 2에 접속할 수 있다. 이때, 접속한 BC의 성능(P)만큼 배터리를 충전 할 수 있다. 만약 한 BC에 두 명의 사용자가 접속한 경우, 접속한 사용자의 수만큼 충전 양을 균등하게 분배한다.

BC의 정보와 사용자의 이동 궤적이 주어졌을 때, 모든 사용자가 충전한 양의 합의 최댓값을 구하는 프로그램을 작성하라.
 
[그림 2]에서 T=11일 때, 사용자 A는 BC 1과 3 둘 중 하나에 접속이 가능하다. 같은 시간에 사용자 B는 BC 1에 접속할 수 밖에 없다. 따라서 사용자 A가 같은 BC 1에 접속한다면 충전되는 양를 반씩 나눠 갖게 되어 비효율적이다. 따라서 사용자 A가 BC 3에 접속하는 것이 더 이득이다.

위 예제에서 매 초마다 충전한 양은 다음과 같다. 따라서 총 충전한 양의 총합은 720 + 480 = 1200 이다.

[제약사항]

1. 지도의 가로, 세로 크기는 10이다.

2. 사용자는 총 2명이며, 사용자A는 지도의 (1, 1) 지점에서, 사용자B는 지도의 (10, 10) 지점에서 출발한다.

3. 총 이동 시간 M은 20이상 100이하의 정수이다. (20 ≤ M ≤ 100)

4. BC의 개수 A는 1이상 8이하의 정수이다. (1 ≤ A ≤ 8)

5. BC의 충전 범위 C는 1이상 4이하의 정수이다. (1 ≤ C ≤ 4)

6. BC의 성능 P는 10이상 500이하의 짝수이다. (10 ≤ P ≤ 500)

7. 사용자의 초기 위치(0초)부터 충전을 할 수 있다.

8. 같은 위치에 2개 이상의 BC가 설치된 경우는 없다. 그러나 사용자A, B가 동시에 같은 위치로 이동할 수는 있다. 사용자가 지도 밖으로 이동하는 경우는 없다.
 

[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.

테스트 케이스의 첫 번째 줄에는 총 이동 시간(M), BC의 개수(A)가 주어진다.

그 다음 2개의 줄에는 각각 사용자 A와 B의 이동 정보가 주어진다.

한 사용자의 이동 정보는 M개의 숫자로 구성되며, 각각의 숫자는 다음과 같이 매초마다 이동 방향을 의미한다.

그 다음 줄에는 A개의 줄에 걸쳐 BC의 정보가 주어진다.

하나의 BC 정보는 좌표(X, Y), 충전 범위(C), 처리량(P)로 구성된다.

[출력]

출력은 "#t"를 찍고 한 칸 띄운 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

정답은 모든 사용자의 충전량 합의 최대값을 출력한다.


입력
5
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
 
출력
#1 1200
#2 3290
#3 16620
#4 40650
#5 52710


# == 나의 풀이 == 
T = int(input())
def moveNscore(pos, move_idx, charge):
    pos[0] += move[move_idx][0]
    pos[1] += move[move_idx][1]
    lst = []
    for k in range(len(APs)):
        if abs(pos[0] - APs[k][0])+abs(pos[1]-APs[k][1]) <= APs[k][2]:
            lst.append(k)
    if len(lst) ==0:
        charge.append([a])
    else:
        charge.append(lst)
    return pos, charge
    
for test_case in range(1, T + 1):
    m, a = map(int, input().split())
    amove = [0]+ list(map(int, input().split()))
    bmove = [0] + list(map(int, input().split()))
    APs =[]
    for i in range(a):
        APs.append(list(map(int, input().split())))
    APs.append([0,0,0,0])
    astart = [1,1]
    bstart = [10,10]
    acharge = []
    bcharge = []
    move = [[0,0], [0,-1], [+1,0], [0,+1], [-1,0]]
    for j in range(m+1):
        astart, acharge = moveNscore(astart, amove[j], acharge)
        bstart, bcharge = moveNscore(bstart, bmove[j], bcharge)
    
    ans = 0    
    for alst, blst in zip(acharge, bcharge):
        max_sum = -1
        for aa in alst:
            for bb in blst:
                if aa != bb and APs[aa][3]+APs[bb][3] > max_sum:
                    max_sum = APs[aa][3]+ APs[bb][3]
                elif aa == bb and APs[aa][3]> max_sum:
                    max_sum = APs[aa][3]
        ans += max_sum
    print('#{} {}'.format(test_case, ans))     
        