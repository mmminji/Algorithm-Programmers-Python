# 2021-06-21
# - 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.


# == 나의 풀이 == 
def solution(numbers):    
    from itertools import permutations
    numbers = list(numbers)
    answer = 0

    for i in range(1, len(numbers)+1):
        for j in set([''.join(j) for j in permutations(numbers, i)]):
            if j != '1' and j[0] != '0':
                lst = []
                for k in range(2, int(int(j)**(1/2))+1):
                    lst.append(int(j) % k)

                if 0 not in lst:
                    answer += 1
    
    return answer


# == 다른 풀이 == 에라토스테네스 체
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))  # 모든 조합, 맨앞에 0인거 제외됨(int 다음 set)
    a -= set(range(0, 2))  # 0, 1 제외
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))  # 배수들 모두 제외
    return len(a)   # 남은 소수 개수



# tuple/list to string : string = ''.join(tuple/list)
# string to list : list = list(string)

# 나누기 몫 : //
# 나누기 나머지 : %