import sys
input = sys.stdin.readline


def oct2bin(char_num):
    base = ['000', '001', '010', '011', '100', '101', '110', '111']
    print(int(base[int(char_num[0])]), end='')
    for c in char_num[1:]:
        print(base[int(c)], end='')


oct_num = input().strip()
oct2bin(oct_num)
