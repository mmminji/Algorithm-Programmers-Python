# 2021-05-12
# - 문제 설명
# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.


# == 나의 풀이 == 
def solution(clothes):
    dict = {}
    
    for i in clothes:
        if i[1] in dict:
            lst = dict[i[1]]
            lst.append(i[0])
            dict[i[1]] = lst
        else:
            dict[i[1]] = [i[0]]

    answer = 1
    print(list(dict.values()))
    for j in list(dict.values()):
        answer *= len(j)+1

    return answer-1


# == 다른 풀이1 ==
def solution(clothes):
    answer = 1
    aDict = {}
    for i in clothes:
        if i[1] in aDict:
            aDict[i[1]] += 1
        else:
            aDict[i[1]] = 1
    for i in aDict.keys():
        answer *= aDict[i] +1
    answer -= 1

    return answer


# == 다른 풀이2 ==
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1