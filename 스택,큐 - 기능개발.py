# 2021-06-15
# - 문제 설명
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.


# == 나의 풀이 == 
def solution(progresses, speeds):
    import math
    left_days = []

    for i in range(len(progresses)):
        left_days.append(math.ceil((100-progresses[i]) / speeds[i]))

    a = left_days[0]
    s = 0
    answer = []
    for j in range(1, len(left_days)):
        s += 1 
        if a < left_days[j]:
            answer.append(s)
            a = left_days[j]
            s = 0
        else:
            pass

    answer.append(s+1)                  

    return answer


# == 다른 풀이 ==
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # 시작할 때거나 뒤에 남은날이 더 클 때
            Q.append([-((p-100)//s),1])  # 먼저 배포 [걸린일수, 배포개수]
        else:
            Q[-1][1]+=1   # 다음 개발 포함
    return [q[1] for q in Q]  # 배포 개수만 리스트로



# ceil은 사용하지 않는 방법 : -((p-100)//s) = math.ceil((100-p)/s)