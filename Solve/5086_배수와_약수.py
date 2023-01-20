import sys
input = sys.stdin.readline


while(True):
    a, b = map(int, input().split())
    if a == b == 0:
        break

    if b % a == 0:
        print(f"factor")
    elif a % b == 0:
        print(f"multiple")
    else:
        print("neither")
