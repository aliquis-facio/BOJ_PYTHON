import sys
input = sys.stdin.readline

T: int = int(input())

for i in range(T):
    a, b = map(int, input().split()) # 1 <= a < 100, 1 <= b < 1,000,000
    a %= 10
    # 일의 자리 숫자만 확인하면 됨

    if a == 0:
        print(10)
        continue
    # a가 10, 20, ..., 90일 때 나머지가 0이 되므로
    # 이럴 때는 10을 출력하고 다음 케이스로

    remainder_cycle = [a] # 같은 숫자로 곱하게 되는 경우 나머지가 주기적으로 반복됨
    tmp: int = a

    for j in range(b - 1): # a = a ^ 1. 즉, 이미 한 번 곱한 것과 같기 때문에 b - 1번 반복
        tmp = (tmp * a) % 10 # tmp값에 a를 곱하고 10으로 나눈 나머지로 tmp값 갱신 (너무 커지지 않게 하기 위해서)
        if tmp in remainder_cycle: # 나머지가 반복되는 것을 확인했으면 for문 종료
            break
        else: # 아닐 경우 나머지를 remainder_cycle 리스트에 넣기
            remainder_cycle.append(tmp)

    print(remainder_cycle[b % len(remainder_cycle) - 1])
    # b를 reaminder_cycle의 길이, 즉 곱할 횟수를 반복되는 주기로 나눈 나머지값에서 리스트 인덱스는 0에서 시작하기 때문에 1을 빼줌
