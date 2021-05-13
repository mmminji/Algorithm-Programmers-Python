# - 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421

# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.


# == 나의 첫 번째 풀이 91.7% == 
def solution(phone_book):
    phone_book.sort(key=len)
    
    while len(phone_book) != 0:
        
        length = len(phone_book[0])
        for i in range(len(phone_book)-1):
            if phone_book[0] == phone_book[i+1][:length]:
                return False
            else :
                pass
        phone_book.remove(phone_book[0])
    return True


# == 나의 두 번째 풀이(참고) == 
def solution(phone_book):

    dict = {}
    for i in phone_book:
        dict[i] = 1

    for j in phone_book:
        a = ''
        for k in j:
            a += k
            if (a in dict) & (a != j):
                return False
    return True            
            

# == 다른 풀이 ==
def solution(phone_book):
    phoneBook = sorted(phone_book)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True