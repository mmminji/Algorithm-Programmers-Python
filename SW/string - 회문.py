# 2021-10-15
# - 문제 설명
# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
 
# 예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
 

# [입력]
 
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

# [출력]
 
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 입력
# 3
# 10 10
# GOFFAKWFSM
# OYECRSLDLQ
# UJAJQVSYYC
# JAEZNNZEAJ
# WJAKCGSGCF
# QKUDGATDQL
# OKGPFPYRKQ
# TDCXBMQTIO
# UNADRPNETZ
# ZATWDEKDQF
# 10 10
# WPMACSIBIK
# STWASDCOBQ
# AMOUENCSOG
# XTIIGBLRCZ
# WXVSWXYYVU
# CJVAHRZZEM
# NDIEBIIMTX
# UOOGPQCBIW
# OWWATKUEUY
# FTMERSSANL
# 20 13
# ECFQBKSYBBOSZQSFBXKI
# VBOAIDLYEXYMNGLLIOPP
# AIZMTVJBZAWSJEIGAKWB
# CABLQKMRFNBINNZSOGNT
# NQLMHYUMBOCSZWIOBINM
# QJZQPSOMNQELBPLVXNRN
# RHMDWPBHDAMWROUFTPYH
# FNERUGIFZNLJSSATGFHF
# TUIAXPMHFKDLQLNYQBPW
# OPIRADJURRDLTDKZGOGA
# JHYXHBQTLMMHOOOHMMLT
# XXCNJGTXXKUCVOUYNXZR
# RMWTQQFHZUIGCJBASNOX
# CVODFKWMJSGMFTCSLLWO
# EJISQCXLNQHEIXXZSGKG
# KGVFJLNNBTVXJLFXPOZA
# YUNDJDSSOPRVSLLHGKGZ
# OZVTWRYWRFIAIPEYRFFG
# ERAPUWPSHHKSWCTBAPXR
# FIKQJTQDYLGMMWMEGRUZ

# 출력
# #1 JAEZNNZEAJ
# #2 MWOIVVIOWM
# #3 TLMMHOOOHMMLT	 


# == 나의 풀이 == 
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append([i for i in input()])
     
    # 가로
    for i in range(n):
        for j in range(n-m+1):
            if lst[i][j:j+m] == lst[i][j:j+m][::-1]:
                ans = lst[i][j:j+m]

     # 세로
    lst_t = []
    for i in list(zip(*lst)):
        lst_t.append(list(i))
    for i in range(n):
        for j in range(n-m+1):
            if lst_t[i][j:j+m] == lst_t[i][j:j+m][::-1]:
                ans = lst_t[i][j:j+m]
                
    print("#{} {}".format(test_case, ''.join(ans)))