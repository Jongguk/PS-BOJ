'''첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.'''
N = int(input())
for i in range(1,N+1):
    for j in range(1,i+1):
        print("*", end="")
    print()

# For 문 2번 쓰지 말고, print("*"*i) 를 이용하면 해결 가능함.
N = int(input())
for i in range(1,N+1):
    print("*"*i)