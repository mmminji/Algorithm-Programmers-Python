# 2021-06-14
# - 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.


# == 나의 풀이 == 
def solution(answers):
    import numpy as np

    answer1 = [1,2,3,4,5]*2000
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000

    x,y,z = 0,0,0

    for i in range(len(answers)):
        a,b,c,k = answer1[i], answer2[i], answer3[i], answers[i]
        if a==k:
            x +=1
        if b==k:
            y +=1
        if c==k:
            z +=1

    max = np.max(np.array((x,y,z)))

    sol = []
    l=1
    for i in [x,y,z]:
        if i == max:
            sol.append(l)
        l += 1
    return sol


# == 다른 풀이 ==
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)  # 사람수만큼 점수리스트

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]: # 나머지를 이용해서 반복효과
                s[i] += 1
            print(s)
    return [i + 1 for i, v in enumerate(s) if v == max(s)]  # for문 이용해서 리스트에 담기(append없이)